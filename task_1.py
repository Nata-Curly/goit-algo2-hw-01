from typing import List, Tuple


def find_min_max(arr: List[int]) -> Tuple[int, int]:
    def _find_min_max(left: int, right: int) -> Tuple[int, int]:

        """
        Recursively finds the minimum and maximum elements in a given array.

        left: Left index of the array.
        right: Right index of the array.

        Returns a tuple of two elements: the minimum and maximum elements in the array.

        Time complexity: O(n)
        Space complexity: O(log n)
        """

        if left == right: # one element in array
            return arr[left], arr[left]

        if right == left + 1: # two elements in array
            if arr[left] < arr[right]:
                return arr[left], arr[right]
            else:
                return arr[right], arr[left]

        mid = (left + right) // 2
        min1, max1 = _find_min_max(left, mid)
        min2, max2 = _find_min_max(mid + 1, right)

        return min(min1, min2), max(max1, max2)

    if not arr:
        raise ValueError("Array cannot be empty!")

    return _find_min_max(0, len(arr) - 1)


arr1 = [18, 12, 23, -4, -55]
print(find_min_max(arr1))

arr2 = [1]
print(find_min_max(arr2))

arr3 = [1, 3]
print(find_min_max(arr3))

arr4 = []
print(find_min_max(arr4))
