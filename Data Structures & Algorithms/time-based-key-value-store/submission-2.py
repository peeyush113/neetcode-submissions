class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap.setdefault(key, []).append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap.get(key, [])
        resp = ""
        l, r = 0, len(values)-1
        while l <= r:
            m = (l+r)//2
            left, right, mid = values[l][0], values[r][0], values[m][0]
            
            if timestamp > mid:
                l = m +1
                resp = values[m][1] 
            elif timestamp < mid:
                r = m -1 
            else:
                return values[m][1]
            print(l,":",left, m,":",mid, r,":",right, values)
        
        return resp
