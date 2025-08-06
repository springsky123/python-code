#LINEAR SEARCH

#Function to find the index of a number by simple function
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
#main
lst = [12,67,489,78,78,362,973,748,8,9]
target = int(input("Enter the number you want to find:"))
result = linear_search(lst,target)
if result != -1:
    print("Element",target,"found at index",result)
else:
    print("Element",target,"not found in the list")


#Function to find the index of a number by recursive function
def linear_search_recursive(arr,target,index=0):
    if index > len(arr):
        return -1
    try:
        if arr[index]==target:
            return index
    except:
        return -1
    return linear_search_recursive(arr,target,index+1)

#main
lst1 = [12,67,489,78,78,362,973,748,8,9]
target1 = int(input("Enter the number you want to find:"))
result1 = linear_search_recursive(lst1,target1)
if result1 != -1:
    print("Element",target1,"found at index",result1)
else:
    print("Element",target1,"not found in the list")

