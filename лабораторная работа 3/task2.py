# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, comma=','):
    Group_One = first_group.split(comma)
    Group_Two = second_group.split(comma)
    common_participants = list(set(Group_One).intersection(Group_Two))
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print("Общие участники:", find_common_participants(participants_first_group, participants_second_group, "/"))
