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

    left, right = 0, 0 # 2 pointers
    Sum = a[0]
    maxLen = 0
    while right < n:
        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1

        # if sum = k, update the maxLen i.e. answer:
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)

        # Move forward the right pointer:
        right += 1
        if right < n: Sum += a[right]

    return maxLen

print(getLongestSubarray([1, -1, 5, -2, 3], 3))