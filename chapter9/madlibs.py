#! python3
# madlibs.py - takes an input textfile and replaces keywords to generate a madlibs inspired text output

keywords = ['NOUN', 'ADJECTIVE', 'ADJECTIVE_(feeling)', 'ADVERB', 'VERB', 'DURATION_OF_TIME', 'NUMBER']

output = open('output.txt', 'w')
punctuation = ['.', '!', '?', ';', ':', ',']
# can modify the above or use regex patterns.

# TODO: read file and iterate over each line

inputFile = open('input.txt')
inputLines = inputFile.readlines()
suffix = ''

for line in inputLines:
    # seperate words in lines 
    words = line.split(' ')
    for index in range(len(words)):
        # the input text doesn't have any keywords ending in punctuation
        # just replace
        
        # strip punctuation
        puncIndex = -1
        for char in punctuation:
            if char in words[index]:
                puncIndex = words[index].find(char)
                break
    
        if puncIndex != -1:
            suffix = words[index][puncIndex:]
            words[index] = words[index][:puncIndex]

        if words[index] in keywords:
            promptStr = 'Please input a ' + words[index] + ': '
            words[index] = input(promptStr)

        if suffix != '':
            words[index] += suffix

        suffix = ''
    
    newLine = ' '.join(words)
    output.write(newLine)

output.close()
output = open('output.txt')
for line in output.readlines():
    print(line)
output.close()