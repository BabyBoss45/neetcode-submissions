class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for i in range (len(strs)):
            length = len(strs[i])
            encoded.append(str(length) + "#" + strs[i]) 


        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1

            word = s[start:start + length]
            decoded.append(word)

            i = start + length

        return decoded