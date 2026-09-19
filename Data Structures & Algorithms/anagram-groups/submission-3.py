from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for char in s:
                arr[ord(char)-ord('a')] += 1
            # print(arr)
            key = "-".join(map(str, arr))
            # print(key)
            m[key].append(s)

        # print(m)
        return list(m.values())
            
        