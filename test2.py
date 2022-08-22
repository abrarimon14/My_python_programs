#1
wordcount = 0
with open('alice.txt') as book:
    for line in book:
        for word in line.split():
            wordcount += 1
print('Total number of words: ', wordcount)

#2
linecount = 0
with open('alice.txt') as book:
    for line in book:
        linecount += 1
print('Average number of words in a line: ', wordcount/linecount)
        
#3
maxwords = 0
with open('alice.txt') as book:
    for line in book:
        wordcount = len(line.split())
        if wordcount > maxwords:
            maxwords = wordcount
            maxline = line
print('Longest line has', maxwords, 'words: ', maxline)

#4
userword = input('Enter word: ')
numberoflines = 0
with open('alice.txt') as book:
    for line in book:
        if userword in line:
            numberoflines += 1
            if numberoflines < 11:
                print(line)
if numberoflines == 0:
    print('Not found')
if numberoflines > 0:
    print(numberoflines, 'lines contain', userword)
