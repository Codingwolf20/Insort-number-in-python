def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# مثال استفاده
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)  # خروجی: [5, 6, 11, 12, 13]
