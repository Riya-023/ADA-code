def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = arr[p + i]
    for j in range(n2):
        R[j] = arr[q + 1 + j]
    i = 0 
    j = 0 
    k = p  

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i =i+ 1
        else:
            arr[k] = R[j]
            j =j+ 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i = i+1
        k = k+ 1
    while j < n2:
        arr[k] = R[j]
        j = j+ 1
        k = k+ 1
def merge_sort(arr, p, r):
    if p < r:
        q = (p+r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
