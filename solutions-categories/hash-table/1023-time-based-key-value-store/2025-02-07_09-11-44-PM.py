class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append([value, timestamp])
        else:
            self.d[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        out = ""
        if key not in self.d:
            return out
        l, r = 0, len(self.d[key]) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.d[key][mid][1] == timestamp:
                return self.d[key][mid][0]
            elif self.d[key][mid][1] < timestamp:
                out = self.d[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return out


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
