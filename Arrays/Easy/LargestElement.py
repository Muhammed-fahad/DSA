# Brute Force Approach
def largest_element(arr):
    arr1 = sorted(arr)
    return arr1[-1]

# Optimal Approach
def optimal_approach(arr):
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

arr = [13, 46, 24, 56 , 20 , 9]
largest_element(arr)
print(optimal_approach(arr))
