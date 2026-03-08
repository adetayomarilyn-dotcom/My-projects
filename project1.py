letter = (input("Type one character"))

if (letter >= 'a' and letter <= 'z'):
    print("This is a small letter alphabet")
    if (letter >= 'A' and letter <= 'Z'):
        print("This is a big letter alphabet")
    else:
        print("This is not a big letter alphabet")
else:
    print("This is not a small letter alphabet")

