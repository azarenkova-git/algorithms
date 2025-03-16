def rotate_array(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

def rotate_part_array(arr, k):
    if arr == [] or k == 0:
        return arr
    else:
        n = len(arr)
        rotate_array(arr, 0, n - 1)
        rotate_array(arr, 0, k % n - 1)
        rotate_array(arr, k % n, n - 1)
        return arr
print(rotate_part_array([1, 2, 3, 4, 5], 2))

