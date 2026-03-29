from flask import Flask, jsonify, request
app = Flask(__name__)

class Grade8:
    def __init__(self, name, id , contact):
        self.name=name
        self.id=id
        self.contact=contact
        
    def introduce(self):
        print(f" This is {self.name} their id number is {self.id} their emergency contact info is  {self.contact}")
    
    def to_dict(self):
        return{
            "name":self.name,
            "id":self.id,
            "contact":self.contact
 
        }
        
        
class StudentRegistry:
    def __init__(self):
        self.students=[]
        
    def student_add(self,student):
        self.students.append(student)
    def student_list(self):
        for s in self.students:
            return[s.to_dict() for s in self.students]

registry=StudentRegistry()

@app.route("/")
def home():
    return"server active"            
            
@app.route("/students", methods=["GET"])        
def get_students():
    return jsonify(registry.student_list())

@app.route("/students", methods=["POST"])
def student_add():
    data=request.json
    
    student=Grade8(
        data["name"],
        data["id"],
        data["contact"],
    )
    
    registry.student_add(student)
    return{"message" : "Student Succesfully added"}
    
if __name__=="__main__":
    app.run(debug=True)
    

        
                