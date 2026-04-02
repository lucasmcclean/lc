class Solution:
    def reverseBits(self, n: int) -> int:
        res, i = 0, 32

        while i > 0 and n > 0:
            res <<= 1
            res |= (n & 1)
            n >>= 1
            i -= 1

        return res << i
