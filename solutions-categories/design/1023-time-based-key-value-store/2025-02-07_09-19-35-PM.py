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
        val = self.d[key]
        l, r = 0, len(val) - 1

        while l <= r:
            mid = (l + r) // 2
            if val[mid][1] == timestamp:
                return val[mid][0]
            elif val[mid][1] < timestamp:
                out = val[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return out


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
