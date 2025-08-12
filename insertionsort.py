#INSERTION SORT

#function for sorting

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

#main
my_list = [12,11,13,5,3,22,81,2]
insertion_sort(my_list)
print("Sorted array is:")
print(my_list)
