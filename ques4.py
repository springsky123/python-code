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
