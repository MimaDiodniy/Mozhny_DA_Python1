# TODO решите задачу
import json  # импортируем json

file_name = "input.json"


def func() -> float:
    with open(file_name, 'r') as file:
        data_json = json.load(file)  #читаем json файл

        multi_values = [item["score"] * item["weight"] for item in data_json]  # произведения двух значений
        summ_values = sum(multi_values)  # находим сумму произведений двух значений
    return round(summ_values, 3)  # возвращаем значение, округлённое до 3 знаков после запятой


if __name__ == '__main__':
    print(func())  # печатаем полученную сумму
