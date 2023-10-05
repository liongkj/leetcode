"""
Runtime
23ms
Beats 99.68%of users with Python3

Memory
16.14MB
Beats 86.60%of users with Python3
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = [*word1]
        b = [*word2]
        res = []
        min_len = min(len(a),len(b))
        for i in zip(a,b):
            res.extend(i)
        if len(a) != len(b):
            if len(a)>len(b):
                res.extend(a[min_len:])
            else:
                res.extend(b[min_len:])
        return "".join(res)
    
if __name__ == '__main__':
    word1 = "abc"
    word2 = "pqr"
    print(Solution().mergeAlternately(word1,word2))