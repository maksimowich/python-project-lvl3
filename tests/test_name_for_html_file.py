from page_loader.get_name import get_name
from urllib.parse import urlparse


def test_get_name_for_html_file1():
    url = "https://ru.hexlet.io/courses"
    parsed_url = urlparse(url)
    actual_value = get_name(parsed_url, ".html")
    expected_value = "ru-hexlet-io-courses.html"
    assert actual_value == expected_value


def test_get_name_for_html_file2():
    url = "https://wooordhunt.ru/word/mock"
    parsed_url = urlparse(url)
    actual_value = get_name(parsed_url, ".html")
    expected_value = "wooordhunt-ru-word-mock.html"
    assert actual_value == expected_value
