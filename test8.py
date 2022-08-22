from tkinter import *
import readquiz, random

questions = readquiz.loadQuestions()
total = 0
correct = 0



def getNewQuestion():
  global questionNumber
  questionNumber = random.choice(range(len(questions)))
  questionLabel['text'] = questions[questionNumber][0]

def goodAnswer():
  global correct, total
  correct += 1
  total += 1
  statusLabel['text'] = 'Your answer was correct'
  statusLabel['bg'] = 'light green'
  scoreLabel['text'] = 'Score: {0}/{1}'.format(correct, total)
  getNewQuestion()


def badAnswer():
  global correct, total
  correct += 0
  total += 1
  statusLabel['text'] = 'Your answer was incorrect'
  statusLabel['bg'] = 'pink'
  scoreLabel['text'] = 'Score: {0}/{1}'.format(correct, total)
  getNewQuestion()




root = Tk()

topFrame = Frame(root)
topFrame.pack(fill=X)

topLabel = Label(topFrame)
topLabel['text'] = 'Question:'
topLabel.pack()



middleFrame = Frame(root)
middleFrame.pack(fill=X)

questionLabel = Message(middleFrame, width=200)
questionLabel.pack()

buttonFrame = Frame(root)
buttonFrame.pack(fil=X)


def commandYes():
  if questions[questionNumber][1] == True:
    goodAnswer()
  else:
    badAnswer()
    
buttYes = Button(buttonFrame)
buttYes['text'] = 'Yes'
buttYes['command'] = commandYes
buttYes.pack(side=LEFT, expand=YES, fill=BOTH)


def commandNo():
  if questions[questionNumber][1] == True:
    badAnswer()
  else:
    goodAnswer()

buttNo = Button(buttonFrame)
buttNo['text'] = 'No'
buttNo['command'] = commandNo
buttNo.pack(side=LEFT, expand=YES, fill=BOTH)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM, fil=X)

statusLabel= Label(bottomFrame)
statusLabel['text'] = 'Status'
statusLabel.pack(side=LEFT)

scoreLabel= Label(bottomFrame)
scoreLabel['text'] = 'Score: {0}/{1}'.format(correct, total)
scoreLabel.pack(side=RIGHT)

getNewQuestion()








