#! pytho3
# bulletPointAdder.py

import pyperclip
text = pyperclip.paste() # module is takng whats in clipboard and putting it in variable

lines = text.split('\n') # split up text by newline
for i in range(len(lines)): 
    lines[i] = '* ' + lines[i] # add bullet points to each line in array

text = '\n'.join(lines)

pyperclip.copy(text)