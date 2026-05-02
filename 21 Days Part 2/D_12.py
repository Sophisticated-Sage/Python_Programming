sentence = input("Enter a sentence: ")
old_word = input("Word to replace: ")
new_word = input("New word: ")

words = sentence.split()

for i in range(len(words)):
    if words[i] == old_word:
        words[i] = new_word

result = " ".join(words)
print("Updated sentence:", result)
