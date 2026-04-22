class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        l, r = 0, m

        while l <= r:
            pm = l + (r - l) // 2
            pn = (m + n + 1) // 2 - pm

            mxlm = float('-inf') if pm == 0 else nums1[pm - 1]
            mnrm = float('inf') if pm == m else nums1[pm]

            mxln = float('-inf') if pn == 0 else nums2[pn - 1]
            mnrn = float('inf') if pn == n else nums2[pn]

            if mxlm <= mnrn and mxln <= mnrm:
                if (m + n) % 2 == 0:
                    return (max(mxlm, mxln) + min(mnrm, mnrn)) / 2
                else:
                    return max(mxlm, mxln)
            elif mxlm > mnrn:
                r = pm - 1
            else:
                l = pm + 1
