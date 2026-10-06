class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        for n in nums:
            count[n]+=1
        import heapq
        res = heapq.nlargest(k, count.values())
        for i in list(count.keys()):
            if count[i] < res[k-1]: count.pop(i)
        return list(count.keys())