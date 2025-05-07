# Text Analyzer

# Step 1: Ask user to enter text
text = input("Enter some text: ")

# Step 2: Analyze the text
word_count = len(text.split())
char_count = len(text)
space_count = text.count("")

# Count vowels and consonants
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Step 3: Show results
print("\n--- Text Analysis ---")
print(f"Total characters: {char_count}")
print(f"Total words: {word_count}")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")