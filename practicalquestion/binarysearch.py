#-----------BINARY SEARCH------------

import time
start = time.time()

class binarysearch:
    #Constructor(Initializer method)
    def __init__(self,arr,target):
        self.arr = arr
        self.target = target

    #Function to find the index of a number by recursive funtion
    def binary_search(self,low,high):
        if low>high:
            return -1
        mid = (low + high)//2
        if self.arr[mid] == self.target:
            return mid
        elif self.arr[mid] > self.target:
             return self.binary_search(low,mid-1)
        else:
            return self.binary_search(mid+1,high)
        return -1
#main
lst = [12,67,489,78,78,362,973,748,8,9]
arr = sorted(lst)
target = int(input("Enter the number you want to find:"))
#create object of binarysearch
o1 = binarysearch(arr,target)
#call method
result = o1.binary_search(0,len(arr)-1)
if result != -1:
    print("Element",target,"found at index",result)
else:
    print("Element",target,"not found in the list")

end = time.time()
t = end-start
print()
print("Total time taken by this program:",t)
