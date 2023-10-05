"""
228ms
Beats 46.86%of users with Python3

21.46MB
Beats 76.91%of users with Python3
"""

class RecentCounter:

    def __init__(self):
        self.request_queue = []

    def ping(self, t: int) -> int:
        while self.request_queue and self.request_queue[0] < t - 3000:
            self.request_queue.pop(0)
        self.request_queue.append(t)
        return len(self.request_queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

if __name__ == "__main__":
    input = [[], [1], [100], [3001], [3002]]
    obj =  RecentCounter()
    for i in input:
        res =obj.ping(i)
    # [null, 1, 2, 3, 3]