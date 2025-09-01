with open("Story.txt", "r") as f:
    story = f.read()
Words = set()
wordStart = -1
targetStart = "<"
targetEnd = ">"
for i, char in enumerate(story):
    if char == targetStart:
        wordStart = i
    
    if char == targetEnd and wordStart != -1:
        Word = story[wordStart: i + 1]
        Words.add(Word)
        wordStart = -1

Answers = {}
for Word in Words:
    answer = input("Enter a word for " + Word + ": ")
    Answers[Word] = answer

for Word in Words:
    story = story.replace(Word, Answers[Word])

print(story)