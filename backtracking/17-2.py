class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        combinations = []
        cur = []

        def generate(idx: int = 0) -> None:
            if idx == len(digits):
                combinations.append("".join(cur))
                return

            for char in mapping[digits[idx]]:
                cur.append(char)
                generate(idx + 1)
                cur.pop()

        generate()
        return combinations
