#QUEUE PROGRAM

class queue:
         #Constructor(Initializer method)
        def __init__(self):
                self.Q = []
                self.front = self.rear = None
        #INSTANCE METHOD FOR CHECKING QUEUE IS EMPTY OR NOT
        def isEmpty(self):
                if len(self.Q) == 0 :
                    return True
                else:
                    return False
        #INSTANCE METHOD FOR PUSH ITEM IN QUEUE
        def Enqueue(self,item):
                self.Q.append(item)
                if len(self.Q) == 1:
                        self.front = self.rear = 0
                else:
                        rear = len(self.Q)-1
        #INSTANCE METHOD FOR POP ITEM IN QUEUE
        def Dequeue(self):
                if self.isEmpty():
                        return "Underflow"
                else:
                        val = self.Q.pop(0)
                if len(self.Q)==0:
                        self.front = self.rear = None
                return val
        #INSTANCE METHOD FOR PRINT THE TOP VALUE 
        def peek(self):
                if self.isEmpty():
                        return "Underflow"
                else:
                        self.front = 0
                        return self.Q[self.front]
         #INSTANCE METHOD FOR PRINT THE TOP VALUE        
        def show(self):
                if self.isEmpty():
                        print("Sorry no item in Queue!!!!")
                else:
                        print()
                        print("Displaying the Queue:")
                        print()
                        t = len(self.Q)-1
                        print("(front)",end = ' ')
                        self.front = 0
                        i = self.front
                        self.rear = len(self.Q)-1
                        while (i<=self.rear):
                                print(self.Q[i],"<==",end = ' ')
                                i+=1
                        print()
        #INSTANCE METHOD FOR CHOICE BY USER
        def choice(self):
                while True:
                        print()
                        print("*********QUEUE OPERATIONS**********")
                        print("1.For Enqueue")
                        print("2.For Dequeue")
                        print("3.For Peek")
                        print("4.For Show ")
                        print("5.For Exit")
                        opt = int(input("Enter your choice:"))
                        if opt == 1:
                                item = input("Enter item for push:")
                                self.Enqueue(item)
                        elif opt == 2:
                                 print("Dequeue element:",self.Dequeue())
                        elif opt == 3:
                                 print("Top element:",self.peek())
                        elif opt == 4:
                                 self.show()
                        elif opt == 5:
                                 print("********PROGRAM END*********")
                                 break
                        else:
                                print("Invaild choice.....Try again!!!!!!!!!!")
#Create object of queue
o1 = queue()
#call method
o1.choice()
                        

                    
                


