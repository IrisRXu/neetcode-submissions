from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r = 0
        m = defaultdict(int)
        most_freq_count = 0
        res = 0
        for l in range(len(s)):
            while r < len(s):
                m[s[r]] += 1
                most_freq_count = max(m.values())
                if (r - l + 1) - most_freq_count <= k:
                    res = max(res, r - l + 1)
                    r += 1
                else:
                    m[s[r]] -= 1
                    break
                
            m[s[l]] -= 1
        return res
