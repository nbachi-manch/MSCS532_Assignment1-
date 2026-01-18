"""
MSCS532 - Assignment 1
Insertion Sort (Monotonically Decreasing Order)

This program implements the Insertion Sort algorithm to sort
a list of integers in descending (monotonically decreasing) order.
"""

from typing import List
import random


def insertion_sort_desc(arr: List[int], trace: bool = False) -> List[int]:
    """
    Sorts a list of integers in monotonically decreasing order
    using the insertion sort algorithm.

    Args:
        arr (List[int]): List of integers to sort
        trace (bool): If True, prints intermediate steps

    Returns:
        List[int]: Sorted list in descending order
    """
    a = arr.copy()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        # Shift elements smaller than key to the right
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

        if trace:
            print(f"Step {i}: {a}")

    return a


def generate_random_list(size: int, low: int = 0, high: int = 100) -> List[int]:
    """
    Generates a list of random integers.

    Args:
        size (int): Number of elements
        low (int): Minimum value
        high (int): Maximum value

    Returns:
        List[int]: Randomly generated list
    """
    return [random.randint(low, high) for _ in range(size)]


def main() -> None:
    """
    Main driver function.
    """
    data = generate_random_list(10, 0, 50)

    print("Original list:")
    print(data)

    sorted_data = insertion_sort_desc(data, trace=True)

    print("\nSorted list (descending order):")
    print(sorted_data)


if __name__ == "__main__":
    main()
