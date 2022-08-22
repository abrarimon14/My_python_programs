#1:
with open('elon-musk.txt') as book:
    numberofTweets = 0
    for tweet in book:
        numberofTweets += 1
    print('Number of tweets: ', numberofTweets)
    
#2:
with open('elon-musk.txt') as book:
    maxWords = 0
    for tweet in book:
        if len(tweet.split()) > maxWords:
            maxWords = len(tweet.split())
            longestTweet = tweet
    print('Tweet with max number of words:', longestTweet)

#3:
def cleanedup(s):
    forCleaning = '@abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in forCleaning:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

with open('elon-musk.txt') as book:
    information = {}
    for tweet in book:
        cleanTweet = cleanedup(tweet)
        for word in cleanTweet.split():
            if '@' in word:
                if word in information:
                    information[word] += 1
                else:
                    information[word] = 1

while True:
    userInput = input('Enter a username: ')
    if userInput in information:
        print('Mentioned', information[userInput], 'times.')
    else:
        print('Not mentioned.')
