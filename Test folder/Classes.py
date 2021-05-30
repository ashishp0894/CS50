"""class point(): #Create a new class of type point
    def __init__(self,x_coord,y_coord): #initialize values of class
        self.x = x_coord
        self.y = y_coord

p = point(10,20)
q = point (30,22)
print(f"{p.x},{p.y} ")
"""

class flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger (self,Passenger_name): #New function created inside class
        if not self.open_seats():
            return False
        else:
            self.passengers.append(Passenger_name)
            return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

f90 = flight(3)
people = ["Harry","Ron","Hermoine","Ginnie"]

for person in people:
    success = f90.add_passenger("person")
    if success:
        print(f"Added {person} successfully")
    else:
        print(f"Unable to add {person} successfully")
