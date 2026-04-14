try:
    bill_amount = float(input("Enter total bill amount"))
    paid_amount = float(input("Enter the amount paid"))
    due_amount = bill_amount - paid_amount
    if due_amount > 0:
        print("Costumer owes", due_amount)
    elif due_amount < 0:
        print("Costumer should get back",due_amount)
    else:
        print("Bill fully paid, no money left due")
except ValueError:
    print("Invalid input! please enter numbers only.")
