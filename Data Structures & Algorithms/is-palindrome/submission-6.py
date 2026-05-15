class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        alpha_numeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        l, r = 0, len(s)-1
        while l<=r:
            if s[l] not in alpha_numeric:
                l += 1
                continue

            if s[r] not in alpha_numeric:
                r -= 1
                continue

            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True