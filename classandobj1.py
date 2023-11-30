#Class and object creation
#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
V1=Vehicle(100,40)
print(V1.max_speed,V1.mileage)