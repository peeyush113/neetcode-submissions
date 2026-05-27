class Solution:
    
    delimiter = "#"

    def encode(self, strs: List[str]) -> str:
        resp = ""
        for s in strs:
            resp += f"{len(s)}{self.delimiter}{s}"
        return resp 
        
    def decode(self, s: str) -> List[str]:
        resp = []
        strs = ""
        i = 0

        while i<len(s):
            strs = ""
            strs_len = ""
            while s[i] != self.delimiter:
                strs_len += s[i]
                i += 1
            i += 1
            strs_len = int(strs_len)
            for n in range(strs_len):
                strs += s[i]
                i += 1
            resp.append(strs)
        return resp
