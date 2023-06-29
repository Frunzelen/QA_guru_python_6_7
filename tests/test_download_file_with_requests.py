import os.path

import requests
import selenium

from tests.conftest import path_to_TMP

# TODO оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь

url = 'https://selenium.dev/images/selenium_logo_square_green.png'
path_png_file = os.path.abspath(os.path.join(path_to_TMP, 'selenium_logo.png'))


def test_download_file_png(tmp_dir_manager):
    response = requests.get(url)
    with open(path_png_file, 'wb') as file:
        file.write(response.content)

    assert os.path.exists(path_png_file)

    print(os.path.getsize(path_png_file))

    assert (os.path.getsize(path_png_file)) == 30803

    os.remove(path_png_file)
