"""
53ms
Beats 8.15%of users with Python3

16.31MB
Beats 22.85%of users with Python3
"""
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a = []
        for i, c in enumerate(candies):
            if c+extraCandies >= max(candies):
                a.append(True)
            else:
                a.append(False)
        return a
