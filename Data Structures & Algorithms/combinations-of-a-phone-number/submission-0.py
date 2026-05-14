class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitMap = {"2": "abc", 
                    "3": "def",
                    "4": "ghi", 
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"}

        resp = []
        k = len(digits)
        def backtracking(i, cur):
            print(i, cur, resp)
            if len(cur) == k:
                resp.append("".join(cur))
                return
            
            if i > k:
                return
            
            for j in digitMap[digits[i]]:
                cur.append(j)
                backtracking(i+1, cur)
                cur.pop()
        
        backtracking(0, [])
        return resp