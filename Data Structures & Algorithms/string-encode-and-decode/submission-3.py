class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for word in strs:
            seperator = f"{len(word)}&>"
            res += f"{seperator}{word}"
        print(f"encoded: {res}")
        return res

    def decode(self, s: str) -> List[str]:

        index = 0
        res = []
        while index < len(s):
            length = "" # length of decoded str
            while s[index].isnumeric():
                length += s[index]
                index += 1
            print(f"length: {length}")
            
            length = int(length) # convert length to int
            index += 2 # skip over the seperator
            print(f"start: {index}")
            word = ""
            for letter in range(length):
                word += s[index]
                index += 1
            res.append(word)
            print(f"end: {index}")
        print(f"decoded: {res}")
        return res
            
