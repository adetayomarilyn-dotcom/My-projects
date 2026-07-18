class BMW():
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed
class Ferrari():
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed
obj1 = BMW("Petrol", 250)
obj2 = Ferrari("Diesel", 300)
print(obj1.max_speed)
print(obj2.max_speed)
print(obj1.fuel_type)
print(obj2.fuel_type)
