class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            strlen = res.append(f"{len(s):03d}")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0
        while idx < len(s):
            strlen = int(s[idx:idx+3])
            idx += 3
            res.append(s[idx:idx+strlen])
            idx += strlen
        return res
