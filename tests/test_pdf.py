from pypdf import PdfReader
import os


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

# Читаем файл pdf
def test_pdf():
    reader = PdfReader(os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources/docs-pytest-org-en-latest.pdf')))
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)

    # Проверяем наличие данных в файле pdf
    assert 412 == len(reader.pages)
    assert "Jul 14, 2022" in text
