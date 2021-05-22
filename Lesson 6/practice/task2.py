# Создать структуру данных для студентов из имен и фамилий, можно случайных. Придумать структуру данных, чтобы
# указывать, в какой группе учится студент (Группы Python, FrontEnd, FullStack, Java). Студент может учиться в
# нескольких группах. Затем вывести:
# студентов, которые учатся в двух и более группах
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java

PYTHON = "Python"
FRONT_END = "FrontEnd"
FULL_STACK = "FullStack"
JAVA = "Java"


def get_student_full_name(student):
    return f"{student['first_name']} {student['last_name']}"


students = [{
    "first_name": "Andrei",
    "last_name": "Petrov",
    "groups": [PYTHON, JAVA]
}, {
    "first_name": "Anton",
    "last_name": "Sydorov",
    "groups": [JAVA]
}, {
    "first_name": "Alexei",
    "last_name": "Grigoriev",
    "groups": [PYTHON, FRONT_END, JAVA]
}, {
    "first_name": "Sergei",
    "last_name": "Antonov",
    "groups": [FULL_STACK]
}, {
    "first_name": "Igor",
    "last_name": "Pavlov",
    "groups": [PYTHON, FRONT_END]
}]

# студенты, которые учатся в двух и более группах
print("\nStudents are studying in 2 or more groups:")
print("\n".join(list(map(get_student_full_name, filter(lambda student: len(student["groups"]) >= 2, students)))))

# студентов, которые не учатся на фронтенде
print("\nStudents are not studying in front_end:")
print("\n".join(list(map(get_student_full_name, filter(lambda student: FRONT_END not in student["groups"], students)))))

# студентов, которые изучают Python или Java
print("\nStudents are studying in java or python:")
print("\n".join(list(map(get_student_full_name,
                         filter(lambda student: PYTHON in student["groups"] or JAVA in student["groups"], students)
                         ))))
