class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output=""
        size=len(strs[0]) 
        for i in range(1,len(strs)):
            size=min(size,len(strs[i]))
        n=0
        while n<size:
            for i in range(1,len(strs)):
                if strs[i][n]!=strs[i-1][n]: return output
            output+=strs[0][n]
            n+=1
        return output