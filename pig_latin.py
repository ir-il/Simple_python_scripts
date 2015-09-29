print("Welcome to the Pig Latin Translator!")
pyg = 'ay'
original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    new_word = word[1:len(word)] + word[0] + pyg
    print("%s = %s + %s + " % (new_word, word[1:], word[0]) + pyg)
else:
    print('empty')