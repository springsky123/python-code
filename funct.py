# wap to store string character in dictionary
def main():
    st = input('enter string:')
    k =[]
    val =[]
    d = {}
    for i in st:
        c = 0
        for j in st:
            if i==j:
                c+=1
        d[i]=c
    print('new dictionary created by string character:')
    print(d)
main()
print()


#wap to sum the values of dictionary
dic = {'hi':32,'hs':56}
print('dictionary:',dic)
def sum_value(d):
    l = tuple(d.values())
    c=0
    for i in l:
        c+=i
    print('sum of dictionary values :',c)
sum_value(dic)
print()

    
#wap to merge two dictionary
def merge():
    d1 = {'name':'bhawana','age':17}
    d2 = {'village':'raikhet'}
    print('orignal dictionaries:')
    print('1.',d1)
    print('2.',d2)
    d1.update(d2)
    return(d1)
print('merge/new dictionary:',merge())
print()


# wap to swap dictionary
dic = {1:1,2:8,3:9}
print('original dictionary:',dic)
item = tuple(dic.items())
new ={}
def swap(d):
    k = tuple(d.keys())
    v = tuple(d.values())
    d ={}

for i in item:
    k,v = i
    new[v]=k
print('new dictionary by swaping key and value :')
print(new)
    


