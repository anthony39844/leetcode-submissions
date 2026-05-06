class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [(timestamp, value)]
        else:
            self.d[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        
        x = self.d[key]
        l, r = 0, len(x) - 1
        while l <= r:
            m = (l + r) // 2
            if x[m][0] == timestamp:
                return x[m][1]
            elif x[m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1
        print(timestamp )
        m = (l + r) // 2
        return x[m][1] if x[m][0] <= timestamp else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
