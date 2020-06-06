#!/usr/bin/env python3
import json
import random
import difflib

initial_words = {
    "azure": "bright blue",
    "defenestrate": "throw out of a window",
    "penultimate": "second last",
    "stochastic": "random"
}

# Code to save the words to a file at the end of the program
def save_words_to_file(words):
    with open('saved_words.json', 'w') as f:
        json.dump(words, f, indent=4, sort_keys=True)

# Code to read the words from a file at the start of the next run
def load_words_from_file():
    with open('saved_words.json', 'r') as f:
        words = json.load(f)
    return words

# Code to define a new custom word
def add_new_word(words):
    term = input("New term: ")
    definition = input("New definition: ")
    if term != "" and definition != "":
        words[term] = definition
        print("Added!\n")
    else:
        print("Invalid entry\n")

def main():
    # Load the words from the last run (if any)
    try:
        words = load_words_from_file()
        print("(words loaded from save file)\n")
    except OSError:
        print("(save file does not exist yet, or could not be loaded)\n")
        words = initial_words

    # Play the game
    print("⚡⚡⚡ Play Flashcard Game ⚡⚡⚡\n")
    score = 0
    terms = list(words.keys())
    random.shuffle(terms)

    try:
        for term in terms:
            response = input(f"What is the definition of {term}? ")
            definition = words[term]
            match = difflib.SequenceMatcher(a=response, b=definition)
            similarity = match.ratio()
            if similarity == 1:
                print("Correct!")
            elif similarity == 0:
                print("Wrong!")
            else:
                print(f"Almost!")
            print(f"The expected answer is \"{definition}\"")
            points = round(similarity,1) 
            print(f"{points} points awarded\n")
            score += points

        print(f"Finished 🎉  Score: {score}/{len(words)}\n")
        
        while True:
            response = input("Would you like to add a new word to the game? (y/n) ")
            if response.lower() != "n":
                add_new_word(words)
            else:
                print("Exiting...")
                break
    # The finally block makes sure the words are always saved
    # even if there is an exception/error
    finally:
        print("\nSaving words...")
        # Save the custom words to a file
        save_words_to_file(words)
        print("Words saved!")

if __name__ == "__main__":
    main()
