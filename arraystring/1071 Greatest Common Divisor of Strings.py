"""
Runtime
64ms
Beats 5.68%of users with Python3

16.65MB
Beats 6.77%of users with Python3
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_len = min(len(str1),len(str2))
        if min_len == 0:
            return ""
        print(min_len)
        for i in range(min_len+1,0,-1):
            if len(str1) > len(str2):
                cand = str1[:i]
            else:
                cand = str2[:i]
            print(cand)
            cand_len = len(cand)
            print(cand_len)
            multiplier1 = int(len(str1) / cand_len)
            print("")
            print("multiplier1",multiplier1)
            multiplier2 = int(len(str2) / cand_len)
            print("multiplier2",multiplier2)

            if multiplier1 * cand == str1 and  multiplier2 * cand == str2:
                return cand
        else:
            return ""
        
if __name__ == '__main__':
    str1= "ABCABC"
    str2 = "ABC"
    print(Solution().gcdOfStrings(str1,str2))