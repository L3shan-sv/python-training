import json

class AutoCars:
    def __init__(self, yard, price, make):
        self.yard=yard
        self.price=price
        self.make=make
    
    def introduce(self):
        print(f"The car is in the {self.yard}, it goes for {self.proce} and its make is {self.make}")
    
    def to_dict(self):
        return{
            "yard":self.yard,
            "price":self.price,
            "make":self.make,
        }    
        
@staticmethod
def from_dict(data):
    return AutoCars(
        data["yard"],
        data["price"],
        data["make"]
    )

class CarRegistry:
    def __init__(self):
        self.cars=[]
    def car_add(self,car):
        self.cars.append(car)
    def car_list(self):
        for c in  self.cars:
            c.introduce()
    
    def save_to_json(self, filename ="cars.json"):
        data =[c.to_dict() for c in self.houses ]
        with open(filename, "w")as file:
            json.dump(data,file, indent=4)
            
    def load_from_json(self, filename="cars.json"):
        with open(filename, "r")as file:
            data=json.load(file)
            self.cars =[AutoCars.from_dict(item) for item in data ]
            
registry=CarRegistry()
c1=AutoCars("Mombasa Yard", "ten million" "aston martin DBX")

registry.car_add(c1)
registry.save_to_json

new_registry=CarRegistry()
new_registry.load_from_json

new_registry.car_list()



                
            
                
            
        
            
    