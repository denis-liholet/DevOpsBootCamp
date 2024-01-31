def linear_search(arr, target):
    """
    Function to perform linear search on a list.

    :param arr: List in which to search.
    :param target: Element to search for.
    :return: Index of the target if found, else -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"Number of iterations: {i}")
            print("Big O notation is O(n), where n is the number of elements in the list.")
            return i  # Target found, return the index
    return -1  # Target not found


def binary_search(arr, target):
    """
    Function to perform binary search on a sorted list.

    :param arr: List in which to search.
    :param target: Element to search for.
    :return: Index of the target if found, else -1.
    """
    counter = 1
    arr.sort()  # Sort the list
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            print(f"Number of iterations: {counter}")
            print("Big O notation is O(log n), where n is the number of elements in the list.")
            return mid  # Target found, return the index
        elif arr[mid] < target:
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half
        counter += 1

    return -1  # Target not found


# Example usage
array = [i for i in range(5000)]  # Create an array of 5000 elements
element = 500

bin_result = binary_search(array, element)
print(f"Binary Search: Index of {element} is {bin_result}\n")

lin_result = linear_search(array, element)
print(f"Linear Search: Index of {element} is {lin_result}")
