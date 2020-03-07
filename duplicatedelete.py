import fileinput
#enter the file name that contains all the words that are to be eliminate from the other file.
with open('bx.txt') as fin:
    exclude = set(line.rstrip() for line in fin)
#enter the file name whose words are to be deleted.
for line in fileinput.input('ax.txt', inplace=True):
    if line.rstrip() not in exclude:
        print (line)
