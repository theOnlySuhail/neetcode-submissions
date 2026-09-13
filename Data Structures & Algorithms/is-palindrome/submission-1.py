class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x.lower() for x in s if x.isalpha() or x.isnumeric()]
        l, r = 0, len(s) - 1
        print(s)
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1; r -= 1
        return True