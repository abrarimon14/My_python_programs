from tkinter import *
import random
import cards


class Card:
    def __init__(self, f, s):
        self.myFaceValue = f
        self.mySuit = s
    def __str__(self):
        return self.myFaceValue + ' of ' + self.mySuit
    def faceValue(self):
        return self.myFaceValue
    def suit(self):
        return self.mySuit
    
class Deck:
    faceValues = ['ace', '2', '3', '4', '5', '6', '7', '8',
                  '9', '10', 'jack', 'queen', 'king']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    def __init__(self):
        self.theCards = [Card(faceValue, suit)
                         for faceValue in Deck.faceValues
                         for suit in Deck.suits]
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.theCards)
    def deal(self, n):
        return [str(self.theCards.pop()) for i in range(n)]
    def cardsLeft(self):
        return len(self.theCards)

class enhancedEntry(Frame):
    def __init__(self, parent, prompt, actionText, action):
        Frame.__init__(self, parent)
        self.inputBoxLabel = Label(self)
        self.inputBoxLabel['text'] = prompt
        self.inputBoxLabel.pack(side=LEFT, fill=X)
        self.inputBox = Entry(self)
        self.inputBox.pack(side=LEFT, fill=X)
        self.button = Button(self)
        self.button['text'] = actionText
        self.button['command'] = action
        self.button.pack(side=LEFT, fill=X)
    def get(self):
        return self.inputBox.get()
    def delete(self):
        self.inputBox.delete(0, END)
    def setActionText(self, actionText):
        self.button['text'] = actionText
    def setPrompt(self, prompt):
        self.inputBoxLabel['text'] = prompt
    def setAction(self, cmd):
        self.button['command'] = cmd

def evaluate(hand):
    score = 0
    fvCounts = {}
    for card in hand:
        fv = cards.faceValueOf(card)
        if fv in fvCounts:
            fvCounts[fv] += 1
        else:
            fvCounts[fv] = 1
    justCounts = []
    for fv in fvCounts:
        justCounts.append(fvCounts[fv])
    justCounts.sort()
    for count in justCounts:
        if count == 2:
            score += 1
        if count == 3:
            score += 10
        if count == 4:
            score += 100
    return score


#This is the third step.
##while True:
##    userInput = input('Number of cards:')
##    if userInput.isdigit():
##        userInput = int(userInput)
##        if userInput <= 52:
##            hand = Deck().deal(userInput)
##            for card in hand:
##                print('    ', card)
##            print('     -----------> Score:', evaluate(hand))
##        else:
##            print('Invalid entry! Enter a positive integer less than 53.')
##    else:
##        print('Invalid entry! Enter an integer.')
#This is the end of the third step.


class CardsFrame(Frame):
    def __init__(self, parent, Card):
        Frame.__init__(self, parent)
        for card in Card:
            self.button = Button(self)
            self.button['text'] = card
            self.button.pack(fill=X)


root = Tk()

def mainDeal():
    global cardButtons, direction
    direction.destroy()
    if userInput.get().isdigit():
        number = int(userInput.get())
        if number < 53:  
            myHand = Deck().deal(int(userInput.get()))
            userInput.delete()
            cardButtons.destroy()
            cardButtons = CardsFrame(root, myHand)
            cardButtons.pack()
            scoreLabel['text'] = 'Score:{0}'.format(evaluate(myHand))
        else:
            userInput.delete()
            direction = Label(scoreFrame)
            direction['text'] = 'Invalid entry! Enter a positive integer less than 53.'
            direction.pack()
    else:
        userInput.delete()
        direction = Label(scoreFrame)
        direction['text'] = 'Invalid entry! Enter a positive integer less than 53.'
        direction.pack()
        
userInput = enhancedEntry(root, 'Number of cards:', 'Deal', mainDeal)
userInput.pack()

scoreFrame = Frame(root)
scoreFrame.pack()

direction = Label(scoreFrame)
direction.pack()

scoreLabel = Label(scoreFrame)
scoreLabel['text'] = 'Score:'
scoreLabel.pack()

cardButtons = CardsFrame(root, [])
cardButtons.pack()






















