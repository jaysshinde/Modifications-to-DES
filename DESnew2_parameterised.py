import getpass
import time, string, random

# Initial permut matrix for the datas
PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Initial permut made on the key
CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]
# Permut applied on shifted key to get Ki+1
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

# Expand matrix to get a 48bits matrix of datas to apply the xor with Ki
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# SBOX
S_BOX = [

    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]

# Permut made after each SBox substitution for each round
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

# Final permut for datas after the 16 rounds
PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

# Matrix that determine the shift for each round of keys
SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def string_to_bit_array(text):  # Convert a string into a list of bits
    array = list()
    for char in text:
        binval = binvalue(char, 8)  # Get the char value on one byte
        array.extend([int(x) for x in list(binval)])  # Add the bits to the final list
    return array


def bit_array_to_string(array):  # Recreate the string from the bit array
    res = ''.join([chr(int(y, 2)) for y in [''.join([str(x) for x in bytes]) for bytes in nsplit(array, 8)]])
    return res


def binvalue(val, bitsize):  # Return the binary value as a string of the given size
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0" + binval  # Add as many 0 as needed to get the wanted size
    return binval


def nsplit(s, n):  # Split a list into sublists of size "n"
    return [s[k:k + n] for k in xrange(0, len(s), n)]


ENCRYPT = 1
DECRYPT = 0


class des():
    def __init__(self):
        self.password1 = None
        self.password2 = None
        self.text = None
        self.text1 = None
        self.text2 = None
        self.keys1 = list()
        self.keys2 = list()

    def run(self, key, text, action=ENCRYPT, padding=False):
        if len(key) != 16:
            raise "Key Should be 16 bytes long"
        elif len(key) == 16:
            key1 = key[:8]  # If key size is above 8bytes, cut to be 8bytes long
            key2 = key[8:]

        self.password1 = key1
        self.password2 = key2

        self.text1 = text[:8]
        self.text2 = text[8:]

        '''
        if padding and action == ENCRYPT:
            self.addPadding()
        elif len(self.text) % 8 != 0:  # If not padding specified data size must be multiple of 8 bytes
            raise "Data size should be multiple of 8"
        '''
        self.generatekeys()  # Generate all the keys    l-> keys1   r-> keys2
        text_blocks1 = nsplit(self.text1, 8)  # Split the text in blocks of 8 bytes so 64 bits
        text_blocks2 = nsplit(self.text2, 8)  # Split the text in blocks of 8 bytes so 64 bits

        result1 = list()
        result2 = list()
        #for block in text_blocks:  # Loop over all the blocks of data
        for l in range(len(text_blocks1)):
            block1 = text_blocks1[l]
            block2 = text_blocks2[l]
            block1 = string_to_bit_array(block1)  # Convert the block in bit array
            block2= string_to_bit_array(block2)  # Convert the block in bit array


            block1 = self.permut(block1, PI)  # Apply the initial permutation
            block2 = self.permut(block2, PI)  # Apply the initial permutation

            g1, d1 = nsplit(block1, 32)  # g(LEFT), d(RIGHT)
            g2, d2 = nsplit(block2, 32)  # g(LEFT), d(RIGHT)

            tmp1 = None
            tmp2 = None
            for i in range(16):  # Do the 16 rounds
                d_e1 = self.expand(d1, E)  # Expand d to match Ki size (48bits)
                d_e2 = self.expand(d2, E)  # Expand d to match Ki size (48bits)
                if action == ENCRYPT:
                    tmp1 = self.xor(self.keys1[i], d_e1)  # If encrypt use Ki
                    tmp2 = self.xor(self.keys2[i], d_e2)
                else:
                    tmp1 = self.xor(self.keys1[15 - i], d_e1)  # If decrypt start by the last key
                    tmp2 = self.xor(self.keys2[15 - i], d_e2)  # If decrypt start by the last key

                tmp1 = self.substitute(tmp1)  # Method that will apply the SBOXes
                tmp2 = self.substitute(tmp2)  # Method that will apply the SBOXes

                tmp1 = self.permut(tmp1, P)
                tmp2 = self.permut(tmp2, P)

                tmp1 = self.xor(g1, tmp1)
                tmp2 = self.xor(g2, tmp2)


                g1 = d1
                g2 = d2
                d1 = tmp1
                d2 = tmp2

            # g1 , d1 = d1 , g1
            # g2 ,d2 = d2, g2

            result1 += self.permut(d1 + g1, PI_1)  # Do the last permut and append the result to result
            result2 += self.permut(d2 + g2, PI_1)  # Do the last permut and append the result to result

        result = result1 + result2
        final_res = bit_array_to_string(result)
        if padding and action == DECRYPT:
            return self.removePadding(final_res)  # Remove the padding if decrypt and padding is true
        else:
            return final_res  # Return the final string of data ciphered/deciphered

    def substitute(self, d_e):  # Substitute bytes using SBOX
        subblocks = nsplit(d_e, 6)  # Split bit array into sublist of 6 bits
        result = list()
        for i in range(len(subblocks)):  # For all the sublists
            block = subblocks[i]
            row = int(str(block[0]) + str(block[5]), 2)  # Get the row with the first and last bit
            column = int(''.join([str(x) for x in block[1:][:-1]]), 2)  # Column is the 2,3,4,5th bits
            val = S_BOX[i][row][column]  # Take the value in the SBOX appropriated for the round (i)
            bin = binvalue(val, 4)  # Convert the value to binary
            result += [int(x) for x in bin]  # And append it to the resulting list
        return result

    def permut(self, block, table):  # Permut the given block using the given table (so generic method)
        return [block[x - 1] for x in table]

    def expand(self, block, table):  # Do the exact same thing than permut but for more clarity has been renamed
        return [block[x - 1] for x in table]

    def xor(self, t1, t2):  # Apply a xor and return the resulting list
        return [x ^ y for x, y in zip(t1, t2)]

    def generatekeys(self):  # Algorithm that generates all the keys
        self.keys1 = []
        self.keys2 = []
        key1 = string_to_bit_array(self.password1)
        key2 = string_to_bit_array(self.password2)
        key1 = self.permut(key1, CP_1)  # Apply the initial permut on the key
        key2 = self.permut(key2, CP_1)  # Apply the initial permut on the key

        g1, d1 = nsplit(key1, 28)  # Split it in to (g->LEFT),(d->RIGHT)
        g2, d2 = nsplit(key2, 28)  # Split it in to (g->LEFT),(d->RIGHT)

        for i in range(16):  # Apply the 16 rounds
            g1, d1 = self.shift(g1, d1, SHIFT[i])  # Apply the shift associated with the round (not always 1)
            g2, d2 = self.shift(g2, d2, SHIFT[i])  # Apply the shift associated with the round (not always 1)

            tmp1 = g1 + d1  # Merge them
            tmp2 = g2 + d2  # Merge them

            self.keys1.append(self.permut(tmp1, CP_2))  # Apply the permut to get the Ki
            self.keys2.append(self.permut(tmp2, CP_2))  # Apply the permut to get the Ki

        self.swap_keys()


    def swap_keys(self):
        for i in range(1,len(self.keys1)):
            self.keys1[i] , self.keys2[i] = self.keys2[i],self.keys1[i]

    def shift(self, g, d, n):  # Shift a list of the given value
        return g[n:] + g[:n], d[n:] + d[:n]

    def addPadding(self):  # Add padding to the datas using PKCS5 spec.
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len)

    def removePadding(self, data):  # Remove the padding of the plain text (it assume there is padding)
        pad_len = ord(data[-1])
        return data[:-pad_len]

    def encrypt(self, key, text, padding=False):
        return self.run(key, text, ENCRYPT, padding)

    def decrypt(self, key, text, padding=False):
        return self.run(key, text, DECRYPT, padding)

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#if __name__ == '__main__':
def main():
    #key = raw_input("Enter key: ")
    key = id_generator(16)
    #text = raw_input("Enter text: ")
    l = list()
    n = input("Enter number of test cases:")
    for i in range(n):
        l.append(id_generator(16))
    d = des()
    start = time.time()
    for i in range(n):
        r = d.encrypt(key,l[i], False)
        r2 = d.decrypt(key, r, False)

    end = time.time()
    # print "Ciphered: %r" %r
    # print "Deciphered: %r" % r2
    print "Time Taken = " ,end - start, " seconds"


main()
