from cs50 import get_string

text = get_string("Text: ")

letters = 0
sentences = 0
words = len(text.split())

for c in text:

    if c.isalpha():
        letters += 1

    if c == "." or c == "!" or c == "?":
        sentences += 1

L = letters / words * 100
S = sentences / words * 100

index = round(0.0588 * L - 0.296 * S - 15.8)

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
