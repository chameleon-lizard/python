alphabet = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_"""

def shex(n):
    if n < 64:
        return alphabet[n]
    else:
        return shex(n // 64) + alphabet[n % 64]

def xehs(s):
    byte_string = bytes(s, "ASCII")
    return sum(64 ** (len(byte_string) - i - 1) * (byte_string[i] - 32) for i in range(len(byte_string)))

print(228, shex(228), xehs(shex(228)))