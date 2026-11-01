def topKFrequent(nums,k):
    store = {}

    for i in nums:
        store[i] = store.get(i, 0) + 1

    numbers = sorted(store, key=lambda x: store[x], reverse=True)

    return numbers[:k]


nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
print(topKFrequent(nums,k))