string_name = 'BBBBBBB'
n = 7

for element in string_name[0:n]: 
    if element == 'A':
        print('B', end ='')
    else: 
        print('A', end ='')

def getWrongAnswers(N: int, C: str) -> int:
    temp = [0]*N
    for i, element in enumerate(C): 
        if element == 'A':
            temp[i] = 'B'
        else:
            temp[i] = 'B' 
    return(print(temp))

def getWrongAnswers(N: int, C: str) -> str:
    out = [0]*N
    for i, element in enumerate(C):
        if element == 'A':
            temp = 'B'
        else:
            temp = 'A'
        out[i] = temp
    wrong_str = str(''.join(out))
    return(wrong_str)

N = 5
C = 'BBBBB'

getWrongAnswers(N,C)
type(getWrongAnswers(N,C))

N = 3
C = 'ABA'

getWrongAnswers(N,C)
type(getWrongAnswers(N,C))


import numpy
i = 3
j = 2
l = [[1,0],[0,0],[0,1]]

a = numpy.array(l) 



pct = numpy.count_nonzero(a)/(i*j)

test = sum([sum(x) for x in l])

pct = test/(i*j)