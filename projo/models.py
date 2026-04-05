import json

class Students:
    def __init__(self, name , course, id):
        self.name=name
        self.course=course
        self.id=id
    
    def to_dict(self):
        return{
            "name":self.name,
            "course":self.course,
            "id":self.id
        }
    @staticmethod
    def from_dict(data):
        return Students( 
            data["name"],
            data["course"]
            data["id"]
            
        )

class StudentRegistry:
    def __init__(self, filename= "students.json"):
        self.filename=filename
        self.students=[]
        self.load=()
        
    def student_add(self,student):
        self.students.append(student)
        self.save()
    def student_list(self):
        return [s.to_dict() for s in self.students]
    
    def  student_get(self,name):
        for s in self.students:
            if self.name==name:
                return s
            return None
    def student_delete(self, name):
        service= self.student_get
        if service:
            self.services.remove(service)
            self.save()
    
    def save(self):
        data=[s.to_dict() for s in self.students]
        with open (self.filename, "w" )as f:
            json.dump(data, f, indent=4)
    
    def load(self):
        try:
            with open(self.filename, "r")as f:
                data =json.load(f)
                self.students= [Students.from_dict(d) for d in data]
            except FileNotFoundError:
                self.students=[]
                
            
                
            
        
        
                   
        
    
        