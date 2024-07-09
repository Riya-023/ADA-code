arr=[3,1,9,7,1,2,4]
max_element=max(arr)
print(max_element)

count_array = [0] * (max_element + 1)  
print(count_array)

for num in arr:
    count_array[num] =count_array[num] + 1
print(count_array)

for i in range(1, max_element + 1):
        count_array[i] =count_array[i]+ count_array[i - 1]
        
sorted_arr = [0] * len(arr)

for num in reversed(arr):
        sorted_arr[count_array[num] - 1] = num
        count_array[num] = count_array[num] - 1

print(f"Sorted array using count sort : {sorted_arr}")
