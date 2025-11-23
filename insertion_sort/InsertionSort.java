// Purpose: to sort a list 

// Function: the program loops through an array, checks if the current number is less than the previous number, and if it is, loops backward until it finds a spot
// where the current number is greater than the previous number, swapping numbers along the way if not

// Best Use Cases: This is an okay algorithm for sorting small lists, however, it is not scalable for larger lists because of the worst case time complexity which
// grows quadratically. I think this should be avoided for much better algorithms.

// Time Complexity: O(n^2)

// Space Complexity: O(1)

// My Code
import java.util.Arrays;

public class InsertionSort {

    public static int[] insertionSort(int[] list) {
        for (int i = 0; i < list.length; i++) {
            int j = i;
            while (j > 0 && list[j] < list[j-1]) {
                int temp = list[j-1];
                list[j-1] = list[j];
                list[j] = temp;
                j--;
            }
        }
        return list;
    }
    public static void main(String[] args) {
        // Testing Examples
        int[] list1 = {-1, 0, 1, 2, 3, 4, 5};
        int[] list1Sorted = {-1, 0, 1, 2, 3, 4, 5};

        int[] list2 = {4, 0, 4, 2, -1, 5, 3, 1};
        int[] list2Sorted = {-1, 0, 1, 2, 3, 4, 4, 5};

        int[] list3 = {0, -1, 1, 5, 3, 2, 4};
        int[] list3Sorted = {-1, 0, 1, 2, 3, 4, 5};

        int[] list4 = {};
        int[] list4Sorted = {};

        // Expected Test Results
        System.out.println(Arrays.equals(list1Sorted, insertionSort(list1)));
        System.out.println(Arrays.equals(list2Sorted, insertionSort(list2)));
        System.out.println(Arrays.equals(list3Sorted, insertionSort(list3)));
        System.out.println(Arrays.equals(list4Sorted, insertionSort(list4)));
    }
}