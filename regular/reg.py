# regular expressions 
# https://regexr.com/

import re 

text = "hii sir how are you sir"

# search for a pattern

match = re.search("sir",text)
print(match)

if match:
    print("match found")
    print("start index: ",match.start())
    print("end index: ",match.end())

# find all occurrences of a pattern
matchs = re.findall("sir",text,re.IGNORECASE) # case-insensitive
print("matches: ",matchs)

# replace a pattern
print(text)
new_text = re.sub("sir","master",text)
print(new_text)