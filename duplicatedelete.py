import fileinput
with open('bx.txt') as fin:
    exclude = set(line.rstrip() for line in fin)

for line in fileinput.input('ax.txt', inplace=True):
    if line.rstrip() not in exclude:
        print (line)
