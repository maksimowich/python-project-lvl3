import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from page_loader.get_name import get_name


def download_images_and_get_correct_soup(parsed_url, response, path_to_dir_to_download):
    dir_of_images_name = get_name(parsed_url, "_files")
    soup = BeautifulSoup(response.text, "html.parser")

    for tag_img in soup.find_all("img"):
        parsed_img_url = urlparse(tag_img['src'])
        if parsed_img_url.scheme == "" or parsed_img_url.netloc == parsed_url.netloc:
            if not os.path.exists(path_to_dir_to_download + "/" + dir_of_images_name):
                os.mkdir(path_to_dir_to_download + "/" + dir_of_images_name)
            img_name = get_img_name(parsed_img_url._replace(netloc=parsed_url.netloc))
            with open(path_to_dir_to_download + "/" + dir_of_images_name + "/" + img_name, "wb") as out_img:
                out_img.write(requests.get(parsed_url.scheme + "://" + parsed_img_url.netloc + parsed_img_url.path).content)
                tag_img["src"] = dir_of_images_name + "/" + img_name

    return soup


def get_img_name(parsed_img_url):
    extension = (parsed_img_url.netloc + parsed_img_url.path).split(".")[-1]
    if extension in ["png", "jpg"]:
        return re.sub(r'[^A-Za-z0-9]', "-", parsed_img_url.netloc + parsed_img_url.path[:-4]) + "." + extension
