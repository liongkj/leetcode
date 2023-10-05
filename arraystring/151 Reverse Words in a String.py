"""
43ms
Beats 37.98%of users with Python3

16.30MB
Beats 72.81%of users with Python3
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        # s = [i for i in s if len(i)>0]
        left, right = 0, len(s) - 1
        while left < right:
            # print(left)
            s[left], s[right]=  s[right], s[left]
            left +=1
            right -=1
        return " ".join(s)


if __name__ == '__main__':
    s = "the sky is blue"
    res = Solution().reverseWords(s)
    print(res)
    assert "blue is sky the"