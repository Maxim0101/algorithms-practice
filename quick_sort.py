# QUICK SORT [ TC: O(n^2), SC: O(logn) ]
# ADVANTAGES
# - faster than many sorting algorithms for large datasets compared to Bubble or Insertion Sort
# - does not require additional memory
# - If pivot is chosen well, great time complexity
# DISADVANTAGES
# - Excessive recursion can lead to stack overflow
# - May not preserver relate order of quality elements
# - Performance heavily depends on how the pivot is chosen, could have a bad time complexity
# - Difficult to implement for Linked Lists
# PSEUDOCODE
# - Quicksort (array, low, high)
#   - If low is less than high
#       - Pivot location = Partition(array, low high)
#       - Quicksort (array, low, pivot_location)
#       - Quicksort(array, pivot_location+1, high)
# - Partition(array, low, high)
#   - Pivot = array[low]
#   - leftwall = low
#   - For range low+1 to high
#       - If a[i] is less than pivot
#           - Swap a[il and a [leftwall]
#           - leftwall = leftwall + 1
# - swap(pivot, a [leftwall]



# MY CODE:










# GPT's OPTMIZED VERSION: