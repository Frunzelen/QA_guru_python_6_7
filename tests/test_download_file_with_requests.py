import os.path

import requests
import selenium

from tests.conftest import path_to_TMP

# TODO оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь
url = 'https://selenium.dev/images/selenium_logo_square_green.png'
path_png_file = os.path.abspath(os.path.join(path_to_TMP, 'selenium_logo.png'))


def test_download_file_png(tmp_dir_manager):
    response = requests.get(url)

    assert os.path.exists('selenium_logo.png')

    with open('selenium_logo.png', 'wb') as file:
        file.write(response.content)
        print(os.path.getsize('selenium_logo.png'))

    assert (os.path.getsize('selenium_logo.png')) == 30803
