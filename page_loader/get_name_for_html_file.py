from urllib.parse import urlparse
import re


def get_name_for_html_file(url):
    u = urlparse(url)
    name_for_html_file = re.sub(r'[^A-Za-z0-9]', "-", u.netloc + u.path) + ".html"
    return name_for_html_file
