# BINARY SEARCH


#Function to find the index of a number
def binary_search(arr,target):
    beg = 0
    end = len(arr)-1
    while beg <= end:
        mid = (beg + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            beg = mid + 1
        else:
            end = mid - 1
    return -1
#main
lst = [12,67,489,78,78,362,973,748,8,9]
arr = sorted(lst)
target = int(input("Enter the number you want to find:"))
result = binary_search(arr,target)
if result != -1:
    print("Element",target,"found at index",result)
else:
    print("Element",target,"not found in the list")
