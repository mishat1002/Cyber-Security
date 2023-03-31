#CIPHER TEXT ENCRYPTION
def encryption(plain_text, key):
    cipher_test = ""

    for i in range(len(plain_text)):

        char = plain_text[i]
        if (char.isupper()):
            cipher_test = cipher_test + chr((ord(char) + key - 65) % 26 + 65)
        elif (char.islower()):
            cipher_test = cipher_test + chr((ord(char) + key -97) % 26 + 97)
        else:
            continue

    return cipher_test
plain_text = input('Write your massage: ')
key = int(input('Enter you encryption + decryption key: '))
cipher_text = encryption(plain_text,key)
print("Your Text is: " , plain_text)
print("Your Encryption key is: " , key)
print("Your Cipher Text is: " , cipher_text)
