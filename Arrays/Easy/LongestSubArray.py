# Brute Force Approach
# Generate all subarrays and check their sums

def longest_subarray_brute_force(arr, target_sum):
    max_length = 0
    n = len(arr)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == target_sum:
                max_length = max(max_length, j - i + 1)
    return max_length

print(longest_subarray_brute_force([1, -1, 5, -2, 3], 3))

# Better Approach  
def longest_subarray_better(arr, target_sum):
    prefix_sum = 0
    max_length = 0
    n = len(arr)
    for i in range(n):
        prefix_sum += arr[i]
        if prefix_sum == target_sum:
            max_length = i + 1
        for j in range(i):
            if prefix_sum - arr[j] == target_sum:
                max_length = max(max_length, i - j)
    return max_length

print(longest_subarray_better([1, -1, 5, -2, 3], 3))

# Optimal Approach
def getLongestSubarray(a , k) -> int:
    
    n = len(a) # size of the array.
    preSumMap = {}
    Sum = 0
    maxLen = 0
    for i in range(n):
        # calculate the prefix sum till index i:
        Sum += a[i]

        # if the sum = k, update the maxLen:
        if Sum == k:
            maxLen = max(maxLen, i + 1)

        # calculate the sum of remaining part i.e. x-k:
        rem = Sum - k

        # Calculate the length and update maxLen:
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        # Finally, update the map checking the conditions:
        if Sum not in preSumMap:
            preSumMap[Sum] = i

    return maxLen

print("optimal" , getLongestSubarray([1, -1, 5, -2, 3], 3))