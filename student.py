import random

class Student:
    def __init__(self, name):
        self.name = name # general attribute #
        self.marks = [] # list to store marks #

    def add_marks(self, mark): # write somthinge after self which you are going to use#
        self.marks.append(mark) 
    
    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0
    
names = ["Alice", "Bob", "Charlie"] 

students =[Student(name) for name in names] #oblect of class Student in list comprehension#

for student in students:# iterating through list of objects#
    for _ in range(5): #non variable loop#
        student.add_marks(random.randint(0, 100))
        print(f"{student.name}'s average mark: {student.average()}")   
    

