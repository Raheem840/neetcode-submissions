class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = sorted(s)
        t1 = sorted(t)
        i = 0
        for char in s1:
            if s1[i] == t1[i]:
                i += 1
            else:
                return False
                break 
        return True