for i in range(0,101,10):
    print(i)

i=0
while i<=100:
    print(i)
    i=i+10
    if i==60:
        break
print("The end")


i=0
while i<=100:
    print(i)
    i=i+10
    if i==60:
        continue
print("The end")


n=int(input("Enter any number: "))
print("the factors of",n,"are:")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=", ")
