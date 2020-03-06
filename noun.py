import nltk
file_name = input("Enter the text file name :-- ")
File = open( file_name, "r")
fw = open('AllNoun.txt','w')
lines = File.read()
sentences = nltk.sent_tokenize(lines)
nouns = []

for sentence in sentences:

     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):

         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
             nouns.append(word)
             fw.write(word)
             fw.write(" ")

#print(nouns)
fw.close()
text = open("simple.txt", "r")
d = dict()
for line in text:
    line = line.lower()
    words = line.split(" ")

    for word in words:
        if word in d:
            d[word] = d[word] + 1

        else:
            d[word] = 1

for key in list(d.keys()):
    if int(d[key]) >= 4:
        print(key, ":", d[key])
