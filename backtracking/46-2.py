class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums.copy()]

        permutations = []

        for _ in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(num)

            permutations.extend(perms)
            nums.append(num)

        return permutations
