import re
def mapping(characters_frequencies, most_common_letters_in_the_alphabet):
    characters_frequencies = dict(sorted(characters_frequencies.items(), key=lambda item: item[1], reverse=True))
    stack = list(most_common_letters_in_the_alphabet.keys())
    for char in characters_frequencies:
        if len(stack) == 0:
            break
        most_common_letters_in_the_alphabet[stack.pop(0)] = char

    most_common_letters_in_the_alphabet = {v:k for k, v in most_common_letters_in_the_alphabet.items()}

    return most_common_letters_in_the_alphabet

def summarize():
    print('\n\nSummary:')
    print('''
          First I created a Dictionary that holds the most common letters to the least common letters in the alphabet.Originally in the homework, 
          there was a table that showed the same dictionary but the value for each character had a decimal distribution.Instead in 
          most_common_letters_in_the_alphabet, each character is assigned a space because we want to fill it up with the frequency of the characters
          in the text.That is why a new characters_frequencies gets made that keeps track of the frequency of the letter. Afterward, we sort the 
          characters_frequencies by the value and start matching it with the most_common_letters_in_the_alphabet dictionary, by replacing the space. 
          Afterward, every character from the text gets replaced by searching the most_common_letters_in_the_alphabet and replacing it with the value 
          and this decodes the message.''')

def problem1():
    cipher_text = "ROYQWH KQXXJYQ: N LQGNQAQ HDJH FO. VW NX J KQKLQO VZ J XQMOQH MONKQ VOYJWNSJHNVW MJGGQF U.D.J.W.H.V.K., IDVXQ YVJG NX HVHJG IVOGF FVKNWJHNVW. HDQNO UGJW NX HV JMBRNOQ J XRUQOIQJUVW JWF HV DVGF HDQ IVOGF OJWXVK. N JK JZOJNF HDJH IQ FV WVH DJAQ KRMD HNKQ LQZVOQ HDQT XRMMQQF.\nN DJAQ OQMQWHGT NWHQOMQUHQF JW QWMOTUHQF KQXXJYQ (JHHJMDKQWH MNUDQO2.HCH) HDJH IJX XQWH LT FO. VW HV VWQ VZ DNX MVWXUNOJHVOX, HDQ NWZJKVRX KO. LGVIZNQGF. N KJWJYQF HV FNXMVAQO HDJH HDQ KQXXJYQ IJX QWMOTUHQF RXNWY HDQ PJMEJG MNUDQO (XQQ XVROMQ MVFQ), LRH N IJX WVH JLGQ FNXMVAQO HDQ XQMOQH EQT, JWF HDQ MNUDQO XQQKX HV LQ RWLOQJEJLGQ. N JK JZOJNF HDJH FQMOTUHNWY HDNX KQXXJYQ NX HDQ VWGT IJT HV XHVU FO. VW'X VOYJWNSJHNVW.\nUGQJXQ XQWF OQNWZVOMQKQWHX NKKQFNJHQGT! N HONQF HV JMH MJRHNVRXGT, LRH N DJAQ J ZQQGNWY HDJH FO. VW'X DQWMDKQW JOQ VWHV KQ. N FVW'H EWVI DVI GVWY N DJAQ LQZVOQ HDQT FNXMVAQO KT OQJG NFQWHNHT JWF KT XQMOQH DNFNWY UGJ"
    most_common_letters_in_the_alphabet = {
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

    characters_frequencies = {}
    for char in cipher_text:
        if not char.isalpha():
            continue
        characters_frequencies[char] = characters_frequencies.get(char, 0) + 1

    print(f"Frequency Table:")
    for char, frequency in characters_frequencies.items():
        print(f"{char}: {frequency}")
    
    most_common_letters_in_the_alphabet = mapping(characters_frequencies,most_common_letters_in_the_alphabet)
    
    for char in range(len(cipher_text)):
        if cipher_text[char] in most_common_letters_in_the_alphabet:
            cipher_text = cipher_text[:char] + most_common_letters_in_the_alphabet[cipher_text[char]] + cipher_text[char+1:]
    print(f"\nDecoded Ciphertext:\n {cipher_text}")
    summarize()


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