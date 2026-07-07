class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        removed_one = False
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            elif removed_one:
                return False
            
            
            if s[l] == s[r-1] and (s[l+1] == s[r-2] or l+1 >= r-2):
                removed_one = True
                l += 2
                r -= 3
            elif s[l+1] == s[r] and (s[l+2] == s[r-1] or l+2 >= r-1):
                removed_one = True
                l += 3
                r -= 2
            else:
                return False

        return True           
        
