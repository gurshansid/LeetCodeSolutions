class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap:
            self.hmap[key].append((value, timestamp))
        else:
            self.hmap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        
        left = 0
        right = len(self.hmap[key]) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if self.hmap[key][mid][1] <= timestamp:
                result = self.hmap[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return result
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)