arr = [2, 3, 4, 10, 40]
search_element = 10

p = 0
r = len(arr) - 1
while p <= r:
    mid = (p+r)//2
    
    if arr[mid] == search_element:
        result = mid
        break
    
    elif arr[mid] < search_element:
        p = mid + 1
    
    else:
        r = mid - 1
else:
    result = -1



if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")