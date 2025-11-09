from collections import Counter

def majorityElement_bruteFore(v):
    n = len(v) # size of the list
    ls = [] # list of answers

    for i in range(n):
        if len(ls) == 0 or ls[0] != v[i]:
            cnt = 0
            for j in range(n):

                if v[j] == v[i]:
                    cnt += 1

            # check if frquency is greater than n/3:
            if cnt > (n // 3):
                ls.append(v[i])

        if len(ls) == 2:
            break

    return ls


def majorityElement_better(arr):
    n = len(arr)
    counter = Counter(arr)
    for num, count in counter.items():
        if count > (n // 2):
            return num

    return -1

print(majorityElement_bruteFore([11, 33, 33, 11, 33, 11]))