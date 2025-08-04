# Calculate the sum of digits of a number (by a recursive function or simple function)

  #by simple function
def sum_digit_simple(number):
    totalsum = 0
    #Handle negative numbers by taking the absolute value
    number = abs(number)
    while number>0:
        digit = number%10
        totalsum+=digit
        number//=10
    return totalsum
  #by recursive function
def sum_digit_recursive(number):
    totalsum = 0
    #Handle negative numbers by taking the absolute value
    number = abs(number)
    if number == 0:
        return 0
    else:
        return (number%10) + sum_digit_recursive(number//10)
  #main
num = int(input("Enter number:"))
print("The sum of the digits of this number is (by simple funtion)",sum_digit_simple(num))
print("The sum of the digits of this number is (by recursive funtion)",sum_digit_recursive(num))


#WAP to read studend data from a csv file and display names of students who scored above 90

import csv


  #function to print the student name
def studentmark():
    try:
        file = open('record.csv','r')
        read = csv.reader(file)
        next(read)
        for row in read:
            if row==[]:
                pass
            else:
                if int(row[4])>90:
                    print(row[0])
                else:
                    pass
    except:
        print("No contents found in the file...")
print("Names of students whose marks are above 90:")
studentmark()


#WAP to take a list of numbers and return a new list containing only prime numbers


     # make a function to check prime number
def check_prime(n):
    c = 0
    for j in range(1,n+1):
        if n%j==0:
            c+=1
    if c==2:
        return True
    else:
        return False
     #main
lst = [11,1,0,2,12,3,45,817,910,277,4,7,287,97]
newlist = []
print('New list(contain only prime number):')
for i in lst:
    if check_prime(i)==True:
        newlist.append(i)
    else:
        pass
print(newlist)
 
