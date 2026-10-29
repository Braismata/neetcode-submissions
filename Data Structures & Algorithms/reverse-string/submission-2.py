class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i,d=0,len(s)-1
        while i<d:
            s[i], s[d] = s[d], s[i]
            i+=1
            d-=1