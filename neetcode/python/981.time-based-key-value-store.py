#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(lambda: [])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        if len(values) == 0:
            return ""

        if values[0][1] > timestamp:
            return ""

        if values[-1][1] <= timestamp:
            return values[-1][0]

        if len(values) == 1 and values[0][1] < timestamp:
            return values[0][0]

        low = 0
        high = len(values) - 1
        mid = low + (high - low) // 2
        if values[mid][1] == timestamp:
            return values[mid][0]
        elif values[mid][1] > timestamp:
            #search_left()
            for i in range(mid, low-1, -1):
                if values[i][1] <= timestamp:
                    return values[i][0]
                else:
                    continue
        else:
            #search_right()
            for i in range(mid, high+1, 1):
                if values[i][1] > timestamp:
                    return values[i-1][0]
                else:
                    continue
        return ""
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

