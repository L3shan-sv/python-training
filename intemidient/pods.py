import json
class ulinziEstate:
    def __init__(self, court , phase, number, owner):
        self.court=court
        self.phase=phase
        self.number=number
        self.owner=owner
    
    def introduce(self):
        print(f" The house is in court {self.court} phase {self.phase} number {self.number } and belongs to {self.owner}")
        
    def to_dict(self):
        return{
            "court":self.court,
            "phase":self.phase,
            "number":self.number,
            "owner":self.owner
                
        }
    @staticmethod
    def from_dict(data):
        return ulinziEstate(
            data["court"],
            data["phase"],
            data["number"],
            data["owner"],
        )    
        
        
class HouseRegistry:
    def __init__(self):
        self.houses=[]
    def house_add(self,house):
        self.houses.append(house)
    def house_list(self):
        for h in self.houses:
            h.introduce()
            
    def save_to_json(self, filename= "houses.json"):
        data =[h.to_dict() for h in self.houses]
        with open(filename,"w")as file:
            json.dump(data,file, indent=4)
    
    def load_from_json(self,filename ="houses.json"):
        with open(filename,"r")as file:
            data=json.load(file)
        self.houses = [ulinziEstate.from_dict(item) for item in data]     
       
                    
 
registry=HouseRegistry()

h1=ulinziEstate("Ulinzi Court" , "Phase3", "45" ,"karanja")             
               
registry.house_add(h1)       
registry.save_to_json()
 
new_registry=HouseRegistry()
new_registry.load_from_json()

new_registry.house_list()



        