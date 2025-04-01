def merge_sorted_arrays(arr1, arr2):
    arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    arr.extend(arr1[i:])
    arr.extend(arr2[j:])
    return arr

