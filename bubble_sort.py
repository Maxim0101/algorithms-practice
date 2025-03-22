# BUBBLE SORT [ TC: O(n^2), SC: 0(1) ]
# ADVANTAGES
# - Simple
# - easy to implement
# - useful for small datasets
# DISADVANTAGES
# - Inefficient for large datasets
# - High time complexity
# PSEUDOCODE
# - Start at beginning of array
#   - Swap the first and second element of array if second element is less than first element.
#   - Move on to the next set of elements and keep doing this until you reach the end.
#   - If you have swapped a set of elements at least one time, then redo the whole process
#   - If you did not swap a single set of elements during the whole iteration, then that means the list is sorted, so the algorithm is finished.



# MY CODE
list1 = [-1, 0, 1, 2, 3, 4, 5]
list2 = [4, 0, 4, 2, -1, 5, 3, 1]
list3 = [0, -1, 1, 5, 3, 2, 4]

def bubble_sort(list):
    swapped_once = True
    while (swapped_once):
        swapped_once = False
        for i in range(len(list) - 1):
            if (list[i] > list[i+1]):
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                swapped_once = True
    return list

print(bubble_sort(list1))
print(bubble_sort(list2))
print(bubble_sort(list3))



# GPT's OPTIMIZED VERSION:
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

print(bubble_sort(list1.copy()))
print(bubble_sort(list2.copy()))
print(bubble_sort(list3.copy()))