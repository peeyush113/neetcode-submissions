class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        resp = []
        l = len(temperatures)
        for i in range(l):
            days = 0
            for j in range(i+1, l):
                if temperatures[j] > temperatures[i]:
                    days = j-i
                    print(i, j)
                    break
            resp.append(days)
        return resp