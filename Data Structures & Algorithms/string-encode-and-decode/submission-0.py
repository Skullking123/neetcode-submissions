class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for word in strs:
            encoding = "".join([encoding, str(len(word)), "&", word])
        print(encoding)
        return encoding

    def decode(self, s: str) -> List[str]:
        decoding = []
        if len(s) > 0:
            index = 0
            # keep going until the end of the encoding
            while index < len(s):
                lengthStr = ""

                # get the length of the string
                while s[index] != "&":
                    lengthStr = lengthStr + s[index]
                    index = index + 1
                
                length = int(lengthStr)
                index = index + 1 # skip seperator
                end = index + length
                word = ""
                # get the word
                while index < end:
                    word = word + s[index]
                    index = index + 1
                index = end
                print(word)

                # append the word into our decoding
                decoding.append(word)

        return decoding

