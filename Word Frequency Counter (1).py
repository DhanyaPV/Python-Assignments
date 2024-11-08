import re

text = input("Enter a paragraph of text: ")
text = text.lower()
text = re.sub(r'[^\w\s]', '', text)

word_frequency = {}
for word in text.split():
    word_frequency[word] = word_frequency.get(word, 0) + 1

print("\nWord Frequency:")
for word, count in word_frequency.items():
    print(f"{word}: {count}")