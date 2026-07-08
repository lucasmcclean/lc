class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = dict()
        longest = 0

        for num in nums:
            prev = 1
            for k, v in res.items():
                if num > k:
                    prev = max(prev, v + 1)
            res[num] = max(res.get(num, 1), prev)
            longest = max(longest, prev)

        return longest
