# Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.

MAX_SUBJECT_RATING = 12


def create_rating_for_subjects(subjects_tuple, rating_tuple):
    return dict(zip(subjects_tuple, rating_tuple))


def get_student_with_max_average(students):
    min_value = -1
    s_data = None

    for s in students:
        average = students[s]["average"]
        if average > min_value:
            min_value = average
            s_data = students[s]
            s_data.update(name=s)

    return s_data


def get_student_with_min_average(students, max_average):
    min_value = max_average
    s_data = None

    for s in students:
        average = students[s]["average"]
        if average < min_value:
            min_value = average
            s_data = students[s]
            s_data.update(name=s)

    return s_data


school_subjects_tuple = ("mathematics", "physics", "geometry", "computer science")
school_students = ("Ivanov", "Petrov", "Sidorov", "Somebody4")
school_students_rating = dict(zip(
    school_students,
    ((8, 9, 10, 11), (2, 3, 4, 5), (3, 4, 5, 6), (9, 5, 12, 6))
))

school_rating = {}

for student in school_students:
    student_data = school_students_rating[student] or dict(zip(student, (0, 0, 0, 0)))
    total = sum(student_data)

    school_rating[student] = dict(
        subjects=create_rating_for_subjects(school_subjects_tuple, student_data),
        total=total,
        average=total / len(student_data)
    )

first_student = get_student_with_max_average(school_rating)
last_student = get_student_with_min_average(school_rating, MAX_SUBJECT_RATING)

print(f'Best student - {first_student["name"]}')
print(f'Worst student - {last_student["name"]}')
