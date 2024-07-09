def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def quick_sort(arr, p, r):
    if p < r:
        pi = partition(arr, p, r)
        quick_sort(arr, p, pi - 1)
        quick_sort(arr, pi + 1, r)
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Original array:", arr)
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
