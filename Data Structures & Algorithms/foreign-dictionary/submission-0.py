class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words)-1):
            p, pl, q, ql = words[i], len(words[i]), words[i+1], len(words[i+1])
            minLen = min(pl, ql)
            if pl>ql and p[:minLen] == q[:minLen]:
                return ""
            
            for j in range(minLen):
                if p[j] != q[j]:
                    adj[p[j]].add(q[j])
                    break
                
            
        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for ng in adj[char]:
                if dfs(ng):
                    return True
            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""
        
        res.reverse()
        return "".join(res)