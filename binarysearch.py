# BINARY SEARCH

#Function to find the index of a number by recursive funtion
def binary_search(arr,target,low,high):
    if low>high:
        return -1
    mid = (low + high)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
         return binary_search(arr,target,low,mid-1)
    else:
        return binary_search(arr,target,mid+1,high)
    return -1
#main
lst = [12,67,489,78,78,362,973,748,8,9]
arr = sorted(lst)
target = int(input("Enter the number you want to find:"))
result = binary_search(arr,target,0,len(arr)-1)
if result != -1:
    print("Element",target,"found at index",result)
else:
    print("Element",target,"not found in the list")

