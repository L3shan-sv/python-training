class Cars:
    def __init__(self, name, make, year, developer):
        self.name=name
        self.make=make
        self.year=year
        self.developer=developer
    
    def inventory(self):
        for c in Cars:
            print(f"In our inventoer we have a {self.name} by {self.developer}, from the year {self.year} the spec is {self.make}")
        
        
class InventoryRegistry:
    def init(self,cars):
        self.Cars=[]
    
    def cars_add(self):
        self.cars.append(self.Cars)
    def introduce(cars):
        for c in Cars:
           c.introduce()
           
registry=InventoryRegistry()
c1= Cars("Maserati", "2013", "DBX" "Ford")

with open("Cars.txt", "w") as file:
    for c in registry.cars:
        file.write(f"{c.name}", "{c.make}", "{c.developer}", "{c.year}")
        
with open ("Cars.txt", "r") as file:
    for line in file:
        print (line.strip())
        
        
    
               