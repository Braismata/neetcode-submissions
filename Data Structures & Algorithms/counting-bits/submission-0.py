class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        bits = 0
        c=n
        while c > 0:
            c &= (c - 1)
            bits += 1
        return self.countBits(n-1) + [bits]