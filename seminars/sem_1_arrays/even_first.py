def even_first(arr):
    ind_even = 0
    index = 0
    while index <= len(arr) - 1:
        if arr[index]%2 == 0:
            arr[index], arr[ind_even] = arr[ind_even], arr[index]
            ind_even += 1
        index += 1
    return arr
