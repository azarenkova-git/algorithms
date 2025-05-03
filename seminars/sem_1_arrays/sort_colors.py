def sort_colors(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 2:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
        elif arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
    return arr

print(sort_colors([2,0,1]))