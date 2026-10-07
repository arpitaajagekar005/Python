
file = open("sample.txt", "r")

text = file.read()
file.close()

word = input("Enter word to search: ")
frequency = text.lower().split().count(word.lower())

print("Frequency of", word, "is:", frequency)