# TODO импортировать необходимые молули
import csv  # импортируем csv и json
import json

INPUT_FILENAME = "input.csv"  # присваиваем имена файлам
OUTPUT_FILENAME = "output.json"


def task() -> None:  # объявляем функцию
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as input_file:  # открываем файл CSV для чтения
        csv_data = csv.DictReader(input_file)  # десериализуем данные и создаем словари "ключ-значение"
        rows = list(csv_data)  # создаем список со словарями

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as output:  # открываем файл JSON для записи
        json.dump(rows, output, indent=4)  # сериализуем в строку формата JSON с отступом 4

if __name__ == '__main__':
    # нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:  # открываем файл JSON для чтения
        for line in output_f:  # проходимся по каждой строке
            print(line, end="")  # выводим значения с разделителем в виде запятой и разделителем строк "\n"
