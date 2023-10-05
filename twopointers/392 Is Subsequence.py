"""
36ms
Beats 77.50%of users with Python3

16.38MB
Beats 40.29%of users with Python3

"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0  # Initialize left and right pointers
        
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1  # Move the left pointer if characters match
            r += 1  # Always move the right pointer
            
        # If the left pointer reached the end of s, it means s is a subsequence of t
        return l == len(s)
if __name__ == '__main__':
    s, t ="abc", "ahbgdc"
    res = Solution().isSubsequence(s,t)
    assert res==True
    print("\n")
    s,t ="aaaaaa","bbaaaa"
    res = Solution().isSubsequence(s,t)
    assert res==False
