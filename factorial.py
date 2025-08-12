#WAP for a recursive factorial function and print timetaken by program

import time
start = time.time()

#Function for factorial

def factorial(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        return -1
    else:
        return n*factorial(n-1)
#main
number = int(input("Enter number:"))
result = factorial(number)
if result==-1:
    print("factorial does not exist negative number..")
else:
    print("Factorial of",number,"is",result)
end = time.time()
t = end-start
print("Total time taken:",t)


