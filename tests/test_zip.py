"""Создать новые тесты, которые заархивируют имеющиеся в resources различные типы файлов
в один архив в tmp и проверят тестом в архиве каждый из файлов, что он является тем самым,
который был заархивирован, не распаковывая архив."""

import os
import zipfile

from tests.conftest import path_to_TMP

# Путь до файлов
resources_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources'))

# Путь к файлам, которые будем архировать
path_resources_files = os.listdir(resources_directory)

# Путь к архиву
path_zip_file = os.path.abspath(os.path.join(path_to_TMP, 'test_zip'))

def test_created_zip_file(tmp_dir_manager):
    with zipfile.ZipFile(path_zip_file, mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zip_archive:
        for file in path_resources_files:
            add_file = os.path.join(resources_directory, file)
            zip_archive.write(add_file, arcname=file)

    with zipfile.ZipFile(path_zip_file) as zip_archive:
        assert len(path_resources_files) == len(zip_archive.infolist())

    for file in path_resources_files:
            info = zip_archive.getinfo(file)