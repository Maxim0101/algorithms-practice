# Purpose: to sort an array 

# Function: loops through an array, checks if the current number is greater than the next number, and if it is, then swaps. Every iteration brings
# the next highest number to the end of the array, creating a sorted part section of the list that no longer needs to be checked. The sorting method
# iterates until the unsortedLength is equal 0, meaning there's nothing left to sort, or until it goes through one iteration where nothing was swapped
# meaning the array must be sorted. 

# Best Use Cases: This is an inefficient algorithm because it has a quadratic time complexity, so it does not work well with larger lists, and so
# it should rarely be used. 

# Time Complexity: O(n^2) where n is the length of the array

# Space Complexity: O(1)

# My Code 
def bubble_sort(arr):
    unsortedLength = len(arr)-1

    while (unsortedLength > 0):
        i = 0
        swapped = False
        while (i < unsortedLength):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
            i += 1
        unsortedLength -= 1
        if (swapped == False):
            break

    return arr

# Testing Examples
arr1 = [-1, 0, 1, 2, 3, 4, 5]
arr2 = [4, 0, 4, 2, -1, 5, 3, 1]
arr3 = [0, -1, 1, 5, 3, 2, 4]
arr4 = []

# Expected Test Results
# [-1, 0, 1, 2, 3, 4, 5]
print(bubble_sort(arr1))
# [-1, 0, 1, 2, 3, 4, 4, 5]
print(bubble_sort(arr2))
# [-1, 0, 1, 2, 3, 4, 5]
print(bubble_sort(arr3))
# []
print(bubble_sort(arr4))