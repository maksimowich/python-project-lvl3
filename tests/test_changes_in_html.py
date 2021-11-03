from page_loader.page_loader import download
import tempfile
import pook


@pook.on
def test_changes_in_html1():
    with open("tests/fixtures/test_changes_in_html1/fixture1", encoding='utf8') as f:
        html = f.read()
    pook.get(
        'https://ru.hexlet.io/courses',
        reply=200,
        response_json=html
    )
    pook.get(
        'https://ru.hexlet.io/assets/professions/nodejs.png',
        reply=200,
        response_json=""
    )
    with tempfile.TemporaryDirectory() as d:
        name_for_html_file = download("https://ru.hexlet.io/courses", d)
        with open(d + "/" + name_for_html_file, encoding='utf8') as f:
            actual_value = f.read().rstrip("\n")
    with open("tests/fixtures/test_changes_in_html1/fixture2", encoding='utf8') as f:
        expected_value = f.read().rstrip("\n")
    assert actual_value == expected_value


@pook.on
def test_changes_in_html2():
    with open("tests/fixtures/test_changes_in_html2/fixture1", encoding='utf8') as f:
        html = f.read()
    mock = pook.get(
        'https://ru.hexlet.io/courses',
        reply=200,
        response_json=html
    )
    pook.get(
        'https://ru.hexlet.io/assets/application.css',
        reply=200,
        response_json=""
    )
    pook.get(
        'https://ru.hexlet.io/courses',
        reply=200,
        response_json=""
    )
    pook.get(
        'https://ru.hexlet.io/assets/professions/nodejs.png',
        reply=200,
        response_json=""
    )
    pook.get(
        'https://ru.hexlet.io/packs/js/runtime.js',
        reply=200,
        response_json=""
    )
    with tempfile.TemporaryDirectory() as d:
        name_for_html_file = download("https://ru.hexlet.io/courses", d)
        with open(d + "/" + name_for_html_file, encoding='utf8') as f:
            actual_value = f.read().rstrip("\n")
    with open("tests/fixtures/test_changes_in_html1/fixture2", encoding='utf8') as f:
        expected_value = f.read().rstrip("\n")
    assert actual_value == expected_value
    assert mock.calls == 1
