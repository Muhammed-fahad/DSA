def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]        # Element to be inserted
        j = i - 1
        while j >= 0 and key < arr[j]:  # Compare with previous elements
            arr[j + 1] = arr[j]         # Shift elements
            j -= 1
        arr[j + 1] = key                # Insert at the correct position
    return arr

# Example:
arr = [12, 11, 13, 5, 6]
print("Sorted array:", insertion_sort(arr))
