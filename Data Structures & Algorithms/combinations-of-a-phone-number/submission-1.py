class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2": "abc", 
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        op = []
        if not digits:
            return op

        def backtrack(i, resp):
            if len(resp) == len(digits):
                op.append("".join(resp))
                return 
            for c in map[digits[i]]:
                resp.append(c)
                print(i, c, resp, op)
                backtrack(i+1, resp)
                resp.pop()

        backtrack(0, [])
        return op