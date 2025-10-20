# Prompt user for input
text = input("Text: ")

# Initialize counters
letters = 0
words = 1  # Start at 1 because the last word won't have a trailing space
sentences = 0

# Count letters, words, sentences
for char in text:
    if char.isalpha():
        letters += 1
    elif char == ' ':
        words += 1
    elif char in ['.', '!', '?']:
        sentences += 1

# Compute averages per 100 words
L = (letters / words) * 100
S = (sentences / words) * 100

# Coleman-Liau index
index = 0.0588 * L - 0.296 * S - 15.8
grade = round(index)

# Output result
if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")
