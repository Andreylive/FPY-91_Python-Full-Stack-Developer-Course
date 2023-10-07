from statistics import mean


class Student:
    """Describe work of student class"""
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        """Describe how studets rate lecturers"""
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def mean_score(self):
        """Describe how mean score calculated for student"""
        return mean(list(self.grades.values()))

    def __str__(self):
        """Change print function"""
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                F"Средняя оценка за домашние задания: {mean(list(self.grades.values()))}\n"
                f"Rурсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                F"Завершенные курсы: {', '.join(self.finished_courses)}"
                )

    def __gt__(self, other):
        """Change __gt__ function"""
        mean_score_1 = self.mean_score()
        mean_score_2 = other.mean_score()
        if mean_score_1 > mean_score_2:
            print(True)
            print(f"Средняя оценка {self.name} {self.surname} равна {mean_score_1}")
            print(f"Средняя оценка {other.name} {other.surname} равна {mean_score_2}")
            return True
        elif mean_score_1 < mean_score_2:
            print(False)
            print(f"Средняя оценка {self.name} {self.surname} равна {mean_score_1}")
            print(f"Средняя оценка {other.name} {other.surname} равна {mean_score_2}")
            return False

    def __ge__(self, other):
        """Change __ge__ function"""
        mean_score_1 = self.mean_score()
        mean_score_2 = other.mean_score()
        if mean_score_1 >= mean_score_2:
            print(True)
            print(f"Средняя оценка {self.name} {self.surname} равна {mean_score_1}")
            print(f"Средняя оценка {other.name} {other.surname} равна {mean_score_2}")
            return True
        else:
            print(False)
            print(f"Средняя оценка {self.name} {self.surname} равна {mean_score_1}")
            print(f"Средняя оценка {other.name} {other.surname} равна {mean_score_2}")
            return False

    def __eq__(self, other):
        """Change __eq__ function"""
        mean_score_1 = self.mean_score()
        mean_score_2 = other.mean_score()
        if mean_score_1 == mean_score_2:
            print(True)
            print(f"Средняя оценка {self.name} {self.surname} равна {mean_score_1}")
            print(f"Средняя оценка {other.name} {other.surname} равна {mean_score_2}")
            return True
        else:
            print(False)
            print(f"Средняя оценка {self.name} {self.surname} равна {mean_score_1}")
            print(f"Средняя оценка {other.name} {other.surname} равна {mean_score_2}")
            return False

    def __ne__(self, other):
        """Change __ne__ function"""
        mean_score_1 = self.mean_score()
        mean_score_2 = other.mean_score()
        if mean_score_1 != mean_score_2:
            print(True)
            print(f"Средняя оценка {self.name} {self.surname} равна {mean_score_1}")
            print(f"Средняя оценка {other.name} {other.surname} равна {mean_score_2}")
            return True
        else:
            print(False)
            print(f"Средняя оценка {self.name} {self.surname} равна {mean_score_1}")
            print(f"Средняя оценка {other.name} {other.surname} равна {mean_score_2}")
            return False


class Mentor:
    """Describe parent mentor class"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    """Describe child lectuter class from parent mentor class"""
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {mean([mean(i) for i in list(self.grades.values())])}\n"
                )


class Reviewer(Mentor):
    """Describe child reviewer class from parent mentor class"""
    def rate_hw(self, student, course, grade):
        """Describe how reviewer can rate students"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'

    def __str__(self):
        """Change print function"""
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# Create students and their sets of courses
# Student 1
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'SQL', 'Advanced Python']
best_student.finished_courses += ['Physics', 'GIT']
print(best_student.courses_in_progress, best_student.finished_courses)

# Student 2
best_student_2 = Student('Andrei', 'Pshenichnyi', 'male')
best_student_2.courses_in_progress += ['Python', 'SQL', 'Advanced Python']
best_student_2.finished_courses += ['Physics', 'GIT']
print(best_student_2.courses_in_progress, best_student_2.finished_courses)

# Create reviewers? their courses and ratings
cool_reviewer = Reviewer('Ivan', 'Mulin')
cool_reviewer.courses_attached += ['Python', 'SQL', 'Advanced Python']
print(cool_reviewer.courses_attached)

# Rate the first student by reviewer
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'SQL', 5)
print(best_student.grades)

# Rate the second student by reviewer
cool_reviewer.rate_hw(best_student_2, 'Python', 3)
cool_reviewer.rate_hw(best_student_2, 'SQL', 8)
print(best_student_2.grades)

# Create lecturers and their courses and raitings
# Lecturer 1
best_lecturer = Lecturer('Albert', 'Einstein')
best_lecturer.courses_attached += ['Physics', 'GIT']

# Lecturer 2
best_lecturer_2 = Lecturer('Isaac', 'Newton')
best_lecturer_2.courses_attached += ['Physics', 'GIT']

# Rate lecturers by students

# Rate lecturer 1 by 2 studets
best_student.rate_hw(best_lecturer, 'Physics', 10)
best_student.rate_hw(best_lecturer, 'GIT', 2)
best_student_2.rate_hw(best_lecturer, 'Physics', 5)
best_student_2.rate_hw(best_lecturer, 'GIT', 5)
print(best_lecturer.grades)

# Rate lecturer 2 by 2 studets
best_student.rate_hw(best_lecturer_2, 'Physics', 10)
best_student.rate_hw(best_lecturer_2, 'GIT', 9)
best_student_2.rate_hw(best_lecturer_2, 'Physics', 9)
best_student_2.rate_hw(best_lecturer_2, 'GIT', 9)
print(best_lecturer_2.grades)

# Check changed print func behaviour
print(best_student)
print(cool_reviewer)
print(best_lecturer.grades)
print(best_lecturer)

# Compare students on average scores
best_student < best_student_2
best_student > best_student_2
best_student == best_student_2
best_student != best_student_2


# Course mean rating function
def mean_course_score(student_list, course):
    """Calculate average grade for hw for all students in one cource"""
    scores_list = []
    for student in student_list:
        if course in student.grades:
            scores_list.append(student.grades[course])
    print(f"Средняя оценка за курс {course} = {mean(scores_list)}")
    return mean(scores_list)


student_list = [best_student, best_student_2]
mean_course_score(student_list, 'Python')


# Lectures mean rating function
def mean_lecture_score(lecturers_list, course):
    """Calculate average grade for lectures for all lecturers in one cource"""
    scores_list = []
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            scores_list.append(lecturer.grades[course])
    grades = mean([mean(grades) for grades in scores_list])
    print(f"Средняя оценка за лекции по {course} = {grades}")
    return grades


lecturers_list = [best_lecturer, best_lecturer_2]
mean_lecture_score(lecturers_list, "Physics")
