class Solution:
    def countBits(self, n: int) -> List[int]:
        op = []
        for i in range(n+1):
            count = 0
            k = i
            while k >0:
                if k&1==1:
                    count +=1 
                k = k>>1
            op.append(count)
        return op