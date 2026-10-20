class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        for c in s:
            print("c: ", c)
            if len(stack) == 0:
                stack.append(c)
                # print("stack is empty: ", stack)

            elif c in m and stack[-1] == m[c]:
                # print("pop: ", 
                stack.pop()
                
            else:
                stack.append(c)
                # print("stack append, ", c)
        if stack:
            return False
        return True