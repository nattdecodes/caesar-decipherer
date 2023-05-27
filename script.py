# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
import json
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
        else: decrypted += char# if its neither alphabetical nor a number, just leave it like that
    return decrypted

def letter_distr(possible_msg):
    indexes = []
    occurrences = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
    # Calculate letter distribution in possible_msg
    total_letters = 0
    for letter in possible_msg:
        if letter.isalpha():
            occurrences[letter.lower()] += 1
            total_letters += 1
    # Calculate percentage distribution
    distribution = {letter: (count / total_letters * 100) if total_letters > 0 else 0 for letter, count in occurrences.items()}
    # Load English letter distribution from JSON file
    with open("caesar-salad/distributionfiles/englishletters.json") as json_file: dic_distr = json.load(json_file)
    # Compare distributions
    for letter in occurrences.keys():
        # Compare percentage distributions
        index = (distribution[letter]/dic_distr[letter])
        indexes.append(index)
    # Calculate the index average
    filtered_nbrs = [num for num in indexes if num != 0.0]
    average_without_zeros = round(sum(filtered_nbrs) / len(filtered_nbrs), 4)
    return average_without_zeros

def check_vocab(possible_msg):
    hits = 0
    for word in possible_msg[0].split():
        with open(r"caesar-salad\wordfiles\englishwords.txt", "r", encoding="utf8") as wl_en:
            for line in wl_en:
                if line.strip() == word.lower():
                    hits += 1
                    break # next word
                continue # else: next line
    possible_msg.append(hits)

def decrypt_all(encrypted_msg):
    key = 25 # All possible keys
    possible_msgs = []
    sorted_decrypted = []
    top_chosen_nbr = 5 # Only decrypts the first n messages based on letter distribution
    while key > 0: # Decrypts every possible keys
        decrypted_gibberish = cipher_decrypt(encrypted_msg, key)
        possible_msgs.append(decrypted_gibberish)
        possible_msgs.append(key)
        key -= 1
    possible_msgs = [possible_msgs[x:x+2] for x in range(0, len(possible_msgs), 2)] # Group each message with its key
    for item in possible_msgs:
        item.append(letter_distr(item[0])) # Get the letter distribution index for each message
    sorted_decrypted = (sorted(possible_msgs, key=lambda x: abs(x[2] - 1)))[:top_chosen_nbr] # Sort messages by index and pick the n first ones
    for top_poss_msg in sorted_decrypted:
        check_vocab(top_poss_msg)
    possible_msgs = sorted(possible_msgs, key=lambda x:x[2], reverse=True) # Sort messages by the vocab check as it's more accurate
    print(f"deciphered message > {sorted_decrypted[0][0]}")
    print(f"key > {sorted_decrypted[0][1]}")

# Format: ["possible message", keynbr, indexdistrnbr, hitsnbr]
decrypt_all(input("caesar cipher to decipher > "))
