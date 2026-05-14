class Solution:
    
    def encode(self, strs: List[str]) -> str:
        resp = ""
        
        for s in strs:
            sl = str(len(s))
            while len(sl)<3:
                sl  = "0"+sl
            resp += sl+s
        print(resp)
        return resp

    def decode(self, s: str) -> List[str]:
        resp = []
        i = 0
        while i<len(s):
            n = int(s[i:i+3])
            i = i+3
            resp.append(s[i:n+i])
            i = n + i
        return resp


