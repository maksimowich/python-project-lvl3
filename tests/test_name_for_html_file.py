from page_loader.get_name_for_html_file import get_name_for_html_file


def test_get_name_for_html_file1():
    url = "https://ru.hexlet.io/courses"
    actual_value = get_name_for_html_file(url)
    expected_value = "ru-hexlet-io-courses.html"
    assert actual_value == expected_value


def test_get_name_for_html_file2():
    url = "https://wooordhunt.ru/word/mock"
    actual_value = get_name_for_html_file(url)
    expected_value = "wooordhunt-ru-word-mock.html"
    assert actual_value == expected_value
