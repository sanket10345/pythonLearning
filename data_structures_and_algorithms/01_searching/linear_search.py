def linear_search(arr, target):
    """
    Perform a linear search on the given list to find the target element.

    Parameters:
    arr (list): The list of elements to search through.
    target (any): The element to find in the list.

    Returns:
    int: The index of the target element if found; otherwise, -1.

    The function iterates over each element of the list along with its index.
    If the current element matches the target, its index is returned.
    If the loop completes without finding the target, -1 is returned to indicate
    that the element is not present in the list.
    """
    for i, el in enumerate(arr):
        if el == target:
            return i
    return -1


# Example usage
arr = [5, 6, 7, 8, 9, 1, 2, 3, 4]
target = 11

index = linear_search(arr, target)
if index != -1:
    print(f'Element {target} found at index {index}')
else:
    print(f'Element {target} not found')
