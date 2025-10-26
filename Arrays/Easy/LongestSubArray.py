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

