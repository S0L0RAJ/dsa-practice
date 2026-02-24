# Reverse an array
def reverse_array(arr):
    return arr[::-1]

# Find maximum element
def find_max(arr):
    return max(arr)

# Find second largest element
def second_largest(arr):
    arr = list(set(arr))
    arr.sort()
    return arr[-2] if len(arr) > 1 else None
