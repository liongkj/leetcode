# Definition for singly-linked list.
"""
34ms
Beats 94.03%of users with Python3

17.76MB
Beats 89.37%of users with Python3

1. [ ] -> [ current (head) ]
2. [ ] -> [ current (head) ]  [ next_node ]
3. [ prev ] <- [ current (head) ] [ next_node ]
4. [ ] <- [ current (head) ] <- [ prev ]
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current

            current = next_node
        return prev
    

if __name__ == "__main__":
    head = [1,2,3,4,5]
    res = Solution().reverseList(head)

    assert res == [5,4,3,2,1]
