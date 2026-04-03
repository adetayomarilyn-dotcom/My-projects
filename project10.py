def calculate_circumference(radius):
    circumference = 2 * 3.14 * radius
    return circumference
radius = int(input("Enter a number"))
result = calculate_circumference(radius)
print(f"The circumference is: {result}")