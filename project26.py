class Vehicle:
  
    def __init__(self, seating_capacity):
      
        self.seating_capacity = seating_capacity

    def fare(self):
      
        return self.seating_capacity * 100


class Bus(Vehicle):
  
    def fare(self):
      
        base_fare = super().fare()
      
        total_fare = base_fare * 1.10
        return total_fare

try:
    capacity_input = int(input("Enter the seating capacity of the bus: "))
    my_bus = Bus(capacity_input)
    print(f"The total fare for the bus is: £{my_bus.fare():.2f}")
  
except ValueError:
  print("Please enter a valid integer for the seating capacity.")
