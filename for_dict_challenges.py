from collections import Counter, defaultdict

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students_1 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]


def cnt_occur(list_students):
    cnt_occur_students = Counter([stud["first_name"] for stud in list_students])
    for student in cnt_occur_students:
        print(f"{student}: {cnt_occur_students[student]}")


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students_2 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]


def max_cnt_occur(list_students):
    cnt_occur_students = Counter([stud["first_name"] for stud in list_students])
    print(cnt_occur_students.most_common(1)[0][0])


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ], [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


def most_occur_name_in_by_classes(classes):
    for grade, class_ in enumerate(classes, start=1):
        cnt_occur_students = Counter([stud["first_name"] for stud in class_])
        name = cnt_occur_students.most_common(1)[0][0]
        print(f"Самое частое имя в классе {grade}: {name}")


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school_1 = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male_1 = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


def cnt_male_and_female(school_classes, genders):
    gender_by_classes = defaultdict(Counter)
    for class_ in school_classes:
        grade = class_["class"]
        gender_in_class = list()
        for student in class_["students"]:
            name = student["first_name"]
            gender_in_class.append(genders[name])
        gender_by_classes[grade] += Counter(gender_in_class)
    for class_, genders in gender_by_classes.items():
        male = genders.get(True, 0)
        female = genders.get(False, 0)
        print(f"Класс {class_}: девочки {female}, мальчики: {male}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school_2 = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male_2 = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}


def max_cnt_male_and_female_by_class(school_classes, genders):
    gender_by_classes = defaultdict(list)
    for class_ in school_classes:
        grade = class_["class"]
        gender_in_class = list()
        for student in class_["students"]:
            name = student["first_name"]
            gender_in_class.append(genders[name])
        gender_by_classes[grade] += gender_in_class

    max_male = 0
    max_female = 0
    max_male_class = None
    max_female_class = None

    for grade, genders in gender_by_classes.items():
        cnt_male = genders.count(True)
        cnt_female = genders.count(False)
        if cnt_male > max_male:
            max_male = cnt_male
            max_male_class = grade
        if cnt_female > max_female:
            max_female = cnt_female
            max_female_class = grade
    print(f"Больше всего мальчиков в классе {max_male_class}")
    print(f"Больше всего девочек в классе {max_female_class}")


if __name__ == '__main__':
    cnt_occur(students_1)
    max_cnt_occur(students_2)
    most_occur_name_in_by_classes(school_students)
    cnt_male_and_female(school_1, is_male_1)
    max_cnt_male_and_female_by_class(school_2, is_male_2)
