# diamond pattern
def print_diamond(rows):
    for i in range(1,rows+1):
        print(' '*(rows-i),end='')
        print('* '*i)
    for j in range(rows-1,0,-1):
        print(' '*(rows-j),end='')
        print('* '*j)
num_row = int(input('enter numbers of row:'))
print_diamond(num_row)
