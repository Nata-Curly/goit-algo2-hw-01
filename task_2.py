from typing import List


def quick_select(arr: List[int], k: int) -> int:
    """
    This function implements the Quick Select algorithm to find the k-th smallest element in the given list.

    Time complexity: O(n) in average case
    Space complexity: O(log n)

    :param arr: The list of elements to search through
    :param k: The index of the element to find (1-indexed)
    :return: The k-th smallest element in the list
    :raises ValueError: If k is not between 1 and len(arr)
    """

    if not 1 <= k <= len(arr):
        raise ValueError("k must be within the length of the array")

    def partition(left: int, right: int, pivot_index: int) -> int:
        pivot_value = arr[pivot_index]

        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    def select(left: int, right: int, k_smallest: int) -> int:
        if left == right:
            return arr[left]

        pivot_index = (left + right) // 2
        pivot_index = partition(left, right, pivot_index)

        if k_smallest == pivot_index:
            return arr[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)

    return select(0, len(arr) - 1, k - 1)

arr1 = [18, 12, 23, -4, -55]
print(quick_select(arr1, 1))
print(quick_select(arr1, 3))
print(quick_select(arr1, 5))
