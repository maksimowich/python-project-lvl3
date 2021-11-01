import requests
import os
from urllib.parse import urlparse
from page_loader.get_name import get_name
from page_loader.download_imgs_and_get_correct_soup import download_images_and_get_correct_soup


def download(url, path_to_dir_to_download):
    if os.path.exists(path_to_dir_to_download):
        response = requests.get(url)
        parsed_url = urlparse(url)

        soup = download_images_and_get_correct_soup(parsed_url, response, path_to_dir_to_download)

        html_file_name = get_name(parsed_url, ".html")
        with open(path_to_dir_to_download + "/" + html_file_name, "w") as output_file:
            output_file.write(soup.prettify())
        return html_file_name

    else:
        return "Directory doesn't exist"
