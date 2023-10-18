# pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long, missing-function-docstring, missing-module-docstring
import json
import os


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
    # Initialize occurrences in message
    occurrences = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
    # Calculate letter distribution in possible_msg
    total_letters = 0
    for letter in possible_msg:
        if letter.isalpha():
            occurrences[letter.lower()] += 1
            total_letters += 1
    # Calculate percentage distribution
    distribution = {letter: (count / total_letters * 100) if total_letters > 0 else 0 for letter, count in occurrences.items()}
    # Establish absolute path
    script_dir = os.path.dirname(__file__)
    # Load English letter distribution from JSON file
    with open(os.path.join(script_dir, "distributionfiles/englishletters.json"), "r", encoding="utf-8") as json_file: dic_distr = json.load(json_file)
    # Compare distributions
    for letter in occurrences.keys():
        # Compare percentage distributions
        index = distribution[letter]/dic_distr[letter]
        indexes.append(index)
    # Calculate the index average
    filtered_nbrs = [num for num in indexes if num != 0.0]
    average_without_zeros = round(sum(filtered_nbrs) / len(filtered_nbrs), 4)
    return average_without_zeros

def check_vocab(possible_msg):
    hits = 0
    # Establish absolute path
    script_dir = os.path.dirname(__file__)
    for word in possible_msg[0].split():
        with open(os.path.join(script_dir, "wordfiles/englishwords.txt"), "r", encoding="utf8") as wl_en:
            for line in wl_en:
                if line.strip() == word.lower():
                    hits += 1
                    break # next word
                continue # else: next line
    possible_msg.append(hits)

def decrypt_all(encrypted_msg):
    key = 25 # All possible keys
    v_sorted_dec = []
    i_sorted_dec = []
    top_chosen_nbr = 5 # Only decrypts the first n messages based on letter distribution
    min_hits = 2 # The minimum amount of hits a decrypted message has to have to be considered the final message

    # Decrypt every possible keys
    while key > 0:
        decrypted_gibberish = cipher_decrypt(encrypted_msg, key)
        v_sorted_dec.append(decrypted_gibberish)
        v_sorted_dec.append(key)
        key -= 1

    # Group each message with its key
    v_sorted_dec = [v_sorted_dec[x:x+2] for x in range(0, len(v_sorted_dec), 2)]

    # Get the letter distribution index for each message
    for item in v_sorted_dec:
        item.append(letter_distr(item[0]))

    # Sort messages by index and pick the n first ones
    i_sorted_dec = sorted(v_sorted_dec, key=lambda x: abs(x[2] - 1))

    while True:

        # Check Vocab for the top n keys
        for top_msg in i_sorted_dec[:top_chosen_nbr]:
            check_vocab(top_msg)

        # Do nothing for the bottom n
        for bottom_msg in i_sorted_dec[top_chosen_nbr:]:
            bottom_msg.append(0)

        # Sort messages by the vocab check
        v_sorted_dec = sorted(v_sorted_dec, key=lambda x:x[-1], reverse=True)

        # Check if there's no more keys or if the minimum amount of hits is.. well... hit
        if top_chosen_nbr >= 25 or v_sorted_dec[0][-1] >= min_hits:
            i_sorted_dec = v_sorted_dec
            break

        top_chosen_nbr += top_chosen_nbr

    print(f"deciphered message > {v_sorted_dec[0][0]}")
    print(f"key > {i_sorted_dec[0][1]}")
# Format: ["possible message", keynbr, indexdistrnbr, hitsnbr]

if __name__ == "__main__":
    cipher = input("caesar cipher to decipher > ")
    print(decrypt_all(cipher))
