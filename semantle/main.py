"""
A Simple Semantle-esque game for the terminal
"""

import re
import random
from typing import List
from tqdm import tqdm

PATTERN : str = r'^[a-zA-Z]+$'
WORD_LIST_FILEPATH : str = "./word_lists/words.txt"

def compute_distance(word1:str ,word2: str) -> int:
    """ Compute the Levenshtein Distance between two words"""

    len_word1 = len(word1)
    len_word2 = len(word2)
    dp = [[0] * (len_word2 + 1) for _ in range(len_word1 + 1)]

    # Initialize the matrix
    for i in range(len_word1 + 1):
        dp[i][0] = i
    for j in range(len_word2 + 1):
        dp[0][j] = j
    # Compute the distance
    for i in range(1, len_word1 + 1):
        for j in range(1, len_word2 + 1):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,    # Deletion
                           dp[i][j - 1] + 1,    # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution
    return dp[len_word1][len_word2]



print(f"Loading word list {WORD_LIST_FILEPATH} ...")
words : List[str] = []
with open(WORD_LIST_FILEPATH,"r",encoding="UTF-8") as f:
    for line in f:
        word = f.readline().strip().lower()
        if re.fullmatch(PATTERN,word):
            words.append(word)

print("Done")

print("Choosing a random word")
WORD_OF_THE_DAY = random.choice(words)
distances = {word:compute_distance(WORD_OF_THE_DAY,word) for word in tqdm(words)}
print("Start Guessing!")

inp :str = ""
distance: int = 1

while True:
    inp :str = input("Enter your guess\n").strip().lower()

    match inp:
        case "quit":
            print("okay, let's stop")
            break
        case "giveup":
            print(f"Hahaha Okay, here {WORD_OF_THE_DAY}")
            print("\n")
            break

    if inp in distances:
        distance = distances[inp]
        print(f"Your distance to the word is {distance}")
        print("\n")
    else:
        print("Invalid word")
        print("\n")
print("Thank you for Playing!")
