x=float(input("Enter your  income: "))
if x<=85528:
    tax=(0.18*x)-556.2
    print("This is your", tax, "amount to be paid")
elif x>=85528:
    tax=14839+(0.32*(x-85528))
    print("This is your", tax, "amount to be paid")
elif tax<0:
    print("The government does not return any tax")
