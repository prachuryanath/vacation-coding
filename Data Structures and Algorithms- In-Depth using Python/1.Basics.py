# While loop
for ch in 'Hello':
    print(ch)

x = range(10,-9,-2)
print(x)

for i in x:
    print(i)

# Continue
l = [10,54,2,61,15]

for i in l:
    if i % 2 != 0:
        continue
    print(i)        # To find even numbers

# Class
class Student:
    '''This is a class method'''
    college = 'IIT'
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks  
        # Student.college = 'IIT'
    def __str__(self):
        return "Name: {}, Roll: {}, Marks: {}".format(self.name, self.roll, self.marks)

    def display(self):
        print('Student name:', self.name)
        print('Student roll:', self.roll)
        print('Student marks:', self.marks)
        print('College:', self.college)

S1 = Student('a',22,96)
S2 = Student('b',21,80)
print(S1.__str__)
print(S1.__doc__)
print(S1)
print(S1.name)
print(S1.roll)
print(S1.marks)
S2.display()