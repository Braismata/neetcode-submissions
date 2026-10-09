class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximo,count=0,0
        l,r=0,0
        positions =  {}
        while r<(len(s)):
            if s[r] in positions:
                l=max(l,positions[s[r]]+1)
            positions[s[r]]=r
            count=1+r-l
            if (count>maximo):
                maximo=count
            r+=1
        return maximo