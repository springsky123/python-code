#---------STACK DEMONSTRATION---------

class Stack:
    #Constructor(Initializer method)
    def __init__(self):
        self.s = []
    #INSTANCE METHOD FOR CHECKING THE STACK IS EMPTY OR NOT
    def isEmpty(self):
        if len(self.s)==0:
            return True
        else:
            return False
    #INSTANCE METHOD FOR PUSH ITEM IN STACK 
    def push(self,item):
        self.s.append(item)
        top = len(self.s)-1
    #INSTANCE METHOD FOR POP ITEM IN STACK
    def pop(self):
        if self.isEmpty():
            return "Underflow"
        else:
            val = self.s.pop()
            if len(self.s)==0:
                top = None
            else:
                top = len(self.s)-1
            return val
    #INSTANCE METHOD FOR PRINT THE TOP VALUE 
    def peek(self):
        if self.isEmpty():
            return "Underflow"
        else:
            top = len(self.s)-1
            return self.s[top]
    #INSTANCE METHOD FOR SHOWING THE STACK
    def show(self):
        if self.isEmpty():
            print("Sorry no items in stack")
        else:
            print()
            print("Displaying the Stack:")
            print()
            t = len(self.s)-1
            print("(Top)",end = '')
            while t>=0:
                print(self.s[t],"<==",end = '')
                t-=1
            print()
    #INSTANCE METHOD FOR CHOICE BY USER
    def choice(self):
        while True:
            print()
            print("*********STACK OPERATIONS**********")
            print("1.For Push")
            print("2.For Pop")
            print("3.For Peek")
            print("4.For Show ")
            print("5.For Exit")
            opt = int(input("Enter your choice:"))
            if opt == 1:
                item = input("Enter item for push:")
                self.push(item)
            elif opt == 2:
                print("Popped element:",self.pop())
            elif opt == 3:
                print("Top element:",self.peek())
            elif opt == 4:
                self.show()
            elif opt == 5:
                print("********PROGRAM END*********")
                break
            else:
                print("Invaild choice.....Try again!!!!!!!!!!")
#Create object of stack
o1 = Stack()
#call method
o1.choice()
                

            
        
