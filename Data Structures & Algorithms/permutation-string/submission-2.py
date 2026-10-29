class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        m1 = [0] * 26
        m2 = [0] * 26
        l = len(s1)
        for c in s1:
            idx = ord(c) - ord('a')
            m1[idx] += 1

        for i in range(l):
            # print(i)
            idx = ord(s2[i]) - ord('a')
            m2[idx] += 1

        for i in range(l, len(s2)):
            if m2 == m1:
                return True
            
            idx_l = ord(s2[i-l]) - ord('a')
            idx_r = ord(s2[i]) - ord('a')
            m2[idx_l] -= 1
            m2[idx_r] += 1

            # print(m2)

        if m2 == m1:
            return True
        
        return False

        