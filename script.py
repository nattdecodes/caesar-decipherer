
def cipher_decrypt(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        # UPPERCASE
        if c.isupper(): 
            c_index = ord(c) - ord('A')
            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        # lowercase
        elif c.islower(): 
            c_index = ord(c) - ord('a') 
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        else:
            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c
    return decrypted

def checkVocab(possibleMsg):
    hits = 0
    for word in possibleMsg[0].split():
        with open(r"caesar-decypherer\englishwords.txt", "r") as wEn:
            for line in wEn:
                if line.strip() == word.lower():
                    hits += 1
                    break # next word
                else:
                    continue # next line
    possibleMsg.append(hits) # format ["possible message", keynbr, hitsnbr]

def decryptAllCases(encryptedMsg):
    k = 25 # all possible keys
    possibleMsgs = []
    while k > 0:
        decryptedPossible = cipher_decrypt(encryptedMsg, k)
        possibleMsgs.append(decryptedPossible)
        possibleMsgs.append(k)
        k -= 1
    possibleMsgs = [possibleMsgs[x:x+2] for x in range(0, len(possibleMsgs), 2)]
    for possibleMsg in possibleMsgs:
        checkVocab(possibleMsg)
    possibleMsgs = sorted(possibleMsgs, key=lambda x:x[2], reverse=True)
    print(f"deciphered message > {possibleMsgs[0][0]}")
    print(f"key > {possibleMsgs[0][1]}")

decryptAllCases(input("caesar cipher to decipher > "))