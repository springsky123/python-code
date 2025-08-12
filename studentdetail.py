#wap to write student details to a binary file

import pickle

#fuction to create binary file
def create_file():
    try:
        file = open('student.dat','w')
        file.close()
    except FileExistsError:
        pass #because the file already exists


#funtion to write the data
def write_data():
    print("Please enter student details..........")
    name = input("Enter student name:")
    cls = input("Enter student class:")
    age = int(input("Enter student age:"))
    address = input("Enter student address:")
    marks  = int(input("Enter students marks:"))
    data = [{'Name':name,
            'Class':cls,
            'Age':age,
            'Address':address,
            'Marks':marks}]
    print()
    #storing the above data in the binary file
    fh = open("student.dat",'ab')
    pickle.dump(data,fh)
    print('Student Data inserted')
    fh.close()


#function to read and display the data
def read_data():
    try:
        with open("student.dat",'rb') as binary_file:
            x = pickle.load(binary_file)
            print(x)
    except:
        print("No contents found in the file...")
     



#functions to choose your choice
def options():
    print('......................................')
    print('1.ADD STUDENT DETAILS')
    print('2.SHOW STUDENT DETAILS')
    print('.......................................')
    option = int(input('enter your choice:'))
    return option

#funtion to handle the entireprogram
def main():
    #create_file()           #once your file created you remove this statement
    choice ='y'
    while choice=='y':
        opt = options()
        if opt==1:
            write_data()
        elif opt==2:
            read_data()
        else:
            print('......invaild choice,please try again!..........')
        print()    
        choice = input('>Do you want to continue?(type*y*for yes):')

    print("\n***THE PROGRAM CLOSES HERE***\n")



#Calling the mainfunction
main()
