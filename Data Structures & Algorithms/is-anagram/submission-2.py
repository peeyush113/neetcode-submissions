class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        for n in s:
            hashMap.setdefault(n, 0)
            hashMap[n] += 1

        for n in t:
            v = hashMap.get(n, 0)
            if v == 0:
                return False
            v = v -1 
            if v == 0:
                del hashMap[n]
            else:
                hashMap[n] = v
        return len(hashMap)<=0 