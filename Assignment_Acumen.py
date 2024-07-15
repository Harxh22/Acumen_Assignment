"""
Inheritance and Polymorphism:
Create a base class Vehicle with a method start_engine that prints "Engine started."
Create a derived class Car that inherits from Vehicle and overrides the start_engine method to print "Car engine started."
Create another derived class Bike that inherits from Vehicle and overrides the start_engine method to print "Bike engine started."
Global Variable:
Define a global variable traffic_light with the value "Green".
Module Variable:
Define a module-level variable speed_limit with the value 60.
Object Variable:
In the Car class, define an object variable make that stores the make of the car.
In the Bike class, define an object variable type that stores the type of bike.
Local Variable:
In each start_engine method, define a local variable message that stores the respective message to be printed.
"""

traffic_light="RED"

class Vehicle:
    
    global traffic_light 
    traffic_light="GREEN";
    speed_limit = 60;

    def __init__(self):
        pass

    def start_engine(self):
        print("Engine Started")

class Car(Vehicle):

    def __init__(self,fuel_type,color):
        self.fuel_type = fuel_type
        self.color = color        

    def start_engine(self):
        print("Car Engine Started")
    
    def car_make(self):
        print("Car Takes "+self.fuel_type+" And Has A "+self.color+" color finish.")

class Bike(Vehicle):

    def __init__(self,types,mileage):
        self.types = types
        self.mileage = mileage
    
    def start_engine(self):
        print("Bike Engine Started")
    
    def bike_type(self):
        print("Bike Is Of "+self.types+" Type And Has A Mileage Of "+self.mileage)
    
#Global Variable Showcase
print("The Signal Is: "+traffic_light)

#Classes And Objects Usage
vehicle= Vehicle();
print("The Official Speed Limit On Highways Is "+str(vehicle.speed_limit)) #Modular Variable Showcase

car= Car("Diesel","Black")
car.car_make()  

bike= Bike("Sports","6")
bike.bike_type()

#Polymorphism Showcase
for x in (vehicle,car,bike):
    x.start_engine()





