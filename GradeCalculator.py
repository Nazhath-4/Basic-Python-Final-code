# Creating Manu
f = open('base.txt', 'a+')
read_base = open('base.txt', 'r')
backno ='No'
backyes ='yes'
interface = True


def user_input(name):
   if  menu == 1:
        f.write(name + '\n')

while interface:
    print('1. Add a name to the base \n2.Delete a name from the base\n3.Get name from the base \n4.Edit a name \n5.Exit')
    menu = int(input('input an option : '))
    if menu ==1:
        user_input(name=input('type a name :'))
        name_added()
    elif menu == 2:
        print('\nOption 2 executed')
    elif menu == 3:
        print('\nOption 3 executed')
    elif menu == 4:
        print('\nOption 4 executed')
    elif menu > 4:
        print('program closed')
        interface = False

import re
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        self.Grade = {}

    def calculate_grades(self):
        for subject in self.marks():
            if marks >=90:
                self.Grade[subject] = 'A'
            elif marks >=80:
                self.Grade[subject] = 'B'
                if marks >= 70:
                    self.Grade[subject] = 'C'
                elif marks >= 60:
                    self.Grade[subject] = 'D'
                elif marks >= 50:
                    self.Grade[subject] = 'E'
                else:
                    self.Grade[subject] = 'Fail'


class GradeCalculator:
    def __init__(self):
        self.students = []
    def add_student(self,name,marks):
        self.students.append(Student(name,marks))
    def calculate_grades(self):
        for student in self.students:
            student.calculate_grades()
    def print_grades(self):
        for student in self.students:
            print(student.name)
            for subject,grade in student.Grade.items():
                print(subject,grade)




