#MANAGE CLASSES OF SCHOOL

import csv
class school_class:
    def __init__(self):
        sel.school_name = "SUNRISE CONVENT SCHOOL"
    #function for add classes
    def addclasses(self):
        cls = input("Enter class name:")
        file = open('classes.csv','a')
        writer = csv.writer(file)
        writer.writerow([cls,self.school_name])
        print("Class added successfully..")
        file.close()
    #function for show classes
    def showclasses(self):
        file = open("classes.csv",'r')
        read = csv.reader(file)
        next(read)
        print(['CLASS','SCHOOL_NAME'])
        for row in read:
            if row==[]:
                pass
            else:
                print(row)
        file.close()
    #function for options to choose 
    def options(self):
        print('......................................')
        print('1.ADD CLASSES')
        print('2.SHOW CLASSES')
        print('.......................................')
        option = int(input('enter your choice:'))
        return option
    #funtion to handle the entireprogram
    def main(self):
        choice ='y'
        while choice=='y':
            opt = self.options()
            if opt==1:
                self.addclasses()
            elif opt==2:
                self.showclasses()
            else:
                print('......invaild choice,please try again!..........')
            print()    
            choice = input('>Do you want to continue?(type*y*for yes):')

        print("\n***THE PROGRAM CLOSES HERE***\n")
#Create object of school_class
st = school_class()





        
        

