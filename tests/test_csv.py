import csv
import os.path

# TODO оформить в тест, добавить ассерты и использовать универсальный путь
# Задаем уникальный путь к файлу csv
csv_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources/csv_for_test.csv'))


# Создаем файл csv и записываем в него данные
def test_csv():
    with open(csv_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    # Проверяем наличие созданного файла
    assert os.path.exists(csv_file)


# Читаем и проверяем файл csv
def test_read_csv():
    with open(csv_file) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            assert len(row) == 3

    # Удаляем созданный файл csv
    os.remove(csv_file)
