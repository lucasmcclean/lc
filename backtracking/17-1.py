class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []

        numToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def generate(idx: int, cur: str):
            if idx == len(digits):
                combinations.append("".join(cur))
                return

            for char in numToChar[digits[idx]]:
                cur.append(char)
                generate(idx + 1, cur)
                cur.pop()

        generate(0, [])
        return combinations
