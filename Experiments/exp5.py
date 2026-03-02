#1
text = input("Enter a string: ")
count = 0
for ch in text:
    if ch.isupper():
        count += 1
print("Number of capital letters:", count)
print()

#2 
text1 = input("Enter a string: ")
count1 = 0
for ch2 in text1:
    if ch2.isupper():
        count1 += 1
print("Number of capital letters:", count1)
print()

#3 
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word)
print()

#4 
string = input("Enter string: ")
substring = input("Enter substring: ")
count2 = 0
for i in range(len(string) - len(substring) + 1):
    if string[i:i+len(substring)] == substring:
        count2 += 1
print(count2)
print()

#5 
text2 = input("Enter string: ")
text2 = text2.upper()
checked = set()
for ch3 in text2:
    if ch3.isalpha() and ch3 not in checked:
        print(text2.count(ch3), ch3)
        checked.add(ch3)
print()

#6
sentence1 = input("Enter a sentence: ")
words1 = sentence1.split()
unique_words = set(words1)
print("Number of unique words:", len(unique_words))
print()

#7
n = int(input("Enter number of fruits in each set: "))
s1 = set()
s2 = set()
print("Enter fruits for Set 1:")
for i2 in range(n):
    s1.add(input())
print("Enter fruits for Set 2:")
for i3 in range(n):
    s2.add(input())
print("a) Common fruits:", s1 & s2)
print("b) Fruits only in s1:", s1 - s2)
print("c) Total fruits count:", len(s1 | s2))
print()

#8
S3 = {"Red", "yellow", "orange", "blue"}
S4 = {"violet", "blue", "purple"}
print("Union:", S3 | S4)
print("Intersection:", S3 & S4)
print("Difference (S3 - S4):", S3 - S4)
print("Difference (S4 - S3):", S4 - S3)
print("Symmetric Difference:", S3 ^ S4)
print()