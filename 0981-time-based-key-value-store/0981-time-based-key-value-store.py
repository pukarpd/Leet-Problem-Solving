class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ''
        
        if timestamp < self.timeMap[key][0][0]: 
            return ''
        keyArr = self.timeMap[key]
        # print(self.timeMap)
        l, r  = 0, len(keyArr) - 1 

        while l <= r:
            m = floor((l + r) //2)
            if keyArr[m][0] < timestamp: 
                l = m + 1 
            elif keyArr[m][0] > timestamp: 
                r = m - 1 
            else: 
                return keyArr[m][1]

        return keyArr[r][1]
            



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)