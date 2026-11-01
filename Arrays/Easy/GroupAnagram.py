def GroupAnagram(strs):
    store = {}
    for word in strs:
        sort = ''.join(sorted(word))
        if sort not in store:
            store[sort] =[]
        store[sort].append(word)
    return list(store.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(GroupAnagram(strs))
