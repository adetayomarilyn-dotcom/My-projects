start = int(input("Enter the start number"))
end = int(input("Enter the end number"))

squares = []
even = []
odd = []

for i in range(start, end + 1):
    sq = i * i
    squares.append(sq)

    if sq % 2 == 0:
        even.append(sq)
    else:
        odd.append(sq)
print(squares)
print(even)
print(odd)