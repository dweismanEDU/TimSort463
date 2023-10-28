import time
import random

def merge_sort(arr):
    """
    Merge Sort Algorithm
    Takes in a list "arr" and sorts it in ascending order using merge sort.
    """
    if len(arr) <= 1:  # Base case: if the array has one or zero elements(already sorted).
        return arr

    mid = len(arr) // 2  # Find the middle index.
    left = merge_sort(arr[:mid])  # Recursively apply merge sort on left half.
    right = merge_sort(arr[mid:])  # Recursively apply merge sort on right half.

    return merge(left, right)  # Merge the two sorted halves.

def merge(left, right):
    """
    Helper function to merge two sorted arrays.
    """
    result = []  # Initialize an empty list to store the sorted elements.
    i = j = 0  # Initialize pointers for each array.

    # Traverse each array and pick the smaller element of each at every step.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])  # Add any remaining elements in the left array.
    result.extend(right[j:])  # Add any remaining elements in the right array.

    return result  # Return the merged and sorted array.

MIN_MERGE = 32  # Constant used in TimSort algorithm.

def calc_min_run(n):
    """Returns the minimum length of a run from 23 - 64 so that
    the len(array)/minrun is less than or equal to a power of 2."""
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    # Insertion sort: Traverses the array and inserts each element in its correct position.
    for i in range(left + 1, right + 1):
        key = array[i]
        j = i - 1
        while j >= left and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    return array


def tim_sort(arr):
    """
    TimSort Algorithm
    """
    n = len(arr)
    min_run = calc_min_run(n)  # Calculate the minimum run length.

    # Sort individual runs using insertion sort.
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    size = min_run
    # Merge runs: Continuously merge runs to sort the entire array.
    while size < n:
        for start in range(0, n, 2 * size):
            midpoint = start + size - 1
            end = min((start + 2 * size - 1), (n - 1))
            merge_left = arr[start:midpoint + 1]
            merge_right = arr[midpoint + 1:end + 1]
            arr[start:start + len(merge_left) + len(merge_right)] = merge(merge_left, merge_right)
        size *= 2

    return arr  # Return the sorted array.

def run_times():
    # Create lists of different sizes to evaluate the runtime of sorting algorithms.
    list_100 = [random.randint(1, 1000) for _ in range(100)]
    list_1000 = [random.randint(1, 10000) for _ in range(1000)]
    list_10000 = [random.randint(1, 100000) for _ in range(10000)]

    # Measure and compare runtimes of merge sort and TimSort.
    for lst in [list_100, list_1000, list_10000]:
        lst_copy = lst.copy()

        # Measure the runtime of merge sort.
        start_time = time.time()
        merge_sort(lst)
        merge_time = time.time() - start_time

        # Measure the runtime of TimSort.
        start_time = time.time()
        tim_sort(lst_copy)
        tim_time = time.time() - start_time

        # Output the runtime results.
        print(f"Size of list: {len(lst)}")
        print(f"MergeSort runtime: {merge_time:.5f} seconds")
        print(f"TimSort runtime: {tim_time:.5f} seconds")
        print("-----------------------------")

def test_sorting_algorithms():
    """
    Test function to validate the sorting algorithms
    """
    test_array = [64, 25, 12, 22, 11]
    sorted_array = [11, 12, 22, 25, 64]

    # Assert the correctness of merge sort and TimSort.
    assert merge_sort(test_array.copy()) == sorted_array
    assert tim_sort(test_array.copy()) == sorted_array

    print("All tests passed!")  # Output if all tests passed.

# Run the test and runtime measurement functions.
test_sorting_algorithms()
run_times()
