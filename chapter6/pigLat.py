VOWELS = {'a', 'e', 'i', 'o', 'u'}
print('Enter the English Message you\'d like to translate to Pig Latin:')
message = input()

pigLatin = [] # list of words in pig latin

# we will iterate over each character for each word and check to see if there is punctuation
for word in message.split():
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]

    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    suffixNonLetters = ''
    while not word [-1].isalpha():
        suffixNonLetters += word[-1] + suffixNonLetters
        word = word[:-1]

    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()

    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
    
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else: 
        word += 'yay'

    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

print(' '.join(pigLatin))