class Solution:
    def encode(self, strs: list[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> list[str]:
        x = 0
        result = []
        while x < len(s):
            y = s.find("#", x)
            if y == -1:
                break
            length = int(s[x:y])
            result.append(s[y + 1 : y + 1 + length])
            x = y + 1 + length
        return result
