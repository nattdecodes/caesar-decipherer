# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
def cipher_decrypt(ciphertext, key):
    decrypted = ""
    for char in ciphertext:
        # UPPERCASE
        if char.isupper():
            c_index = ord(char) - ord('A')
            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        # lowercase
        elif char.islower():
            c_index = ord(char) - ord('a')
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        else:
            # if its neither alphabetical nor a number, just leave it like that
            decrypted += char
    return decrypted

def check_vocab(possible_msg):
    hits = 0
    for word in possible_msg[0].split():
        with open(r"englishwords.txt", "r", encoding="utf8") as wl_en:
            for line in wl_en:
                if line.strip() == word.lower():
                    hits += 1
                    break # next word
                continue # else: next line
    possible_msg.append(hits) # format ["possible message", keynbr, hitsnbr]

def decrypt_all(encrypted_msg):
    k = 25 # all possible keys
    poss_msgs = []
    while k > 0:
        decrypted_possible = cipher_decrypt(encrypted_msg, k)
        poss_msgs.append(decrypted_possible)
        poss_msgs.append(k)
        k -= 1
    poss_msgs = [poss_msgs[x:x+2] for x in range(0, len(poss_msgs), 2)]
    for possible_msg in poss_msgs:
        check_vocab(possible_msg)
    poss_msgs = sorted(poss_msgs, key=lambda x:x[2], reverse=True)
    print(f"deciphered message > {poss_msgs[0][0]}")
    print(f"key > {poss_msgs[0][1]}")

decrypt_all(input("caesar cipher to decipher > "))
