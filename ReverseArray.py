def array_slice(arr):
    res = arr[::-1]
    print("Reversed array: ", res)


def array_reverse(arr):
    arr.reverse()
    print("Reversed array: ", arr)


class ReverseArray:
    arr = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        element = int(input())
        arr.append(element)
    print("Original array: ", arr)
    array_slice(arr)  # Reversing an Array Using List Slicing
    array_reverse(arr)  # Reversing Items in a List Using the .reverse() Method
