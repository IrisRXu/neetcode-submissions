class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        # print(m)
        sorted_map = dict(sorted(m.items(), reverse=True, key=lambda item:item[1]))

        ans = list(sorted_map.keys())
        ans = ans[:k]

        return ans
