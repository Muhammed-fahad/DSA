def TwoSum_Bruteforce(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            
            if nums[i]+nums[j] == target:
                return (i,j)

print(TwoSum_Bruteforce([2,6,5,8,11] , 14))

def TwoSum_optimal(nums, target):
    hashset = {}
    for i in range(len(nums)):
        if (target - nums[i]) in hashset:
            return (hashset[target-nums[i]] , i)
        else:
            hashset[nums[i]] = i

print(TwoSum_Bruteforce([2,6,5,11,8] , 13))


