class Solution:
    def validPalindrome(self, s: str) -> bool:
        izq,der=0,len(s)-1
        checkpoint=[]
        while izq<der:
            if s[izq]==s[der]:
                izq+=1
                der-=1
            if s[izq]!=s[der]:
                if len(checkpoint)==0:
                    checkpoint.append(izq)
                    izq+=1
                elif len(checkpoint)==1:
                    izq=checkpoint[0]
                    der=len(s)-2-izq
                    checkpoint.append(izq+1)
                else:
                    return False
        return True