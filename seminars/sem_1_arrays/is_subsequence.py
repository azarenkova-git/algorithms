def is_subsequence(a, b):
    i = 0
    j = 0

    while j < len(b) and i < len(a):
        if a[i] == b[j]:
            i += 1
        j += 1

    return i == len(a)

a = []
b = []
print(is_subsequence(a, b))