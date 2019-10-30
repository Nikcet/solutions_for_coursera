s = input()

pos = s.find(' ')

word1 = s[pos + 1:]
word2 = s[:pos]

print(word1, word2)
