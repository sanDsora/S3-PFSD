class Student:
    count=0
    def __init__(self):
        Student.count=Student.count+1
s1=Student()
s2=Student()
s3=Student()
print("Number of objects are:", Student.count)