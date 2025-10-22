with open("Story.txt", "r") as f:
    story = f.read()
Words = set() # we use set here because they don't hold any duplicate values. All, unique values are stored. Here "Words" is a variable which is a set 
wordStart = -1
targetStart = "<"
targetEnd = ">"
for i, char in enumerate(story):
    if char == targetStart:
        wordStart = i # A store of value - that stores the index position where the < is found in the string
    if char == targetEnd and wordStart != -1: 
        Word = story[wordStart: i + 1] # here the terms inside [] mean we want to access parts of string beginning from character at wordStart and until "i+1"
        # Give me the substring starting at the character at position wordStart, and go up to (but include) the character at position i.
        Words.add(Word) #Add the string stored in Word to the set Words.
        wordStart = -1

Answers = {}
for Word in Words:
    answer = input("Enter a word for " + Word + ": ")
    Answers[Word] = answer

for Word in Words:
    story = story.replace(Word, Answers[Word])

print(story)

# I can use none as well here to indicate no value found at wordstart 
# but None vs -1 
# None -> We want to signal absence of a value clearly
# -1 -> means not found but used only when working with numbers or positions like list or string

# We are saying that start enumerating the story file that is start counting string with their index when you find < that mean you found the iterator, here we call it i. When counting the string you encounter > when we already found < stop. Here you need to start getting the strings from until last character and store it in Word. Then add this stored value in Words. (Since Words is a set it will only store unique values. So, if content inside <> is repeated, it is only stored once.). Then reset the find and start again looking for < again. Once done for all and story ends - opena dictionary named Answers. But for each Word stored in set named Words we need input from the user and this input from user is stored in answer. Now, put whatever you got from the user under a label called word (consequently after, the values stored inside <> ares tored in words. That means whatever is stored in <> gets the value from user input) and then Answer[Word] become whatever is stored in answer. Then word story takes a new value where all character stored in <> are replaced by users giving an input ie Word written before , means the value to replace and Answer[Word] written after , means what to replace with. Then print story.

"""
Explanation Refined:

1. Start enumerating the story string — this means going through each character one by one and keeping track of its position (called i here).
2. When you find a < character, it means you've found the start of a placeholder.
3. Continue counting until you encounter a > character after finding <.
4. Once you find >, extract the substring starting from < up to and including > — store this in Word.
5. Add this Word to the set Words. Since Words is a set, it stores only unique placeholders, so repeated placeholders are stored once.
6. Reset the search (by setting wordStart = -1) and start looking for the next <.
7. After the entire story is processed, create an empty dictionary called Answers.
8. For each placeholder in Words, ask the user for an input (like a replacement word), and store this input in the variable answer.
9. Save this input in the dictionary Answers under the key Word (the placeholder), so Answers[Word] = answer.
10. Then, replace all instances of the placeholder in the story string with the corresponding user input (Answers[Word]).
11. Finally, print the modified story with all placeholders replaced by user inputs.
"""
