from itertools import permutations
def NextPermutation_bruteforce(nums):
    perms = sorted(set(permutations(nums)))
    print(perms)
    current = tuple(nums)
    for i in range(len(perms)):
        if perms[i] == current:
            # If last permutation, return first
            if i == len(perms) - 1:
                return list(perms[0])
            # Else return next
            return list(perms[i + 1])

    return nums

next_perm = NextPermutation_bruteforce([1,2,3])
print(next_perm)