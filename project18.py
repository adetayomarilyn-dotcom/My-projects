dictionary_y = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

key = input("Enter the key you want to check for duplicates: ")

if key in dictionary_y:
     value = dictionary_y[key]
     counter = 0
     for k, v in dictionary_y.items():
          if v == value:
               counter += 1
     print("Amount of duplicates this value has:", counter)
else:
     print("Key not found in dictionary")