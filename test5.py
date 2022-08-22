import os


def cleanedup(s):
    alphabet='123456789@_abcdefghijklmnopqrstuvwxyz'
    cleantext=''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext +=' '
    return cleantext


def findMentions(filename):
    dictionary = {}
    with open(filename, encoding='utf-8') as lines:
        for line in lines:
            for user in cleanedup(line).split():
                if user[0] == '@':
                    if user in dictionary:
                        dictionary[user] += 1
                    else:
                        dictionary[user] = 1
    listUsers = []
    for user in dictionary:
        listUsers.append([dictionary[user],user])
    listUsers.sort()
    print(filename)
    print('  ', listUsers[-3][1], listUsers[-3][0])
    print('  ', listUsers[-2][1], listUsers[-2][0])
    print('  ', listUsers[-1][1], listUsers[-1][0])

    
for filename in os.listdir('.'):
    if filename[-7:]=='.tweets':
        findMentions(filename)
        print()



