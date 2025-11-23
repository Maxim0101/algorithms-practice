// Purpose: to sort a arr 

// Function: the program loops through an array, checks if the current number is less than the previous number, and if it is, loops backward until it finds a spot
// where the current number is greater than the previous number, swapping numbers along the way if not

// Best Use Cases: This is an okay algorithm for sorting small arrs, however, it is not scalable for larger arrs because of the worst case time complexity which
// grows quadratically. I think this should be avoided for much better algorithms.

// Time Complexity: O(n^2)

// Space Complexity: O(1)

// My Code
import java.util.Arrays;

public class InsertionSort {

    public static int[] insertionSort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int j = i;
            while (j > 0 && arr[j] < arr[j-1]) {
                int temp = arr[j-1];
                arr[j-1] = arr[j];
                arr[j] = temp;
                j--;
            }
        }
        return arr;
    }
    public static void main(String[] args) {
        // Testing Examples
        int[] arr1 = {-1, 0, 1, 2, 3, 4, 5};
        int[] arr1Sorted = {-1, 0, 1, 2, 3, 4, 5};

        int[] arr2 = {4, 0, 4, 2, -1, 5, 3, 1};
        int[] arr2Sorted = {-1, 0, 1, 2, 3, 4, 4, 5};

        int[] arr3 = {0, -1, 1, 5, 3, 2, 4};
        int[] arr3Sorted = {-1, 0, 1, 2, 3, 4, 5};

        int[] arr4 = {};
        int[] arr4Sorted = {};

        // Expected Test Results
        System.out.println(Arrays.equals(arr1Sorted, insertionSort(arr1)));
        System.out.println(Arrays.equals(arr2Sorted, insertionSort(arr2)));
        System.out.println(Arrays.equals(arr3Sorted, insertionSort(arr3)));
        System.out.println(Arrays.equals(arr4Sorted, insertionSort(arr4)));
    }
}