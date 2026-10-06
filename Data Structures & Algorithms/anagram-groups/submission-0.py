class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output=defaultdict(list)
        for s in strs:
            sort=''.join(sorted(s))
            output[sort].append(s)
        return list(output.values())