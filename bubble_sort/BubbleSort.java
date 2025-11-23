// Purpose: to sort an array 

// Function: loops through an array, checks if the current number is greater than the next number, and if it is, then swaps. Every iteration brings
// the next highest number to the end of the array, creating a sorted part section of the list that no longer needs to be checked. The sorting method
// iterates until the unsortedLength is equal 0, meaning there's nothing left to sort, or until it goes through one iteration where nothing was swapped
// meaning the array must be sorted. 

// Best Use Cases: This is an inefficient algorithm because it has a quadratic time complexity, so it does not work well with larger lists, and so
// it should rarely be used. 

// Time Complexity: O(n^2) where n is the length of the array

// Space Complexity: O(1)

// My Code
import java.util.Arrays;

public class BubbleSort {

    public static int[] bubbleSort(int[] arr) {
        int unsortedLength = arr.length;
        while (unsortedLength > 0) {
            Boolean swapped = false;
            for (int i = 0; i < unsortedLength-1; i++) {
                if (arr[i] > arr[i+1]) {
                    swapped = true;
                    int temp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = temp;
                }
            }
            if (!swapped) {
                break;
            }
            unsortedLength--; 
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
        System.out.println(Arrays.equals(arr1Sorted, bubbleSort(arr1)));
        System.out.println(Arrays.equals(arr2Sorted, bubbleSort(arr2)));
        System.out.println(Arrays.equals(arr3Sorted, bubbleSort(arr3)));
        System.out.println(Arrays.equals(arr4Sorted, bubbleSort(arr4)));
    }
}