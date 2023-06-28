import glob
import os
import pytest

path_to_TMP = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp'))

@pytest.fixture(scope='function', autouse=False)
def tmp_dir_manager():
    if not os.path.exists(path_to_TMP):
        os.makedirs(path_to_TMP)

    yield

    files = glob.glob(os.path.join(path_to_TMP, '*'))
    for f in files:
        os.remove(f)


