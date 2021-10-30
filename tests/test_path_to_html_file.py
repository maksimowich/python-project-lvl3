from page_loader.page_loader import download
import tempfile
import os
import pook


@pook.on
def test_path_to_html_file1():
    mock = pook.get(
        'https://ru.hexlet.io/courses',
        reply=200,
        response_json={'testing': 'on'}
    )
    with tempfile.TemporaryDirectory() as d:
        name_for_html_file = download("https://ru.hexlet.io/courses", d)
        assert os.path.exists(d + "/" + name_for_html_file)
        assert mock.calls == 1


@pook.on
def test_path_to_html_file2():
    mock = pook.get(
        'https://wooordhunt.ru/word/mock',
        reply=200,
        response_json={'testing': 'on'}
    )
    with tempfile.TemporaryDirectory() as d:
        name_for_html_file = download('https://wooordhunt.ru/word/mock', d)
        assert os.path.exists(d + "/" + name_for_html_file)
        assert mock.calls == 1
