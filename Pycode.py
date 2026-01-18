"""
MSCS532 - Assignment 1
Insertion Sort (Monotonically Decreasing Order)

This script implements insertion sort to sort a list in *descending* order.
It includes:
- insertion_sort_desc(): core algorithm
- input validation
- optional step-by-step tracing
- a simple CLI demo in main()

Run:
    python insertion_sort_desc.py

Optional:
    python insertion_sort_desc.py --trace
"""

from __future__ import annotations
from typing import List, Sequence
import argparse
import random
import sys


def insertion_sort_desc(arr: Sequence[int], trace: bool = False) -> List[int]:
    """
    Sorts the input sequence into monotonically decreasing order using insertion sort.

    Args:
        arr: A sequence of comparable items (int used here for simplicity).
        trace: If True, prints the array state after each outer-loop iteration.

    Returns:
        A new list sorted in descending order.
    """
    # Make a copy so the original input isn't modified
    a = list(arr)

    # Insertion sort (descending)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        # Move elements that are < key to one position ahead
        # (This creates descending order: larger values come first)
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

        if trace:
            print(f"After inserting index {i} (key={key}): {a}")

    return a


def parse_int_list(s: str) -> List[int]:
    """
    Parses a comma-separated string into a list of ints.
    Example: "5, 2, 9, -1" -> [5, 2, 9, -1]
    """
    parts = [p.strip() for p in s.split(",") if p.strip() != ""]
    if not parts:
        raise ValueError("No numbers provided.")
    try:
        return [int(p) for p in parts]
    except ValueError as e:
        raise ValueError("Input must be a comma-separated list of integers.") from e


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Insertion Sort in monotonically decreasing order (descending)."
    )
    parser.add_argument(
        "--nums",
        type=str,
        default="",
        help='Comma-separated integers, e.g. "5,2,9,1". If omitted, a random list is used.',
    )
    parser.add_argument(
        "--n",
        type=int,
        default=10,
        help="Size of random list if --nums is not provided (default: 10).",
    )
    parser.add_argument(
        "--low",
        type=int,
        default=0,
        help="Random list minimum value (default: 0).",
    )
    parser.add_argument(
        "--high",
        type=int,
        default=100,
        help="Random list maximum value (default: 100).",
    )
    parser.add_argument(
        "--trace",
        action="store_true",
        help="Print step-by-step array state during sorting.",
    )

    args = parser.parse_args()

    # Build the list
    if args.nums.strip():
        try:
            data = parse_int_list(args.nums)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        if args.n <= 0:
            print("Error: --n must be a positive integer.", file=sys.stderr)
            sys.exit(1)
        if args.low > args.high:
            print("Error: --low must be <= --high.", file=sys.stderr)
            sys.exit(1)
        data = [random.randint(args.low, args.high) for _ in range(args.n)]

    print(f"Original: {data}")
    sorted_data = insertion_sort_desc(data, trace=args.trace)
    print(f"Sorted (descending): {sorted_data}")


if __name__ == "__main__":
    main()
