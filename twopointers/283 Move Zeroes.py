from typing import List

"""
138ms
Beats 86.88%of users with Python3

17.80MB
Beats 71.69%of users with Python3
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left],nums[right] = nums[right], nums[left]
                left += 1
            right+=1
        print(nums)
        return nums

if __name__ == '__main__':
    nums = [0,1,0,3,12]
    res = Solution().moveZeroes(nums)
    assert res == [1,3,12,0,0]