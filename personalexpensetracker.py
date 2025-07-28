#PERSONAL EXPENSE TRACKER

import csv

#create a csv file locally
csv_file = 'expenses.csv'

#fuction to start the file/initialize csv
def initializeCSV():
    try:
        file = open(csv_file,'w')
        writer = csv.writer(file)
        writer.writerow(['Date','Categary','Description','Amount'])
        file.close()
    except FileExistsError:
        pass #no initialization because file already exists

#function to record the expenses
def recordExpenses():
    print('..............................')
    inp_date = input('Enter date:')
    inp_categary = input('Enter the categary:')
    inp_des = input('Enter the description:')
    inp_amt= float(input('Enter the amout:'))
    print('................................')
    #storing the above data in the csv file
    file = open(csv_file,'a')
    writer = csv.writer(file)
    writer.writerow([inp_date,inp_categary,inp_des,inp_amt])
    print(">>>Expense added successfully")
    file.close()

#fuction to show the expenses
def showExpenses():
    try:
        file = open(csv_file,'r')
        read = csv.reader(file)
        next(read)
        for row in read:
            if row==[]:
                pass
            else:
                print(row)
    except:
        print("No contents found in the file...")
        
#main functions to handle the program
def options():
    print('......................................')
    print('1.ADD EXPENSE')
    print('2.SHOW EXPENSE')
    print('.......................................')
    option = int(input('enter your choice:'))
    return option
#funtion to handle the entireprogram
def main():
    initializeCSV()   #when your file created you remove this statement
    choice ='y'
    while choice=='y':
        opt = options()
        if opt==1:
            recordExpenses()
        elif opt==2:
            showExpenses()
        else:
            print('......invaild choice,please try again!..........')
        print()    
        choice = input('>Do you want to continue?(type*y*for yes):')

    print("\n***THE PROGRAM CLOSES HERE***\n")

#calling the mainfuction
main()
