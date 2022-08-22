#  A-1K:  Mean or NastyMirror
#  A-8K:  Mean
#  A-32K: Mirror
#
#  B-1K:  NastyMirror
#  B-8K:  Mirror, NastyMirror or Random
#  B-32K: Random or Mirror
#
#  C-1K:  NastyMirror
#  C-8K:  Mirror or (Mirror and Counting together)
#  C-32K: Mirror or (Mirror and Counting together)

import random
class Player:
    idCounter = 0
    totalEncounters = 0
    strangerEncounters = 0
    def __init__(self):
        self.score = 0
        self.memory = {}
        Player.idCounter += 1

        self.name = 'Player {0}'.format(Player.idCounter)
    def processResult(self, otherName,myResponse,otherResponse):
        Player.totalEncounters += 1
        if otherName not in self.memory:
            Player.strangerEncounters += 1
        result = [myResponse, otherResponse]
        if otherName in self.memory:
            self.memory[otherName].append(result)
        else:
            self.memory[otherName] = [result]
        if myResponse == 'nice' and otherResponse == 'nice':
            self.score += 30
        elif myResponse == 'nice' and otherResponse == 'nasty':
            self.score -= 70
        elif myResponse == 'nasty' and otherResponse == 'nice':
            self.score += 50
        else:
            self.score += 0
class FriendlyPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (friendly)'
    def respondsTo(self, otherName):
        return 'nice'
    
class MeanPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (mean)'
    def respondsTo(self, otherName):
        return 'nasty'

class MirrorPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (mirror)'
    def respondsTo(self, otherName):
        if otherName in self.memory:
            return self.memory[otherName][-1][1]
        else:
            return 'nice'

class RandomPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (random)'
    def respondsTo(self, otherName):
        return random.choice(['nice', 'nasty'])

class NastyMirrorPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (nasty mirror)'
    def respondsTo(self, otherName):
        if otherName in self.memory:
            return self.memory[otherName][-1][1]
        else:
            return 'nasty'

class CountingPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (counting)'
    def respondsTo(self, otherName):
        nicePoint = 0
        nastyPoint = 0
        for name in self.memory:
            for interaction in self.memory[name]:
                if interaction[1] == 'nice':
                    nicePoint += 1
                else:
                    nastyPoint += 1
        if nicePoint >= nastyPoint:
            return 'nice'
        else:
            return 'nasty'


class ProbingPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (probing)'
    def respondsTo(self, otherName):
        if otherName in self.memory:
            record = self.memory[otherName]
            if len(record) == 1:
                return 'nice'
            elif record[0][1] == 'nice' and record[1][1] == 'nice':
                return 'nasty'
            elif record[0][1] == 'nasty' and record[1][1] == 'nasty':
                return 'nasty'
            else:
                return 'nice'
        else:
            return 'nasty'


def encounter(player1, player2):
    name1, name2 = player1.name, player2.name
    response1 = player1.respondsTo(name2)
    response2 = player2.respondsTo(name1)
    player1.processResult(name2, response1, response2)
    player2.processResult(name1, response2, response1)
def makePopulation(specs):
    population = []
    for playerType, number in specs:
        for player in range(number):
            population.append(playerType())
    return population
def doGeneration(population, numberOfEncounters):
    for encounterNumber in range(numberOfEncounters):
        players = random.sample(population, 2)
        encounter(players[0], players[1])
def sortPopulation(population):
    scoreList = [[player.score, player.name, type(player)]
                 for player in population]
    scoreList.sort()
    return scoreList

def report(scoreList):
    pattern = '{0:23s}{1:6d}'
    friendNum = 0
    meanNum = 0
    mirrorNum = 0
    randomNum = 0
    nastyMirrNum = 0
    countingNum = 0
    for player in allPlayers:
        if type(player) == FriendlyPlayer:
            friendNum += 1
        elif type(player) == MeanPlayer:
            meanNum += 1
        elif type(player) == MirrorPlayer:
            mirrorNum += 1
        elif type(player) == RandomPlayer:
            randomNum += 1
        elif type(player) == NastyMirrorPlayer:
            nastyMirrNum += 1
        elif type(player) == CountingPlayer:
            countingNum += 1
    print(patternRow.format(str(friendNum),str(meanNum),str(mirrorNum),str(randomNum),str(nastyMirrNum),str(countingNum)))
    
def makeNextGeneration(scoreList):
    nextGeneration = []
    populationSize = len(scoreList)
    scoreList = scoreList[int(populationSize/2):]
    for score, name, playerType in scoreList:
        for number in range(2):
            nextGeneration.append(playerType())
    return nextGeneration


patternRow = '{0:13s}{1:13s}{2:13s}{3:13s}{4:13s}{5:13s}'


##print(patternRow.format('Friend', 'Mean', 'Mirror', 'Random', 'NastyMirror', 'Counting'))
##allPlayers = makePopulation([[FriendlyPlayer, 10], [MeanPlayer, 10], [MirrorPlayer, 10], [RandomPlayer, 10], [NastyMirrorPlayer, 10], [CountingPlayer, 10]])
##
##for generationNumber in range(20):
##    doGeneration(allPlayers, 32000)
##    sortedResults = sortPopulation(allPlayers)
##    report(sortedResults)
##    allPlayers = makeNextGeneration(sortedResults)


A = [[FriendlyPlayer, 10], [MeanPlayer, 10], [MirrorPlayer, 10], [RandomPlayer, 10], [NastyMirrorPlayer, 10], [CountingPlayer, 10]]
B = [[FriendlyPlayer, 10], [MeanPlayer, 0], [MirrorPlayer, 10], [RandomPlayer, 10], [NastyMirrorPlayer, 10], [CountingPlayer, 10]]
C = [[FriendlyPlayer, 0], [MeanPlayer, 0], [MirrorPlayer, 10], [RandomPlayer, 10], [NastyMirrorPlayer, 10], [CountingPlayer, 10]]

def test(scenario, numberOfEnounters):
    print(patternRow.format('Friend', 'Mean', 'Mirror', 'Random', 'NastyMirror', 'Counting'))
    global allPlayers
    allPlayers = makePopulation(scenario)
    for generationNumber in range(20):
      doGeneration(allPlayers, numberOfEnounters)
      sortedResults = sortPopulation(allPlayers)
      report(sortedResults)
      allPlayers = makeNextGeneration(sortedResults)

##test(C, 32000)




























    
