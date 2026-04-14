class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        res = []
        for l in range(len(nums)):
            if l != 0 and nums[l] == nums[l - 1]:
                continue

            m, r = l + 1, len(nums) - 1
            while m < r:
                total = nums[l] + nums[m] + nums[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    m += 1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    while m < r and nums[m] == nums[m - 1]:
                        m += 1

        return res
