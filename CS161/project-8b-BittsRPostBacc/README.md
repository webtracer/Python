# project-8b

Write a function named words_in_both that takes two strings as parameters and returns a set of only those words that appear in **both** strings.  You can assume all characters are letters or spaces.  Capitalization shouldn't matter: "to", "To", "tO", and "TO" should all count as the same word.  The words in the set should be all lower-case.  For example, if one string contains "To", and the other string contains "TO", then the set should contain "to".

You can use Python's split() funciton, which breaks up a string into a **list** of strings.  For example:
```
sentence = 'Not the comfy chair!'
print(sentence.split())
['Not', 'the', 'comfy', 'chair!']
```

Here's one simple example of how words_in_both() might be used:
```
common_words = words_in_both("She is a jack of all trades", 'Jack was tallest of all')
```

The file must be named: words_in_both.py
