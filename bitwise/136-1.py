class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda a, x: a ^ x, nums)
