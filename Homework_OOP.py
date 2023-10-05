class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
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

    
# Task 1. Create basic objects to check code

mentor_1 = Mentor('Andrei', 'Pshenichnyi')
print(mentor_1.name)

lecturer_1 = Lecturer('Vasya', 'Ivanov')
print(lecturer_1.name)

Reviewer_1 = Reviewer('Oleg', 'Petrov')
print(Reviewer_1.name)


# Task 2.1 Check behaviour of reviewer calss

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Ivan', 'Mulin')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)