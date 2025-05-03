def zero_end(arr):
    i = 0
    while i < len(arr) and arr[i]!=0:
        i +=1
    j = i
    while j < len(arr):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], 0
            i += 1
        j += 1
    return arr

print(zero_end([0,1,2,0,4,0]))