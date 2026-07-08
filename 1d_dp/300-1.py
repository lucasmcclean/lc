class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        def bin_search(n: int) -> int:
            l, r = 0, len(res) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if res[mid] < n:
                    l = mid + 1
                elif res[mid] > n:
                    r = mid - 1
                else:
                    return mid
            return l

        for n in nums:
            if not res or n > res[-1]:
                res.append(n)
                continue
            i = bin_search(n)
            res[i] = n

        return len(res)
