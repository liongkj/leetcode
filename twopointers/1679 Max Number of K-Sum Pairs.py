from collections import Counter
from typing import List

"""
549ms
Beats 78.00%of users with Python3

28.56MB
Beats 85.23%of users with Python3

narrow search space when equal
if smaller then left move to the right, because number is sorted
"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev, next = 0,len(nums)-1
        count = 0
        while next > prev:
            if nums[prev] + nums[next] == k:
                count+=1
                next-=1
                prev+=1
            elif nums[prev] + nums[next] < k:
                prev+=1
            else:
                next -=1
        return count
            



if __name__ == "__main__":
    nums = [1,2,3,4]
    k = 5
    res = Solution().maxOperations(nums=nums,k=k)
    assert res == 2, "wrong answer"
    print("yay")