def sequential_search(A, key, low, high):
    for i in range(low, high+1):
        if key == A[i].key :
            return i
    return None

def binary_search(A, key, low, high):
    if low <= high :
        middle = (low + high) // 2
        if key == A[middle].key:
            return middle
        elif key < A[middle].key :
            return binary_search(A, key, low, middle - 1)
        else :
            return binary_search(A, key, middle + 1, high)
    return None

def binary_search_iter(A, key, low, high):
    while (low <= high):
        middle = (low + high) // 2
        if key == A[middle].key: return middle
        elif (key > A[middle].key): low = middle + 1
        elif (key < A[middle].key): high = middle - 1

def interpolation_search(A, key, low, high):
    if low <= high :
        middle = int(low + (high-low) * (key-A[low].key) / (A[high].key-A[low].key))
        if key == A[middle].key:
            return middle
        elif key < A[middle].key :
            return binary_search(A, key, low, middle - 1)
        else :
            return binary_search(A, key, middle + 1, high)
    return None