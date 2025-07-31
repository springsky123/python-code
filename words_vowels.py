#WAP to count the words who start with a vowel

line = input("Enter lines(string):")
c = 0
vowel = ['a','A','e','E','i','I','o','O','u','U']
words = line.split()
for i in words:
    if i[0] in vowel:
        c+=1
    else:
        pass
print("The number of words who start with a vowel:",c)
