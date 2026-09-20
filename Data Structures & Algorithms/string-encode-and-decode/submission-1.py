class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
            # print(res)
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            init = i
            while s[i] != "#":
                i+=1
            str_len = int(s[init:i])
            i += 1
            res.append(s[i:i+str_len])
            i += str_len

        return res


