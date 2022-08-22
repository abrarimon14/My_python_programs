import urllib.request

url = 'http://nancymcohen.com/csci133/cpiai.txt'
file = urllib.request.urlopen(url)
lines = file.readlines()
file.close()

cpi = {}
for line in lines:
    items = line.decode().split()
    if len(items) > 0 and items[0].isdigit():
        cpi[int(items[0])] = [float(item) for item in items[1:13]]

def listAverage(L):
    total = 0
    for number in L:
        total += number
    return (total/len(L))
        
userInput = (input('Enter query: ')).split()
userYearMonths = [float(number) for number in userInput]

if len(userYearMonths) == 1:
    listCPI = [number for number in cpi[userYearMonths[0]]]
    print(listCPI, listAverage(listCPI))
else:
    index = [int(number) for number in userYearMonths[1:len(userYearMonths)]]
    listCPI = [cpi[userYearMonths[0]][index[i]-1] for i in range(len(index))]
    print(listCPI, listAverage(listCPI))



