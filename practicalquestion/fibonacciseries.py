#wap to fibonacci series

class fibonacci:
    def __init__(self,num):
        self.rangenum = num
    def fibo_of_num(self):
        a =0
        b = 1
        print(a,end=',')
        print(b,end=',')
        for i in range(n-2):
            c = a+b
            print(c,end=',')
            a = b
            b = c
        print()
n = int(input('Enter range:'))
# create object of fibonacci
o1 = fibonacci(n)
o1.fibo_of_num()

