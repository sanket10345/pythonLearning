def binary_search(arr, target):
    """
    Perform a binary search on a sorted list to find the index of the target element.

    Parameters:
    arr (list): A sorted list of elements to search through.
    target (any): The element to find in the list.

    Returns:
    int: The index of the target if found; otherwise, -1.

    Binary search works by repeatedly dividing the search interval in half.
    - Start with two pointers, left (start of the array) and right (end of the array).
    - Calculate the middle index.
    - If the element at the middle index equals the target, return the index.
    - If the target is greater than the middle element, search in the right half.
    - If the target is smaller, search in the left half.
    - Repeat until the pointers converge.
    Note: The list must be sorted for binary search to work correctly.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = 12.5
index = binary_search(arr, target)
if index != -1:
    print(f'Element {target} found at index {index}')
else:
    print(f'Element {target} not found')

target = 12
index = binary_search(arr, target)
if index != -1:
    print(f'Element {target} found at index {index}')
else:
    print(f'Element {target} not found')
