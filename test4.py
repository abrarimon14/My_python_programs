import random
import cards



def oneGame(initial):
    current = initial
    numberRounds = 0
    while 0<current<2*initial:
        deck = cards.shuffledDeck()
        hand = []
        for i in range(6):
            hand.append(deck[i])
        faceCards = []
        for j in range(6):
            faceCards.append(cards.faceValueOf(hand[j]))
        if 'ace' in faceCards:
            current +=1
        else:
            current -=1
        numberRounds +=1
    return numberRounds

def experiment(initial):
    totalRounds = 0
    for number in range(1000):
        totalRounds += oneGame(initial)
    average = totalRounds/1000
    return average

while True:
    userInput = int(input('Enter initial amount: '))
    avg = experiment(userInput)
    print('Average number of rounds: ', avg)

                
                
            
            


    
