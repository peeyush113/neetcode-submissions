class Solution:
    def simplifyPath(self, path: str) -> str:
        valid_path = []
        for s in path.split("/"):
            if s in ["/", "//", "///", ".", ""]:
                continue
            
            if s == "..":
                if valid_path:
                    valid_path.pop()
                continue
            valid_path.append(s)
        print(valid_path)
        return "/"+"/".join(valid_path)