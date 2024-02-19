import re
import random
def problem1():
    cipher_text = "ROYQWH KQXXJYQ: N LQGNQAQ HDJH FO. VW NX J KQKLQO VZ J XQMOQH MONKQ VOYJWNSJHNVW MJGGQF U.D.J.W.H.V.K., IDVXQ YVJG NX HVHJG IVOGF FVKNWJHNVW. HDQNO UGJW NX HV JMBRNOQ J XRUQOIQJUVW JWF HV DVGF HDQ IVOGF OJWXVK. N JK JZOJNF HDJH IQ FV WVH DJAQ KRMD HNKQ LQZVOQ HDQT XRMMQQF.\nN DJAQ OQMQWHGT NWHQOMQUHQF JW QWMOTUHQF KQXXJYQ (JHHJMDKQWH MNUDQO2.HCH) HDJH IJX XQWH LT FO. VW HV VWQ VZ DNX MVWXUNOJHVOX, HDQ NWZJKVRX KO. LGVIZNQGF. N KJWJYQF HV FNXMVAQO HDJH HDQ KQXXJYQ IJX QWMOTUHQF RXNWY HDQ PJMEJG MNUDQO (XQQ XVROMQ MVFQ), LRH N IJX WVH JLGQ FNXMVAQO HDQ XQMOQH EQT, JWF HDQ MNUDQO XQQKX HV LQ RWLOQJEJLGQ. N JK JZOJNF HDJH FQMOTUHNWY HDNX KQXXJYQ NX HDQ VWGT IJT HV XHVU FO. VW'X VOYJWNSJHNVW.\nUGQJXQ XQWF OQNWZVOMQKQWHX NKKQFNJHQGT! N HONQF HV JMH MJRHNVRXGT, LRH N DJAQ J ZQQGNWY HDJH FO. VW'X DQWMDKQW JOQ VWHV KQ. N FVW'H EWVI DVI GVWY N DJAQ LQZVOQ HDQT FNXMVAQO KT OQJG NFQWHNHT JWF KT XQMOQH DNFNWY UGJ"
    probabilities = {
        'E': '',
        'T': '',
        'A': '',
        'O': '',
        'I': '',
        'N': '',
        'R': '',
        'S': '',
        'H': '',
        'D': '',
        'C': '',
        'M': '',
        'L': '',
        'P': '',
        'Y': '',
        'G': '',
        'U': '',
        'W': '',
        'B': '',
        'F': '',
        'V': '',
        'K': '',
        'Z': '',
        'J': '',
        'Q': '',
        'X': ''
    }

    freq = {}
    for char in cipher_text:
        if not char.isalpha():
            continue
        freq[char] = freq.get(char, 0) + 1

    freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    stack = list(probabilities.keys())
    for char in freq:
        if len(stack) == 0:
            break
        probabilities[stack.pop(0)] = char

    probabilities = {v:k for k, v in probabilities.items()}

    for char in range(len(cipher_text)):
        if cipher_text[char] in probabilities:
            cipher_text = cipher_text[:char] + probabilities[cipher_text[char]] + cipher_text[char+1:]
    print(cipher_text)


def JACKAL_Decrypt(firstKeyByte, secondKeyByte, cipherText):
# returns a plaintext bytearray 
    x = (firstKeyByte + 31)
    y = (secondKeyByte * 3)
    p = []
    for z in range(len(cipherText)):
        x = (x + 29) & 0xFF
        y = (y * 19) & 0xFF
        p.append(cipherText[z] ^ x ^ y)
    return bytearray(p)

def isEnglishText(byte):
    punctuations = ".,'-:{}"
    try:
        for char in byte.decode('utf-8'):
            if not (char.isalnum() or char.isspace() or char in punctuations):
                return False
    except UnicodeDecodeError as e:
        return False
    return True

def problem2():
    with open("cipher2.txt", "rb") as file:
        cipherText = file.read()
    plainText = ''
    for i in range(256):
        for j in range(256):
            plainText = JACKAL_Decrypt(i, j, cipherText)
            if isEnglishText(plainText):
                break
        if isEnglishText(plainText):
            break

    print(plainText.decode())


def problem3():
    with open("cipher3.txt", "rb") as file:
        cipher_text = file.read()

    key_phrase = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    plain_text = bytearray()
    for i in range(len(cipher_text)):
        plain_text.append(cipher_text[i] ^ key_phrase[i % 11])


    print(plain_text.decode('utf-8'))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n\nProblem 1 \n\n")
    problem1()
    print("\n\nProblem 2 \n\n")
    problem2()
    print("\n\nProblem 3 \n\n")
    problem3()