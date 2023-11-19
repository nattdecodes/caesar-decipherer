import os
from math import log

# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
words = open(r"C:\Users\natac\OneDrive\Documents\VSC\caesar-salad\wordfiles\englishwords.txt").read().split()

# Navigate to the parent directory
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Define the path to the file you want to access
file_path = os.path.join(parent_directory, "wordfiles", "englishwords.txt")
# Check if the file exists
if os.path.exists(file_path):
    # If the file exists, you can open and read it
    words = open(r"C:\Users\natac\OneDrive\Documents\VSC\caesar-salad\wordfiles\englishwords.txt").read().split()
else:
    print("The specified file does not exist.")

wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    s = s.lower()
    s = s.replace(".", "").replace(",", "")
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    print(" ".join(reversed(out)))

infer_spaces("Pythonunittestmo.duleisusedto,testaunitof,sourcecodesupposeyouneedto,testyourproject.")