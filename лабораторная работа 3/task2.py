# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, comma=','):  # объявили функцию принимающую две строки
    Group_One = first_group.split(comma)  # объявляем разделитель для первой группы
    Group_Two = second_group.split(comma)  # объявляем разделитель для второй группы
    common_participants = list(set(Group_One).intersection(Group_Two))  # создаём список общих участников двух групп
    return sorted(common_participants)   # возвращаем общий список отсортированных участников

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print("Общие участники:", find_common_participants(participants_first_group, participants_second_group, "|"))

