class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "$" + s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        length = ""
        strs = []

        i = 0
        while i < len(s):
            text = ""

            if s[i].isdigit():
                length += s[i]
            elif s[i] == "$":
                for j in range(i+1, i+int(length)+1):
                    text += s[j]
                i = i+int(length)
                length = ""
                strs.append(text)

            i += 1

        return strs