class Students:
    def __init__(self,name, course, school, Id):
        self.name=name
        self.course=course
        self.school=school
        self.id=Id
    
    def introduce(self):
        print ( f"My name is {self.name}, I go to {self.school}, I do {self.course} and my Id numbr is {self.id}")    

class StudentsRegistry:
    def __init__(self):
        self.students=[]
    def student_add(self,student):
        self.students.append(student)
    def introduce(self):
        for s in self.students:
            s.introduce()


registry=StudentsRegistry()
s1 = Students("Leshan", "1234", "Strathmore", "Computer Science")
s2 = Students("Karanja", "5678", "USIU", "Math")
s3 = Students("Frida", "9999", "JKUAT", "HR")

with open("students.txt" , "w") as file:
    for s in registry.students:
        file.write (f"{s.name}, {s.course},{s.id}, {s.school} \n")
        
        
with open("students.txt" ,"r") as file:
    for line in file:
        print(line.strip())
