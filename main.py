import time
import random


def merge_sort(arr):
    """
    Merge Sort Algorithm
    Takes in a list "arr" and sorts it in ascending order using merge sort method.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    """
    Helper function to merge two sorted arrays.
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


MIN_MERGE = 32


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
    min_run = calc_min_run(n)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    size = min_run
    while size < n:
        for start in range(0, n, 2 * size):
            midpoint = start + size - 1
            end = min((start + 2 * size - 1), (n - 1))
            merge_left = arr[start:midpoint + 1]
            merge_right = arr[midpoint + 1:end + 1]
            arr[start:start + len(merge_left) + len(merge_right)] = merge(merge_left, merge_right)
        size *= 2

    return arr

def run_times():
    # Create lists of different sizes
    list_100 = [random.randint(1, 1000) for _ in range(100)]
    list_1000 = [random.randint(1, 10000) for _ in range(1000)]
    list_10000 = [random.randint(1, 100000) for _ in range(10000)]

    # Measure and compare runtimes
    for lst in [list_100, list_1000, list_10000]:
        lst_copy = lst.copy()

        start_time = time.time()
        merge_sort(lst)
        merge_time = time.time() - start_time

        start_time = time.time()
        tim_sort(lst_copy)
        tim_time = time.time() - start_time

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

    assert merge_sort(test_array.copy()) == sorted_array
    assert tim_sort(test_array.copy()) == sorted_array

    print("All tests passed!")


test_sorting_algorithms()
run_times()
