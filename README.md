# Flashcard Game

A simple Flashcard Game written in Python to answer this question: <https://stackoverflow.com/questions/62147592/save-inputs-as-dictionary-values-forever>

## Example Game

```
$ python3 flashcard_game.py 
(words loaded from save file)

⚡⚡⚡ Play Flashcard Game ⚡⚡⚡

What is the definition of azure? blue
Almost!
The expected answer is "bright blue"
0.5 points awarded

What is the definition of penultimate? second last
Correct!
The expected answer is "second last"
1.0 points awarded

What is the definition of stochastic? ?!@?  
Wrong!
The expected answer is "random"
0.0 points awarded

What is the definition of defenestrate? open a window
Almost!
The expected answer is "throw out of a window"
0.6 points awarded

Finished 🎉  Score: 2.1/4

Would you like to add a new word to the game? (y/n) y
New term: awesome
New definition: this game
Added!

Would you like to add a new word to the game? (y/n) n
Exiting...

Saving words...
Words saved!
```

## Data Format

```
$ cat saved_words.json 
{
    "awesome": "this game",
    "azure": "bright blue",
    "defenestrate": "throw out of a window",
    "penultimate": "second last",
    "stochastic": "random"
}
```

## Acknowledgements

Inspired by [Simon's](https://stackoverflow.com/users/13663897/simon) Stack Overflow [question](https://stackoverflow.com/questions/62147592/save-inputs-as-dictionary-values-forever).

## Questions? Wanna chat?

Send an email to `andrew@simmons.ai`, and I'll try to help!
