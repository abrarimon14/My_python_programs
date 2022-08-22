def goalSeek(function, lowLimit, highLimit, target, maxError=.01):
    error = maxError + 1
    while error > maxError:
        guess = (lowLimit+highLimit)/2
        result = function(guess)
        error = abs(result-target)
        if result > target:
            highLimit = guess
        if result < target:
            lowLimit = guess
    return guess


#1
def P1(x):
    return x*x*x - x*x + 4*x - 30

def P2(x):
    return x*x*x + 0.5*x*x + x - 6

def P3(x):
    return 3*x*x*x + 13.6*x*x + 13.2*x + 47.8

print('root of P1: ', goalSeek(P1, -5, 5, 0))
print('root of P2: ', goalSeek(P2, -5, 5, 0))
print('root of P3: ', goalSeek(P3, -5, 5, 0))
print()


#2
with open('poly.txt') as polynomials:
    for line in polynomials:
        if line[0] != '#':
            information = [float(value) for value in line.split()[:6]]
            print(information)
print()
          

#3
def makePoly(A,B,C,D):
    def P(x):
        return A*x*x*x+B*x*x+C*x+D
    return P


#4
with open('poly.txt') as polynomials:
    for line in polynomials:
        if line[0] != '#':
            info = [float(value) for value in line.split()[:6]]
            P = makePoly(info[0],info[1],info[2],info[3])
            root = goalSeek(P, info[4], info[5], 0, 0.01)
            pattern = '{0:8.2f}{1:8.2f}{2:8.2f}{3:8.2f}  ->  {4:8.2f}'
            print(pattern.format(info[0], info[1], info[2], info[3], root))












