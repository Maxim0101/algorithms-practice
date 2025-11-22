# Purpose: to sort a list 

# Function: the program loops through an array, checks if the current number is less than the previous number, and if it is, loops backward until it finds a spot
# where the current number is greater than the previous number, swapping numbers along the way if not

# Best Use Cases: This is an okay algorithm for sorting small lists, however, it is not scalable for larger lists because of the worst case time complexity which
# grows quadratically. I think this should be avoided for much better algorithms.

# Time Complexity: O(n^2)

# Space Complexity: O(1)

# My Code 
def insertion_sort(list):
    i = 1
    while (i < len(list)):
        if (list[i] < list[i-1]):
            j = i
            while (j > 0):
                if list[j] >= list[j-1]:
                    break
                else:
                    temp = list[j]
                    list[j] = list[j-1]
                    list[j-1] = temp
                j -= 1
        i += 1
    return list

# Testing Examples
list1 = [-1, 0, 1, 2, 3, 4, 5]
list2 = [4, 0, 4, 2, -1, 5, 3, 1]
list3 = [0, -1, 1, 5, 3, 2, 4]
list4 = []

# Expected Test Results
# [-1, 0, 1, 2, 3, 4, 5]
print(insertion_sort(list1))
# [-1, 0, 1, 2, 3, 4, 4, 5]
print(insertion_sort(list2))
# [-1, 0, 1, 2, 3, 4, 5]
print(insertion_sort(list3))
# []
print(insertion_sort(list4))