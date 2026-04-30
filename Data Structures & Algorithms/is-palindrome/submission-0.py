class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''.join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(t)-1

        while left < right:
            if t[left] == t[right]:
                left += 1
                right -= 1
            else:
                return False
        return True        
        