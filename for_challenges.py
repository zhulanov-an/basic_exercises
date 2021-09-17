# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names_1 = ['Оля', 'Петя', 'Вася', 'Маша']


def new_line_print(words: list):
    print(*words, sep='\n')


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names_2 = ['Оля', 'Петя', 'Вася', 'Маша']


def print_name_and_cnt_char(words: list):
    for word in words:
        print(f"{word}:{len(word)}")


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names_3 = ['Оля', 'Петя', 'Вася', 'Маша']


def print_sex(people_list: list, people_dict: dict):
    for human in people_list:
        sex = 'male' if people_dict[human] else "female"
        print(f"{human}: {sex}")


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups_1 = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]


def group_information(multigroups: list):
    print(f"Всего {len(multigroups)} групп(ы)")
    for num_group in range(1, len(multigroups)):
        print(f"Группа {num_group}: {len(multigroups[num_group - 1])} человек(а)")


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups_2 = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]


# ???
def detail_group_information(multigroups: list):
    for num_group in range(1, len(multigroups)):
        print(f"Группа {num_group}: {multigroups[num_group - 1]}")


if __name__ == '__main__':
    new_line_print(names_1)
    print_name_and_cnt_char(names_2)
    print_sex(names_3, is_male)
    group_information(groups_1)
    detail_group_information(groups_2)