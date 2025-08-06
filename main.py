from mixins import AvgGradeMixin, CompareMixin
from utils import avg_students_grades_on_course, avg_lecturer_grades_on_course


class Student(AvgGradeMixin, CompareMixin):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        is_lecturer = isinstance(lecturer, Lecturer)
        is_course_attached = course in lecturer.courses_attached
        is_student_on_course = course in self.courses_in_progress
        is_correct_grade = grade in range(11)

        if not all((is_lecturer, is_course_attached, is_student_on_course, is_correct_grade)):
            return 'Ошибка'
        else:
            lecturer.grades.setdefault(course, list()).append(grade)

    def __str__(self):
        about = {
            'Имя': self.name,
            'Фамилия': self.surname,
            'Средняя оценка за домашние задания': self.avg_grade,
            'Курсы в процессе изучения': ', '.join(self.courses_in_progress),
            'Завершенные курсы': ', '.join(self.finished_courses)
        }
        return '\n'.join(f'{key}: {value}' for key, value in about.items())


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, AvgGradeMixin, CompareMixin):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        about = {
            'Имя': self.name,
            'Фамилия': self.surname,
            'Средняя оценка за лекции': self.avg_grade
        }
        return '\n'.join(f'{key}: {value}' for key, value in about.items())


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        is_student = isinstance(student, Student)
        is_course_attached = course in self.courses_attached
        is_student_on_course = course in student.courses_in_progress
        is_correct_grade = grade in range(11)

        if not all((is_student, is_course_attached, is_student_on_course, is_correct_grade)):
            return 'Ошибка'
        else:
            student.grades.setdefault(course, list()).append(grade)

    def __str__(self):
        about = {
            'Имя': self.name,
            'Фамилия': self.surname
        }
        return '\n'.join(f'{key}: {value}' for key, value in about.items())


student_1 = Student('Иван', 'Студентов')
student_2 = Student("Пётр", 'Студентов-Второй')
lecturer_1 = Lecturer('Иван', 'Лекторов')
lecturer_2 = Lecturer('Пётр', 'Лекторов-Второй')
reviewer_1 = Reviewer('Иван', 'Ревьюеров')
reviewer_2 = Reviewer('Пётр', 'Ревьюеров-Второй')

student_1.courses_in_progress += ['Python', 'SQL']
student_1.finished_courses += ['HTML/CSS']
reviewer_1.courses_attached += ['Python']
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
print(reviewer_1.rate_hw(student_1, 'Django', 9))  # Ошибка
print(reviewer_1.rate_hw(student_1, 'Python', 11))  # Ошибка
print()

print(student_1)
print()

student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['SQL']
reviewer_2.courses_attached += ['Python']
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 8)
print(student_2)
print()
print(student_1 == student_2, student_1 > student_2)  # False True
print()

lecturer_1.courses_attached += ['Python', 'SQL']
lecturer_2.courses_attached += ['SQL']
student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 5)
student_1.rate_lecture(lecturer_1, 'SQL', 10)
print(student_2.rate_lecture(lecturer_1, 'SQL', 10))  # Ошибка
print()
student_1.rate_lecture(lecturer_1, 'SQL', 7)

print(lecturer_1)
print()
student_1.rate_lecture(lecturer_2, 'SQL', 8)
student_1.rate_lecture(lecturer_2, 'SQL', 7)
student_1.rate_lecture(lecturer_2, 'SQL', 5)
print(lecturer_2)
print(lecturer_1 == lecturer_2, lecturer_1 > lecturer_2)  # False, True
print()

print(avg_students_grades_on_course([student_1, student_2], 'Python'))
print(avg_lecturer_grades_on_course([lecturer_1, lecturer_2], 'Python'))
