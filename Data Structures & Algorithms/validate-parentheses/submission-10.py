class Solution:
    def isValid(self, s: str) -> bool:
        # Simplest case: Odd-length strings cannot have perfectly balanced brackets
        if len(s) % 2 != 0:
            return False

        opened = []
        pairs = {"]":"[", "}":"{", ")":"("}

        for c in s:
            if c in "[({":
                opened.append(c)
            elif opened and pairs[c] == opened[-1]:
                opened.pop()
            else:
                return False
            
        return not opened
