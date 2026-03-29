rows = (int(input("Enter a number")))
for i in range(1, rows+1):
    spaces = " " * (rows-i)
    stars = "*" * i
    print(spaces + stars)