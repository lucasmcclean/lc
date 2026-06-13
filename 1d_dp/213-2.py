class Solution:
    def rob(self, nums: List[int]) -> int:

        def find_max(nums):
            pre, res = 0, 0

            for cur in nums:
                tmp = max(res, pre + cur)
                pre = res
                res = tmp

            return res

        return max(find_max(nums[:-1]), find_max(nums[1:]), nums[0])
