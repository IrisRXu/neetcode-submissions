class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sn = sorted(nums)
        # print(sn)

        output = []

        for i in range(len(sn)):
            n = sn[i]
            if n > 0:
                break

            if i > 0 and n == sn[i-1]:
                continue

            l = i+1
            r = len(sn)-1

            target = -n

            while l < r:
                val = sn[l] + sn[r]
                if val < target:
                    l += 1
                elif val > target:
                    r -= 1
                else:
                    output.append([sn[l], sn[r],n])
                    l += 1
                    r -= 1
                    while sn[l] == sn[l-1] and l<r:
                        l += 1
        return output

       

        


        


# -4 -1 -1 0 1 2

# i + j = -k