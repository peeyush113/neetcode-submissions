class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, 0
        curr_sum = 0
        resp = 0

        while r<len(arr):
            curr_sum += arr[r]
            if r-l>=k-1:
                avg = curr_sum/k
                if avg >= threshold:
                    resp += 1
                print(l, r, curr_sum, resp, avg)
                curr_sum -= arr[l]
                l += 1
            r += 1
        return resp
