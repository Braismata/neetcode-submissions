class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size=len(digits)
        if digits[size-1]!=9:
            digits[size-1]+=1
            return digits
        else:
            n=1
            while n<(size+1):
                if digits[size-n]!=9:
                    digits[size-n]+=1
                    n-=1
                    while n>0:
                        digits[size-n]=0
                        n-=1
                    return digits
                else:
                    n+=1
            return [1]+size*[0]

