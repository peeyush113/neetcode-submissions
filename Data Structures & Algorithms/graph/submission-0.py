class Graph:
    
    def __init__(self):
        self.adj = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj:
            self.adj[src] = []
        if dst not in self.adj:
            self.adj[dst] = []
        self.adj[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
                
        if src in self.adj and dst in self.adj[src]:
            self.adj[src].remove(dst)
            return True    
        return False

    def dfs(self, src, dst, visited):
        for n in self.adj[src]:
            if n == dst:
                return True
            
            if n in visited:
                return False
            
            visited.add(n)
            if self.dfs(n, dst, visited):
                return True
        
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        if src == dst:
            return True

        visited = set()
        visited.add(src)
        if self.dfs(src, dst, visited):
            return True
        return False


