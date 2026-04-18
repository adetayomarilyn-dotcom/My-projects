import math

angle = float(input("Enter angle in degrees"))

radians = math.radians(angle)

sin_val = math.sin(radians)
cos_val = math.cos(radians)
tan_val = math.tan(radians)

print("sin:", sin_val)

print("cos:", cos_val)

print("tan:", tan_val)