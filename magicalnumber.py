#MAGICAL NUMBER


def magic_number(n):
    while n>=10:
        sum_of_digits = 0
        while n>0:
            sum_of_digits += n%10
            n//=10
        n = sum_of_digits
    return n==1
#main
num = int(input("Enter number:"))            
if magic_number(num):
    print(num,"is a magic number.")
else:
    print(num,"is not a magic number.")
