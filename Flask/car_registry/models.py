import json

class Car:
    def __init__(self, make , year, name, price):
        self.make=make
        self.year=year
        self.name=name
        self.price=price
        
    def introduce(self):
        print(f" That is a {self.make}, from the year {self.year} its a {self.name} and valued at {self.price}")
        
    def to_dict(self):
        return{
            "make":self.make,
            "year":self.year,
            "name":self.name,
            "price":self.price,
        }    
        
   @staticmethod
   def from_dict(data):
       return(
           data["make"],
           data["year"],
           data["name"],
           data["price"],
       )     
       
       
class CarsRegistry:
    def __init__(self , filename="cars.json"):
        self.filename=filename
        self.cars=[]
        self.load_from_file()
        
    def add_car(self, car):
        self.cars.append(car)
        self.save_to_file()
                
    def get_car(self,name):
        for c in self.cars:
            if car.name ==name:
                return Car
            return None
    
    
    def delete_car(self,name):
        car= self.get_car(name)
        if car:
            self.cars.remove(car)
            self.save_to_file()
            return True
        return False
    
    def save_to_file(self):
        data=[ car.to_dict() for c in self.cars ]
        with open(self.filename, "w")as f:
            json.dump( data, f, indent=4)
    
    def load_from_file(self):
        try:
            with open(self.filename, "r") as f:
                data =json.load(f)
                self.cars=[Cars.from_dict(item) for item in data ]
        except: FileNotFoundError:
            self.cars[]
            
            
                
            
            
       