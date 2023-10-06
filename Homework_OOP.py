from statistics import mean

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def mean_score(self):
        return mean(list(self.grades.values()))

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                F"Средняя оценка за домашние задания: {mean(list(self.grades.values()))}\n"
                f"Rурсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                F"Завершенные курсы: {', '.join(self.finished_courses)}"
        )
    
    def __gt__(self, other):
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
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        
class Lecturer(Mentor):
    def __str__(self):
     return (f"Имя: {self.name}\n"
             f"Фамилия: {self.surname}\n"
             F"Средняя оценка за лекции: {mean([mean(i) for i in list(self.grades.values())])}\n"
    )

class Reviewer(Mentor):
        def rate_hw(self, student, course, grade):
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += grade
                else:
                    student.grades[course] = grade
            else:
                return 'Ошибка'
        
        def __str__(self):
            return f"Имя: {self.name}\nФамилия: {self.surname}"


# Create students and their sets of courses
# Student 1
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['SQL'] 
best_student.courses_in_progress += ['Advanced Python']
best_student.finished_courses += ['Physics']
best_student.finished_courses += ['GIT']
print(best_student.courses_in_progress)
print(best_student.finished_courses)

# Student 2
best_student_2 = Student('Andrei', 'Pshenichnyi', 'male')
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['SQL'] 
best_student_2.courses_in_progress += ['Advanced Python']
best_student_2.finished_courses += ['Physics']
best_student_2.finished_courses += ['GIT']
print(best_student_2.courses_in_progress)
print(best_student_2.finished_courses)

# Create a reviewers and their courses and ratings
cool_reviewer = Reviewer('Ivan', 'Mulin')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['SQL']
cool_reviewer.courses_attached += ['Advanced Python']

# Rate first student by reviewer
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'SQL', 5)
print(cool_reviewer.courses_attached)
print(best_student.grades)

# Rate second student by reviewer
cool_reviewer.rate_hw(best_student_2, 'Python', 3)
cool_reviewer.rate_hw(best_student_2, 'SQL', 8)
print(cool_reviewer.courses_attached)
print(best_student_2.grades)

# Create lecturers and their courses and raitings
best_lecturer = Lecturer('Albert', 'Einstein')
best_lecturer.courses_attached += ['Physics']
best_lecturer.courses_attached += ['GIT']

best_lecturer_2 = Lecturer('Isaac', 'Newton')
best_lecturer_2.courses_attached += ['Physics']
best_lecturer_2.courses_attached += ['GIT']

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

# #  Check changed print func behaviour
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
    scores_list = []
    for student in student_list:
        if course in student.grades:
            scores_list.append(student.grades[course])
    print(f"Средняя оценка по курс {course} = {mean(scores_list)}")    
    return mean(scores_list)       

student_list = [best_student, best_student_2]
mean_course_score(student_list, 'Python')

# Lectures mean rating function




