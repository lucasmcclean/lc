class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        if m > n:
            m, n = n, m
            nums1, nums2 = nums2, nums1

        l, r = 0, m
        while l <= r:
            p1 = l + (r - l) // 2
            p2 = (m + n + 1) // 2 - p1

            l1 = float("-inf") if p1 == 0 else nums1[p1 - 1]
            r1 = float("inf") if p1 == m else nums1[p1]

            l2 = float("-inf") if p2 == 0 else nums2[p2 - 1]
            r2 = float("inf") if p2 == n else nums2[p2]

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                r = p1 - 1
            else:
                l = p1 + 1
