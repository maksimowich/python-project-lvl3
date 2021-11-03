import logging
import os
import re
import requests
from progress.bar import Bar
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from page_loader.get_name import get_name

file_logger = logging.getLogger('app_file_logger')
console_logger = logging.getLogger('app_console_logger')


def download_resources_and_get_correct_soup(parsed_url, response, path_to_dir_to_download, session):
    file_logger.info("Entered to the download_resources function")
    dir_of_resources_name = get_name(parsed_url, "_files")
    path_to_dir_of_resources = path_to_dir_to_download + "/" + dir_of_resources_name
    soup = BeautifulSoup(response.text, "html.parser")
    create_dir_of_resources_if_not_exist(path_to_dir_of_resources)
    file_logger.info("Start making tag cycle")
    for tag in Bar('Processing').iter(soup.find_all(["img", "link", "script"])):
        if tag.name == "script" and tag.get('src') is None:
            continue
        file_logger.info(tag)
        parsed_tag_url = get_parsed_tag_url(tag)
        file_logger.info(parsed_tag_url)
        if parsed_tag_url.netloc == "" or parsed_tag_url.netloc == parsed_url.netloc:
            file_logger.info("Resource suitable for downloading has been found")
            download_resource_and_correct_soup(path_to_dir_of_resources, dir_of_resources_name, parsed_tag_url,
                                               parsed_url, tag, session)
    console_logger.info("Exit of the func download_resources")
    return soup


def get_resource_name(parsed_resource_url):
    extension = parsed_resource_url.path.split(".")[-1]
    if extension in ["js", "png", "jpg", "css", "svg"]:
        index_of_last_dot = parsed_resource_url.path.rfind(".")
        return re.sub(r'[^A-Za-z0-9]', "-", parsed_resource_url.netloc + parsed_resource_url.path[:index_of_last_dot]) + "." + extension
    else:
        return get_name(parsed_resource_url, ".html")


def create_dir_of_resources_if_not_exist(path_to_dir_of_resources):
    if not os.path.exists(path_to_dir_of_resources):
        os.mkdir(path_to_dir_of_resources)


def get_open_format(tag_name):
    if tag_name == "img":
        return "wb"
    else:
        return "w"


def get_parsed_tag_url(tag):
    if tag.name == "script" or tag.name == "img":
        return urlparse(tag.get('src'))
    elif tag.name == "link":
        return urlparse(tag.get('href'))


def download_resource_and_correct_soup(path_to_dir_of_resources, dir_of_resources_name, parsed_tag_url, parsed_url, tag, session):
    file_logger.info("Enter to download particular resource function")
    resource_name = get_resource_name(parsed_tag_url._replace(netloc=parsed_url.netloc))
    open_format = get_open_format(tag.name)
    with open(path_to_dir_of_resources + "/" + resource_name, open_format) as out_file:
        if open_format == "wb":
            try:
                out_file.write(
                    session.get(parsed_url.scheme + "://" + parsed_url.netloc + parsed_tag_url.path).content)
            except Exception as e:
                file_logger.exception("Something wrong with HTTP request for resource")
                console_logger.critical("Something wrong with HTTP request for resource")
                raise e
        else:
            try:
                out_file.write(
                    requests.get(parsed_url.scheme + "://" + parsed_url.netloc + parsed_tag_url.path).text)
            except Exception as e:
                file_logger.exception("Something wrong with HTTP request for resource")
                console_logger.critical("Something wrong with HTTP request for resource")
                raise e
        file_logger.info('Resource downloaded')
        tag["src"] = dir_of_resources_name + "/" + resource_name
