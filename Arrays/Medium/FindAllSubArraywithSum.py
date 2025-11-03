def findAllSubarraysWithGivenSum_bruteforcr(arr, k):
    n = len(arr)  # size of the given array.
    cnt = 0  # Number of subarrays.

    for i in range(n):
        for j in range(i, n):
            subarray_sum = sum(arr[i:j+1])
            if subarray_sum == k:
                cnt += 1

    return cnt

def findAllSubarraysWithGivenSum_best(arr, k):
    n = len(arr)  # size of the given array.
    cnt = 0  # Number of subarrays.

    for i in range(n):  # starting index i.
        subarray_sum = 0
        for j in range(i, n):  # ending index j.
            subarray_sum += arr[j]
            if subarray_sum == k:
                cnt += 1

    return cnt

if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    k = 6
    cnt = findAllSubarraysWithGivenSum_bruteforcr(arr, k)
    cn1 = findAllSubarraysWithGivenSum_best(arr,k)
    print("The number of subarrays is:", cnt)
    print(cn1)