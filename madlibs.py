import re

# TODO: open text file ,
filename = input('enter file name :')
text = open(filename)
newfile = open('newtext','w')

# TODO: create regexs
N = 'NOUN'
ADJ = 'ADJECTIVE'
ADV = 'ADVERB'
V = 'VERB'

ponc = re.compile(r'[,.:;!?]')
# TODO: get user replacements :
for line in text :
    line = line.split()
    for word in line :
        if ponc.match(word[-1]):
            p=word[-1::]
            word = word[:-1:]
        else : p=0
        if word == N :
            noun = input('enter a noun :')
            word = noun
        elif word == ADJ:
            adj = input('enter an adjective :')
            word = adj
        elif word == ADV:
            adv = input('enter an adverb :')
            word = adv
        elif word == V:
            verb = input('enter a verb :')
            word = verb
        if p!=0:
            word = word + p
        newfile.write(word+' ')
# TODO: save matches to a new file
