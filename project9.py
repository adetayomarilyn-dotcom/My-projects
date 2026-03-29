num = float(input("Give me a decimal number"))
binary = ""

while num > 0:
    binary = str(num % 2) + binary
    num //= 2
print(binary)