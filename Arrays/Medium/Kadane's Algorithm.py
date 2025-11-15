# Kadane's Algorithm
def maxSubarraySum(arr):
    n = len(arr)
    maxi = float('-inf')

    for i in range(n):
        for j in range(i, n):
            summ = 0
            for k in range(i, j+1):
                summ += arr[k]

            maxi = max(maxi, summ)

    return maxi

print(maxSubarraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


def maxSubarraySum_better(arr):
    n = len(arr)
    maxi = float('-inf')
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            maxi = max(maxi, sum)

    return maxi

print(maxSubarraySum_better([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


def maxSubarraySum_optimal(arr, n):
    n = len(arr)
    maxi = float('-inf')
    sum = 0

    for i in range(n):
        sum += arr[i]

        if sum > maxi:
            maxi = sum

        if sum < 0:
            sum = 0

    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum_optimal(arr, n)
print("The maximum subarray sum is:", maxSum)