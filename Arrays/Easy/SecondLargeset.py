arr = [13, 46, 24, 56 , 20 , 9]
# Brute Force Approach
def second_largest(arr):
    arr1 = sorted(arr)
    return arr1[-2]


# Optimal Approach
def optimal_approach(arr):
    largest = second_largest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    return second_largest

print(second_largest(arr))
print(optimal_approach(arr))