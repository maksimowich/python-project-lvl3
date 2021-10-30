import requests
import os
from page_loader.get_name_for_html_file import get_name_for_html_file


def download(url, path_to_dir_to_download):
    if os.path.exists(path_to_dir_to_download):
        response = requests.get(url)
        html_file_name = get_name_for_html_file(url)
        with open(path_to_dir_to_download + "/" + html_file_name, "w") as output_file:
            output_file.write(response.text)
        return html_file_name
    else:
        return None
