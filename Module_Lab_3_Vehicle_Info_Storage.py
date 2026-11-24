#Geovanny Sanchez
#Module_Lab_3_Vehicle_Info_Storage.py
# Use classes and inheritance to store
#and display automobile info

#Superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


#Subclass for Automobile
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year 
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#User input and store info
print("Enter Vehicle information")

year = input("Enter year: ")
make = input("Enter make: ")
model = input("Enter model: ")
doors = input("Enter # of doors(2 or 4): ")
roof = input("Enter roof type(solid or sun roof): ")

#Creates Automobile object
car = Automobile(year, make, model, doors, roof)

#Display information results
print("\nVehicle Information")
print("-------------------")
print("Vehicle type", car.vehicle_type)
print("Year", car.year)
print("Make", car.make)
print("Model", car.model)
print("Number of doors:", car.doors)
print("Type of roof:", car.roof)
