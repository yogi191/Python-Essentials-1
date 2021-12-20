y=int(input("Enter the year: "))
if y<1582:
    print("Not within the georgian calendar")
elif y%4!=0:
    print("Common year")
elif y%100 !=0:
    print("Leap year")
elif y%400 !=0:
    print("Common year")
else:
    print("Leap year")
