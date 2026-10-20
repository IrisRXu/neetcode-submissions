class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        

        if not s:
            return 0
        unique =set(s[l])

        res = 1
        while r < len(s):
            # print(s[r], unique)
            if s[r] in unique:
                 
            # else:
                res = max(res, r-l)
                # print(s[l], unique, l, r)
                while s[l] != s[r]:
                    unique.remove(s[l])
                    l += 1
                unique.remove(s[l])
                l += 1
            unique.add(s[r])     
            r += 1
            

        res = max(res, r-l)
        return res




