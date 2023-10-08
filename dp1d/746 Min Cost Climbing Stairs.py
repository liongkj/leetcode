"""
62ms
Beats 51.88%of users with Python3

16.42MB
Beats 54.35%of users with Python3
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [10,15,20]
        # this is to check two steps ahead and save the min of both
        # holder = [0] * len(cost)
        # holder[0] = cost[0]
        # holder[1] = cost[1] 
        # for step in range(2, len(cost)):
        #     holder[step] = cost[step] + min(holder[step-1],holder[step-2])  
        # return min(holder[-1],holder[-2])
        """
        59ms
        Beats 68.72%of users with Python3

        16.43MB
        Beats 54.35%of users with Python3

        optimize it slightly by using two variables instead of an entire list to keep track of the minimum costs for the previous two steps.
        This optimization reduces the space complexity from O(N) to O(1). Here's an optimized version of your code
        """
        prev1 = cost[0]
        prev2 = cost[1] 
        for step in range(2, len(cost)):
            current = cost[step] + min(prev1,prev2)
            prev1,prev2 = prev2,current
        return min(prev1,prev2)