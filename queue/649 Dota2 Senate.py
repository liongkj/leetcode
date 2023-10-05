"""
48ms
Beats 92.20%of users with Python3

16.62MB
Beats 45.83%of users with Python3

create list of index based on the turns
if radiant turn is later than dire, add dire turn to the last of queue 
"""

from collections import deque


class Solution:
    def predictPartyVictory(self,senate: str) -> str:
        radiant_queue = deque()
        dire_queue = deque()

        for i, party in enumerate(senate):
            if party == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        while radiant_queue and dire_queue:
            radiant_senator = radiant_queue.popleft()
            dire_senator = dire_queue.popleft()

            if radiant_senator < dire_senator:
                radiant_queue.append(radiant_senator + len(senate))
            else:
                dire_queue.append(dire_senator + len(senate))

        return "Radiant" if radiant_queue else "Dire"
