class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        while len(prices) > 1 and prices[0] > prices[1]:
            prices.pop(0)
        if len(prices)==1: return 0
        while prices[-1]<prices[-2]:
            prices.pop()
        if len(prices)==2: return prices[1]-prices[0]
        size= len(prices)
        minimum = [1000] * size
        maximum = [0] * size
        for i in range(size):
            minimum[i]=min(minimum[i-1],prices[i])
        maximum[size-1]=prices[size-1]
        for i in range(size - 2, -1, -1):
            maximum[i]=max(maximum[i+1],prices[i])
        dif=0
        for i in range(size):
            dif=max(dif,(maximum[i]-minimum[i]))
        return dif


        