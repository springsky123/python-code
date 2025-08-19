#STUDENT ATTENDENCE MANAGEMENT  SYSTEM
#REGISTRATION OR LOGIN FUNCTIONS

import csv
import getpass

class Registration:
    def registration(self):
        name = input("Enter your name:")
        Id = self.checkid()
        password = self.checkpasswd()
        data = [name,Id,password]
        file = open('registrated.csv','a',newline = '')
        writer = csv.writer(file)
        writer.writerow(data)
        print("Registration completed..")
        file.close()
    def checkid(self):
        Id = input("Enter your id:")
        if len(Id)>=8: 
            with open('registrated.csv','r')as file:
                read = csv.reader(file)
                next(read)
                for row in read:
                    if row==[]:
                        pass
                    else:
                        if row[1]==Id:
                            print("This id is already registered!!..please try again...")
                            self.checkid()
                else:
                    return Id
        else:
            print("Invaild Id!!!..please try again...")
            self.checkid()
    def checkpasswd(self):
        passwd = getpass.getpass("Enter your password:")
        if len(passwd)>=8:
            return passwd
        else:
            print("Password must be at least 8 characters long........")
            self.checkpasswd()
class Login:
    def log_in(self):
        Id = input("Enter your id:")
        checkuser = self.log_usercheck(Id)
        if checkuser==True:
            self.log_checkpassword(Id)
    def log_usercheck(self,Id):
        if len(Id)>=8:
            with open('registrated.csv','r')as file:
                read = csv.reader(file)
                next(read)
                for row in read:
                    if row==[]:
                        pass
                    else:
                        if row[1]==Id:
                            return True
                else:
                    print("Invaild id!! please try again....")
                    self.log_in()
        else:
            print("Invaild id!! please try again....")
            self.log_in()
    def log_checkpassword(self,Id):
        Id2 = Id
        passwd = getpass.getpass("Enter your password:")
        if len(passwd)>=8:
            with open("registrated.csv",'r')as file:
                read = csv.reader(file)
                next(read)
                for row in read:
                    if row==[]:
                        pass
                    else:
                        if row[1]==Id:
                            if row[2]==passwd:
                                print("Login successfully")
                            else:
                                print("Wrong password...try again")
                                self.log_checkpassword(Id2)
                                
                        else:
                            pass
        else:
            print("Wrong password...try again")
            self.log_checkpassword(Id2)
#function for options to choose 
def options():
    print('......................................')
    print('1.FOR REGISTRATION')
    print('2.FOR LOGIN')
    print('.......................................')
    option = int(input('enter your choice:'))
    return option
#funtion to handle the entireprogram
def main():
    choice ='y'
    while choice=='y':
        opt = options()
        if opt==1:
            s = Registration()
            s.registration()
        elif opt==2:
            s2 = Login()
            s2.log_in()
        else:
            print('......invaild choice,please try again!..........')
        print()    
        choice = input('>Do you want to continue?(type*y*for yes):')

    print("\n***THE PROGRAM CLOSES HERE***\n")

#calling the mainfuction
main()

    
    

