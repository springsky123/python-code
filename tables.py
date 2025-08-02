#tables 
try:
    n = int(input("enter range:"))
    for i in range(1,n+1):
        print("Table of",i,'is:')
        for j in range(1,11):
            print(i,'*',j,'=',i*j)
except ValueError:
    print("Please enter a number....String not allowed")
finally:
    print("End code...")
