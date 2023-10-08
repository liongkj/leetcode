"""
41ms
Beats 30.30%of users with Python3

16.18MB
Beats 81.12%of users with Python3
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        holder = [0] * (n - 2)
        holder = [0,1 ,1] + holder
        for i in range(3,len(holder)):
            # print(i)
            holder[i] = holder[i-1] + holder[i-2] + holder[i-3]
            # print(holder)
        return holder[-1]