class Solution:
    def rob(self, nums: List[int]) -> int:
        pre, res = 0, 0

        for cur in nums:
            tmp = max(res, pre + cur)
            pre = res
            res = tmp

        return res
