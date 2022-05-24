#https://leetcode.com/problems/backspace-string-compare/
from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        temp1 = deque([])
        temp2 = deque([])
        for a in s:
            if a != "#":
                temp1.append(a)
            elif temp1:
                temp1.pop()
        for b in t:
            if b != "#":
                temp2.append(b)
            elif temp2:
                temp2.pop()
        return temp1 == temp2




sol = Solution()
print(sol.backspaceCompare(s = "ab##", t = "c#d#"))
print(sol.backspaceCompare(s = "ab#c",t = "ad#c"))
