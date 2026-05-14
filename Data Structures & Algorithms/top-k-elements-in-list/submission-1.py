class Solution:

    def quickSort(self, arr):
        def helper(s, e):
            if e-s+1<1:
                return 
            
            p = arr[e]
            l = s
            for i in range(s, e):
                if arr[i][1] > p[1]:
                    tmp = arr[l]
                    arr[l] = arr[i]
                    arr[i] = tmp
                    l += 1
            arr[e] = arr[l]
            arr[l] = p

            helper(s, l-1)
            helper(l+1, e)
            return
        helper(0, len(arr)-1)
        return arr

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}
        for n in nums:
            hMap.setdefault(n, 0)
            hMap[n] += 1
        resp = []
        
        for key, val in self.quickSort(list(hMap.items())):
            resp.append(key)
            k -= 1
            if k == 0:
                break
        return resp