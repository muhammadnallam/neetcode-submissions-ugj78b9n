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
            else:
                try:
                    if pairs[c] == opened[-1]:
                        opened.pop()
                    else:
                        return False
                except IndexError:
                    return False
                except KeyError:
                    return False
            
        return len(opened) == 0
