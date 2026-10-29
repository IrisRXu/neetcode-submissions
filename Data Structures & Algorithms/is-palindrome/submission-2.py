class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        sArr = []

        for c in s:
            if c.isalnum():
                sArr.append(c)

        l = 0
        r = len(sArr)-1

        while l < r:
            if sArr[l].lower() != sArr[r].lower():
                return False
            l += 1
            r -= 1
        return True