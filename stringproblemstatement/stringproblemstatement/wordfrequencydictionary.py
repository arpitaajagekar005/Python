s = input("Enter a paragraph: ")
words = s.lower().split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word Frequency:")
for word in freq:
    print(word, ":", freq[word])