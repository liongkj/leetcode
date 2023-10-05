# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
"""
34ms
Beats 78.03%of users with Python3

16.13MB
Beats 83.86%of users with Python3
"""
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1,n
        while left <=right:

            myguess = left + (right - left) / 2
            res = guess(myguess)
            if res == 0:
                return int(myguess)
            if res == 1: # too low, guess higher
                left = myguess
            else:
                right = myguess

if __name__ == "__main__":
    n = 10
    pick = 6