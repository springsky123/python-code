#PYRAMID PATTERN

def print_pyramid(rows):
    for i in range(1,rows+1):
        print(' '*(rows-i),end='')
        print('* '*i)
row = int(input('Enter rows:'))
print_pyramid(row)
