alphabet = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5
}

sum = 0

word = input()

for letter_index in range(0, len(word)):
    current_letter = word[letter_index]

    if current_letter in alphabet:
        sum += alphabet[current_letter]

print(sum)
