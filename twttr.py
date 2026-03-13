text = input("Input: ")

print("Output: ", end="")

for letter in text:
    if letter.lower() not in "aeiou":
        print(letter, end="")

print()