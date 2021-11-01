import re


def get_name(url, extension):
    name_for_html_file = re.sub(r'[^A-Za-z0-9]', "-", url.netloc + url.path) + extension
    return name_for_html_file
