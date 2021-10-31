class EncryptionHelper:
    @staticmethod
    def GetEncryptedString(text, key = 3):
        encrypted = ""

        for c in text:
            if c.isupper():  # check if it's an uppercase character
                c_index = ord(c) - ord('A')
                # shift the current character by key positions
                c_shifted = (c_index + key) % 26 + ord('A')
                c_new = chr(c_shifted)
                encrypted += c_new
            elif c.islower():  # check if its a lowecase character
                # subtract the unicode of 'a' to get index in [0-25) range
                c_index = ord(c) - ord('a')
                c_shifted = (c_index + key) % 26 + ord('a')
                c_new = chr(c_shifted)
                encrypted += c_new

            elif c.isdigit():
                # if it's a number,shift its actual value
                c_new = (int(c) + key) % 10
                encrypted += str(c_new)
            else:
                # if its neither alphabetical nor a number, just leave it like that
                encrypted += c

        return encrypted

    @staticmethod
    def GetDecryptedString(text, key = 3):
        decrypted = ""
        for c in text:
            if c.isupper():
                c_index = ord(c) - ord('A')
                # shift the current character to left by key positions to get its original position
                c_og_pos = (c_index - key) % 26 + ord('A')
                c_og = chr(c_og_pos)
                decrypted += c_og
            elif c.islower():
                c_index = ord(c) - ord('a')
                c_og_pos = (c_index - key) % 26 + ord('a')
                c_og = chr(c_og_pos)
                decrypted += c_og
            elif c.isdigit():
                # if it's a number,shift its actual value
                c_og = (int(c) - key) % 10
                decrypted += str(c_og)
            else:
                # if its neither alphabetical nor a number, just leave it like that
                decrypted += c
        return decrypted

    @staticmethod
    def GetDecryptedTuple(encryptedTuple):
        valuesList = []
        for encryptedValue in encryptedTuple:
            valuesList.append(EncryptionHelper.GetDecryptedString(str(encryptedValue)))
        return tuple(valuesList)

    @staticmethod
    def GetEncryptedTuple(decryptedTuple):
        valuesList = []
        for value in decryptedTuple:
            valuesList.append(EncryptionHelper.GetEncryptedString(str(value)))
        return tuple(valuesList)


    # def decryptNestedTupleToNestedList(self, tupple):
    #     newList = []
    #     for t in tupple:
    #         newList.append(self.decryptTupleToList(t))
    #     return newList






    print()