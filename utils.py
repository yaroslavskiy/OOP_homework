from itertools import chain


def avg_students_grades_on_course(students, course):
    grades = list(chain.from_iterable([student.grades.get(course, []) for student in students]))
    return round(sum(grades) / len(grades), 1) if grades else 0.0


def avg_lecturer_grades_on_course(lecturers, course):
    grades = list(chain.from_iterable([lecturer.grades.get(course, []) for lecturer in lecturers]))
    return round(sum(grades) / len(grades), 1) if grades else 0.0
