#wap to print all prime numbers between 1 to n 
n = int(input('enter range:'))
if n==0 or n==1:
    print('invalid choice,try again')
else:
    print('All the prime numbers in this range are:')
    for i in range(2,n+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c<=2:
            print(i,end=',')
print()

