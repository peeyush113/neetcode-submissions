class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = [[]]

        for n in nums:
            localPerms = []
            for perm in perms:
                for i in range(len(perm)+1):
                    p = perm.copy()
                    p.insert(i, n)
                    localPerms.append(p)
            perms = localPerms
        return perms