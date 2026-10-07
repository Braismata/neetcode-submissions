import math
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        remove = re.sub(r'[^a-zA-Z0-9]', '', s)
        lowercased_string= remove.lower()
        for n in range(math.ceil(len(remove)/2)):
            if lowercased_string[n]!=lowercased_string[-1-n]: return False
        return True