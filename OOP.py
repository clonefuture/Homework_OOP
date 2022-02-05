class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and 0 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print('Ошибка')

    def avg_grades(self):
        sm = 0
        cnt = 0
        for i in self.grades:
            sm += sum(self.grades[i])
            cnt += len(self.grades[i])
        if cnt == 0:
            return 0
        return sm / cnt

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'\
              f'Средняя оценка за домашние задания: {round(self.avg_grades(), 2)}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет такого студента')
            return
        return self.avg_grades() < other.avg_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grades(self):
        sm = 0
        cnt = 0
        for i in self.grades:
            sm += sum(self.grades[i])
            cnt += len(self.grades[i])
        if cnt == 0:
            return 0
        res = sm / cnt
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'\
            f'Средняя оценка за лекции: {round(self.avg_grades(), 2)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет такого лектора')
            return
        return self.avg_grades() < other.avg_grades()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_student = Student('Roy', 'Eman', 'man')
best_student.courses_in_progress += ['Java', 'C#']

last_student = Student('Moon', 'Fun', 'women')
last_student.courses_in_progress += ['Java']

good_student = Student('Luke', 'Skywalker', 'man')
good_student.courses_in_progress += ['Java', 'Python', 'C#']
good_student.finished_courses += ['Введение в программирование']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Java']
cool_mentor.courses_attached += ['C#']

master_mentor = Reviewer('Darth', 'Vader')
master_mentor.courses_attached += ['Java']
master_mentor.courses_attached += ['Python']
master_mentor.courses_attached += ['C#']

fst_lecturer = Lecturer('Every', 'Buddy')
fst_lecturer.courses_attached += ['Java']
fst_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Obi-Wan', 'Kenobi')
second_lecturer.courses_attached += ['Java']
second_lecturer.courses_attached += ['C#']

master_mentor.rate_hw(best_student, 'Java', 10)
cool_mentor.rate_hw(best_student, 'C#', 6)
cool_mentor.rate_hw(best_student, 'Java', 9)

master_mentor.rate_hw(last_student, 'Java', 6)
cool_mentor.rate_hw(last_student, 'Java', 9)
master_mentor.rate_hw(good_student, 'Java', 10)

master_mentor.rate_hw(good_student, 'Python', 8)
master_mentor.rate_hw(good_student, 'C#', 5)
cool_mentor.rate_hw(good_student, 'Java', 10)

good_student.rate_lec(fst_lecturer, 'Python', 9)
last_student.rate_lec(fst_lecturer, 'Java', 5)
best_student.rate_lec(second_lecturer, 'C#', 10)
good_student.rate_lec(second_lecturer, 'Java', 5)

print(f'{best_student}\n')
print(f'{last_student}\n')
print(f'{good_student}\n')
print(f'''\nReviewers:\n
{cool_mentor}\n
{master_mentor}\n''')

print(f'''\nLecturers:\n
{fst_lecturer}\n
{second_lecturer}\n''')

print()

students = [best_student, good_student, last_student]
lecturers = [fst_lecturer, second_lecturer]


def avg_rate_hw(students, course):
    sum_grades = 0
    sum_cnt_grades = 0
    for student in students:
        for crs in student.grades:
            if crs == course:
                sum_grades += sum(student.grades[crs])
                sum_cnt_grades += len(student.grades[crs])
    if sum_cnt_grades == 0:
        return 'Нет оценок'
    return f'Средняя оценка студентов по предмету {course} - {sum_grades / sum_cnt_grades}'


print(avg_rate_hw(students, 'C#'))


def avg_rate_lec(lecturers, course):
    sum_grades = 0
    sum_cnt_grades = 0
    for lecturer in lecturers:
        for crs in lecturer.grades:
            if crs == course:
                sum_grades += sum(lecturer.grades[crs])
                sum_cnt_grades += len(lecturer.grades[crs])
    if sum_cnt_grades == 0:
        return 'Нет оценок'
    return f'Средняя оценка лекторов по предмету {course} - {sum_grades / sum_cnt_grades}'


print(avg_rate_lec(lecturers, 'Java'))