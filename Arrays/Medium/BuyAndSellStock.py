def BuySellBruteforce(prices):
    maxprofit = 0
    for i in range(1, len(prices)):
        mini = min(prices[:i])
        profit = prices[i] - mini
        maxprofit = max(maxprofit, profit)
    return maxprofit

print(BuySellBruteforce([7,9,5,3,8,1]))

def maxProfit_optimal(arr):
    maxPro = 0
    minPrice = float('inf')
    for i in range(len(arr)):
        minPrice = min(minPrice, arr[i])
        maxPro = max(maxPro, arr[i] - minPrice)
    return maxPro

print(maxProfit_optimal([7,9,5,3,8,1]))