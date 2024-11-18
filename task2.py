# TODO импортировать необходимые молули
import csv  # импортируем csv и json
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as input_file:  # открываем и считываем файл csv
        csv_data = csv.DictReader(input_file)
        rows = list(csv_data)  # столбец

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as output:  # открываем json файл
        json.dump(rows, output, indent=4)  # отступы = 4

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")  # печатаем json строку
