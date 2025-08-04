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
