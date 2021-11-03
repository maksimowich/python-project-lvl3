import logging.config
import os
import requests
from urllib.parse import urlparse
from page_loader.get_name import get_name
from page_loader.download_resources_and_get_correct_soup import download_resources_and_get_correct_soup
from page_loader.exceptions import Not200StatusResponse
from page_loader.exceptions import NonExistingDirectory
from page_loader.settings import logger_config


logging.config.dictConfig(logger_config)
file_logger = logging.getLogger('app_file_logger')
console_logger = logging.getLogger('app_console_logger')


def download(url, path_to_dir_to_download):

    with requests.Session() as session:

        check_path_for_existence(path_to_dir_to_download)

        response = make_request_and_get_response(session, url)

        check_response_for_status_200(response)

        parsed_url = urlparse(url)
        soup = download_resources_and_get_correct_soup(parsed_url, response, path_to_dir_to_download, session)

        file_logger.info('Get name for main HTML file')
        html_file_name = get_name(parsed_url, ".html")
        with open(path_to_dir_to_download + "/" + html_file_name, "w") as output_file:
            output_file.write(soup.prettify())
        file_logger.info("Main HTML file was downloaded")
        return path_to_dir_to_download + html_file_name


def check_path_for_existence(path):
    if not os.path.exists(path):
        file_logger.exception("Invalid directory was specified")
        console_logger.critical("Invalid directory was specified")
        raise NonExistingDirectory()


def make_request_and_get_response(session, url):
    try:
        file_logger.info("Try to make HTTP request")
        response = session.get(url)
    except Exception as e:
        file_logger.exception("HTTP request for page HTML cannot be done")
        console_logger.critical("HTTP request for page HTML cannot be done")
        raise e
    return response


def check_response_for_status_200(response):
    if response.status_code != 200:
        file_logger.exception("Bad response status")
        console_logger.critical("Bad response status")
        raise Not200StatusResponse
    file_logger.info("HTTP response has status 200!")
