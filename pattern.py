#wap to create patterns
n = int(input('enter range:'))
for i in range(1,n+1):
    print('*'*i)
# second
x = int(input('enter range:'))
for i in range(x,0,-1):
    print('*'*i)
# third
y = int(input('enter range:'))
for i in range(1,y):
    for j in range(1,i+1):
        print(j,end='')
    print()
# fourth
z = int(input('enter range:'))
for i in range(z):
    for j in range(z,i,-1):
        print(j,end='')
    print()
