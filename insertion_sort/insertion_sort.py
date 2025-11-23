# Purpose: to sort a list 

# Function: the program loops through an array, checks if the current number is less than the previous number, and if it is, loops backward until it finds a spot
# where the current number is greater than the previous number, swapping numbers along the way if not

# Best Use Cases: This is an okay algorithm for sorting small lists, however, it is not scalable for larger lists because of the worst case time complexity which
# grows quadratically. I think this should be avoided for much better algorithms.

# Time Complexity: O(n^2) where n is the length of the list

# Space Complexity: O(1)

# My Code 
def insertion_sort(arr):
    i = 1
    while (i < len(arr)):
        if (arr[i] < arr[i-1]):
            j = i
            while (j > 0):
                if arr[j] >= arr[j-1]:
                    break
                else:
                    temp = arr[j]
                    arr[j] = arr[j-1]
                    arr[j-1] = temp
                j -= 1
        i += 1
    return arr

# Testing Examples
arr1 = [-1, 0, 1, 2, 3, 4, 5]
arr2 = [4, 0, 4, 2, -1, 5, 3, 1]
arr3 = [0, -1, 1, 5, 3, 2, 4]
arr4 = []

# Expected Test Results
# [-1, 0, 1, 2, 3, 4, 5]
print(insertion_sort(arr1))
# [-1, 0, 1, 2, 3, 4, 4, 5]
print(insertion_sort(arr2))
# [-1, 0, 1, 2, 3, 4, 5]
print(insertion_sort(arr3))
# []
print(insertion_sort(arr4))