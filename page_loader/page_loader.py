import requests


def download(url, path_to_dir_to_download):
    r = requests.get(url)
    print(r.text)

