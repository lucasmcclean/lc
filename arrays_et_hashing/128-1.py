class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)

        for num in nums:
            if num - 1 in nums:
                continue

            next_num = num + 1
            while next_num in nums:
                next_num += 1
            longest = max(longest, next_num - num)

        return longest
