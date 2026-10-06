class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)): return False
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))
        for num in range(len(s)):
            if sorted_s[num]!=sorted_t[num]: return False
        return True