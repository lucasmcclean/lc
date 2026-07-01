class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        mx = mn = 1

        for num in nums:
            pmx = mx * num
            pmn = mn * num
            mx = max(pmx, pmn, num)
            mn = min(pmx, pmn, num)

            res = max(res, mx)

        return res
