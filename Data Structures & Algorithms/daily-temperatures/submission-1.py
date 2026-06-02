class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            tmp = temperatures[i]
            while stack:
                s = stack.pop()
                stmp = temperatures[s]
                if tmp>stmp:
                    res[s] = i-s
                else:
                    stack.append(s)
                    break
            stack.append(i)
        return res
