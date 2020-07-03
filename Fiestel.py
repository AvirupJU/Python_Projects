import random

test_str = str(input())
def Fiestel(s):
    converted = str(''.join(format(ord(i), 'b') for i in s))
#print(converted)


    def key_gen(l):
        res=""
        for i in range(l):
            temp = random.randint(0, 1)
            temp = str(temp)
            res = res + temp

        return res


    n = len(converted)//2


    def exor(a,b):
        temp = ""

        for i in range(n):

            if a[i] == b[i]:
                temp += "0"

            else:
                temp += "1"

        return temp


    key1 = key_gen(n)
    key2 = key_gen(n)

    L = converted[:n]
    R = converted[n:]

#first round of ciphering
    L1= R
    R1= exor(L,exor(R,key1))

#second round of ciphering
    L2= R1
    R2= exor(L1,exor(R1,key2))

    cipher= L2+R2
    DL= L2
    DR= R2
    DL1= DR
    DR1= exor(DL,exor(DR,key2))
    DL2= DR1
    DR2= exor(DL1,exor(DR1,key1))
    decipher= DL2+DR2

    def decode_binary_string(s):
        return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))


    c_text = decode_binary_string(cipher)
    #dc_text= decode_binary_string(decipher)
    return c_text

print(Fiestel(test_str))
