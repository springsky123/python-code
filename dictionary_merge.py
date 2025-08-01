#Wap to merge two dictionary if they having some common keys then add their values

d1 = {'1':200,'2':300,'4':500}
d2 = {'1':100,'3':200,'2':300}
d3 = dict(d1)
d3.update(d2)
for i,j in d1.items():
    for x,y in d2.items():
        if i==x:
            d3[i]=(j+y)
print('Orignal dictionaries:')
print('1.',d1)
print('2.',d2)
print("The resultant dictionary:")
print(d3)
