from page_loader.get_name_for_html_file import get_name_for_html_file
from page_loader.page_loader import download
import tempfile
import os
import pook
import requests


@pook.on
def test_changes_in_html1():
    with open("tests/fixtures/fixture1", encoding='utf8') as f:
        html = f.read()
    mock = pook.get(
        'https://ru.hexlet.io/courses',
        reply=200,
        response_json=html
    )
    mock2 = pook.get(
        'https://ru.hexlet.io/assets/professions/nodejs.png',
        reply=200,
        response_json=""
    )
    with tempfile.TemporaryDirectory() as d:
        name_for_html_file = download("https://ru.hexlet.io/courses", d)
        with open(d + "/" + name_for_html_file, encoding='utf8') as f:
            actual_value = f.read().rstrip("\n")
    with open("tests/fixtures/fixture2", encoding='utf8') as f:
        expected_value = f.read().rstrip("\n")
    assert actual_value == expected_value
