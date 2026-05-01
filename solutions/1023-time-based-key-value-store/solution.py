class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        
        x = self.d[key]
        l, r = 0, len(x) - 1
        out = ""
        while l <= r:
            m = (l + r) // 2
            if x[m][0] <= timestamp:
                out = x[m][1]
                l = m + 1
            else:
                r = m - 1
        return out        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
