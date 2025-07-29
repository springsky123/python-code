#wap to check ang string is palindrome or not
st = input('enter string:')
rev = ''
for i in range(-1,(-len(st)-1),-1):
    rev+=st[i]
if rev==st:
    print('string is a palindrome')
else:
    print('string is not a palindrome')
