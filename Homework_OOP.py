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

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self.grades}\n Курсы в процессе изучения: {self.courses_in_progress}\n Завершенные курсы: {self.finished_courses}"
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        
class Lecturer(Mentor):
    pass

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
            return f" Reviewer - {self.name} {self.surname}"


# Create students and their sets of courses
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['SQL'] 
best_student.courses_in_progress += ['Advanced Python']
best_student.finished_courses += ['Physics']
best_student.finished_courses += ['GIT']
print(best_student.courses_in_progress)
print(best_student.finished_courses)

# Create a reviewers and their courses and ratings
cool_reviewer = Reviewer('Ivan', 'Mulin')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['SQL']
cool_reviewer.courses_attached += ['Advanced Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'SQL', 5)
print(cool_reviewer.courses_attached)
print(best_student.grades)

# Create a lecturer and her courses and thier raiting
best_lecturer = Lecturer('Albert', 'Einstein')
best_lecturer.courses_attached += ['Physics']
best_student.rate_hw(best_lecturer, 'Physics', 10)
print(best_lecturer.courses_attached)
print(best_lecturer.grades)

# Change pring func behaviour