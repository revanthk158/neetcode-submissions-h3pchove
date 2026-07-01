class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0
        for i in nums:
            if i == 0:
                res = max(res, cnt)
                cnt = 0
            else:
                cnt  = cnt + 1
        return max(res, cnt)
        