class Solution:
    def encode(self, strs: List[str]) -> str:
        count = f"{len(strs):02d}"

        lens = []
        for s in strs:
            lens.append(f"{len(s):03d}")

        return count + "".join(lens) + "".join(strs)

    def decode(self, s: str) -> List[str]:
        res = []

        count = int(s[0:2])

        cur = 2 + count * 3
        for i in range(2, 2+ count * 3, 3):
            cur_len = int(s[i:i+3])
            res.append(s[cur:cur+cur_len])
            cur += cur_len

        return res
