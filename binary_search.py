# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:

import random
import time
from static_array import *


# ------------------- PROBLEM 1 - -------------------------------------------


def binary_search(arr: StaticArray, target: int) -> int:
    """
    Receives a StaticArray and an integer target and returns the index of
    the target element if it is present in the array or returns -1 if it is not.
    """
    length = arr.size()
    low, high = 0, length - 1

    while low <= high:

        if arr[0] < arr[length - 1]:
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid

            elif target < arr[mid]:
                high = mid - 1

            else:
                low = mid + 1

        else:
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid

            elif target > arr[mid]:
                high = mid - 1

            else:
                low = mid + 1

    return -1


# ------------------- PROBLEM 2 - -------------------------------------------


def binary_search_rotated(arr: StaticArray, target: int) -> int:
    """
    Receives a StaticArray and an integer target and returns the index of
    the target element if it is present in the array or returns -1 if it is not.
    """
    length = arr.size()

    low, high = 0, length

    while low < high:
        mid = low + (high - low)//2
        if arr[mid] == target:
            return mid

        if arr[low] < arr[mid]:
            if arr[mid] > target >= arr[low]:
                high = mid

            else:
                low = mid + 1

        else:
            if arr[mid] < target <= arr[high - 1]:
                low = mid + 1
            else:
                high = mid

    return -1


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":
    pass

    # print('\n# problem 1 example 1')
    # src = (-10, -5, 0, 5, 7, 9, 11)
    # targets = (7, -10, 11, 0, 8, 1, -100, 100)
    # arr = StaticArray(len(src))
    # for i, value in enumerate(src):
    #     arr[i] = value
    # print([binary_search(arr, target) for target in targets])
    # arr._data.reverse()
    # print([binary_search(arr, target) for target in targets])
    #
    # print('\n# problem 1 example 2')
    # src = [random.randint(-10 ** 7, 10 ** 7) for _ in range(5_000_000)]
    # src = sorted(set(src))
    # arr = StaticArray(len(src))
    # arr._data = src[:]
    #
    # # add 20 valid and 20 (likely) invalid targets
    # targets = [-10 ** 8, 10 ** 8]
    # targets += [arr[random.randint(0, len(src) - 1)] for _ in range(20)]
    # targets += [random.randint(-10 ** 7, 10 ** 7) for _ in range(18)]
    #
    # result, total_time = True, 0
    # for target in targets:
    #     total_time -= time.time()
    #     answer = binary_search(arr, target)
    #     total_time += time.time()
    #     result &= arr[answer] == target if target in src else answer == -1
    # print(result, total_time < 0.5)
    #
    # arr._data.reverse()
    # for target in targets:
    #     total_time -= time.time()
    #     answer = binary_search(arr, target)
    #     total_time += time.time()
    #     result &= arr[answer] == target if target in src else answer == -1
    # print(result, total_time < 0.5)

    print('\n# problem 2 example 1')
    test_cases = (
        ((6, 8, 12, 20, 0, 2, 5, 9), 0),
        ((6, 8, 12, 20, 0, 2, 5, 9), -1),
        ((1,), 1),
        ((1,), 0),
        ((-689518409, -304117705, 922976428), -1000000000),
        ((517391563, 720581049, 840517417, 929287243, -867829919, -759633569, -711879816, -589718124, 87297208), -867829919)
    )
    result = []
    for src, target in test_cases:
        arr = StaticArray(len(src))
        for i, value in enumerate(src):
            arr[i] = value
        result.append((binary_search_rotated(arr, target)))
    print(*result)

    print('\n# problem 2 example 2')

    src = [random.randint(-10 ** 7, 10 ** 7) for _ in range(5_000_000)]
    src = sorted(set(src))
    arr = StaticArray(len(src))
    arr._data = src[:]

    # add 20 valid and 20 (likely) invalid targets
    targets = [-10 ** 8, 10 ** 8]
    targets += [arr[random.randint(0, len(src) - 1)] for _ in range(20)]
    targets += [random.randint(-10 ** 7, 10 ** 7) for _ in range(18)]

    result, total_time = True, 0
    for target in targets:
        # rotate arr random number of steps
        pivot = random.randint(0, len(src) - 1)
        arr._data = src[pivot:] + src[:pivot]

        total_time -= time.time()
        answer = binary_search_rotated(arr, target)
        total_time += time.time()
        result &= arr[answer] == target if target in src else answer == -1
    print(result, total_time < 0.5)
