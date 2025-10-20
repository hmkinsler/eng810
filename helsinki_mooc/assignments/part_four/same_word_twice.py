# Write your solution here
words = []
unique_words = 0

while True:
    x = input("Word: ")

    if x in words:
        break
    else:
        words.append(x)
        unique_words += 1

print(f"You typed in {unique_words} different words")


    