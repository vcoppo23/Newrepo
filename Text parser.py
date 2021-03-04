import re

filename = input("Name of file: ")
newname = input("What would you like to call your new file?:")

with open(filename, 'r') as file:
    data = file.readlines()
    data = ''.join(data)
    ## Change the numbers in the brackets to change the length requirments of the word
    wordlist = re.findall(r'\b[a-zA-Z]{4,7}\b',data)
    
    
newfile = open(newname, 'x')
with open(newname, 'w') as newfile:
    for i in range(0, len(wordlist)):
        newfile.write(wordlist[i] + '\n')
