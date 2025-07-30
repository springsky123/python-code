#STUDENT RECORD

import csv

#create a csv file
def create():
    file = open('record.csv','w')
    file.close()
#create()       #once your file created you remove this statement

    
#funtion to load student record 
def addrecord():
    print('...........................................')
    print("Please enter student details..........")
    name = input("Enter student name:")
    cls = input("Enter student class:")
    age = int(input("Enter student age:"))
    address = input("Enter student address:")
    data = [{'Name':name,
            'Class':cls,
            'Age':age,
            'Address':address}]
    #storing the above data in the csv file
    file = open('record.csv','a')
    writer = csv.writer(file)
    writer.writerow(data)
    print(">>>Student record added successfully")
    file.close()
#fuction to show the student detail
def showrecord():
    try:
        file = open('record.csv','r')
        read = csv.reader(file)
        for row in read:
            if row==[]:
                pass
            else:
                print(row)
    except:
        print("No contents found in the file...")
#function for options to choose 
def options():
    print('......................................')
    print('1.ADD STUDENT RECORD')
    print('2.SHOW STUDENT RECORD')
    print('.......................................')
    option = int(input('enter your choice:'))
    return option
#funtion to handle the entireprogram
def main():
    choice ='y'
    while choice=='y':
        opt = options()
        if opt==1:
            addrecord()
        elif opt==2:
            showrecord()
        else:
            print('......invaild choice,please try again!..........')
        print()    
        choice = input('>Do you want to continue?(type*y*for yes):')

    print("\n***THE PROGRAM CLOSES HERE***\n")

#calling the mainfuction
main()

    
    
