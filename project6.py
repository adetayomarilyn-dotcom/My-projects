rows = (int(input("Give me a number")))
for i in range(1, rows+1):
    spaces = " " * (rows-i)
    stars = "*" * i
    print(spaces + stars)