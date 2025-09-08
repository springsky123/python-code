#Implement a stack using two queues

from collections import deque

class mystack:
         #Constructor(Initializer method)
        def __init__(self):
                self.q1 = deque()
                self.q2 = deque()
        # Insert element
        def push (self,x):
                self.q1.append(x)
        # Remove top element
        def pop(self):
                if not self.q1:
                        return
                while len(self.q1)!=1:
                        self.q2.append(self.q1.popleft())
                self.q1.popleft()
                self.q1,self.q2 = self.q2,self.q1
        # Return top element
        def top(self):
                if not self.q1:
                        return
                while len(self.q1)!=1:
                        self.q2.append(self.q1.popleft())
                temp = self.q1.popleft()
                self.q2.append(temp)
                self.q1,self.q2 = self.q2,self.q1
                return temp
        # Return current size
        def size(self):
                return len(self.q1)
if __name__ == "__main__":
        st = mystack()
        st.push(1)
        st.push(2)
        st.push(3)

        print(st.top())
        st.pop()
        print(st.top())
        st.pop()
        print(st.top())
        print(st.size())

