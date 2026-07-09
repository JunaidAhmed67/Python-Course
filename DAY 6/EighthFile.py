class Student:
    def __init__(self,name,marks):
        self.name =  name 
        self.marks = marks
    def welcome(self):
        print("Welcome :",self.name )
    def marks_std(self):
        return self.marks

s1 = Student("Hussain", 99)
print(s1.name,s1.marks)
print(s1.marks_std())


class Student:
    def __init__(self,name ,marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        marks = self.marks
        for mark in marks:
            sum +=mark
        avg = sum/(len(marks))
        return avg
    @staticmethod
    def hello():
        print("hello world!")
    


marks = []
for i in range(3):

    get_marks = int(input("Enter your mark of subject "+str(i+1)+" : "))

    marks.append(get_marks)
s1 = Student("ALi",marks)

print("Name: ",s1.name," Average of marks: ",s1.avg()  )
Student.hello()    

