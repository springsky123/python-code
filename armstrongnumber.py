#ARMSTRONG NUMBER


#function for check a number is armstrong or not
def check_armstrong(num):
    for i in range(1,num):
        sum1 = 0
        num_str = str(i)
        num_digit = len(num_str)
        temp = i
        while temp >0:
            digit = temp%10
            sum1+=digit**num_digit
            temp//=10
        if sum1 == i:
            print(i,"is an armstrong number.")
        else:
            pass
# main
num = int(input("Enter range:"))
print()
check_armstrong(num)
