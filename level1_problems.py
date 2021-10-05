# bisection search for square roots

def squareRootBi(x, epsilon):
    """Assumes x and epsilon are positive floats & epsilon < 1
    Returns a y such that y*y is within epsilon of x"""
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
            ans = (high + low)/2.0
    return ans


string_1 = "iceman"
string_2 = "cinema"

def anagram_check(str_1, str_2):
    str_1_sorted = sorted(str_1) 
    str_2_sorted = sorted(str_2)
    if str_1_sorted == str_2_sorted:
        return True
    else:
        return False

anagram_check(string_1, string_2)

## First repeating 

str1 = 'hedahder'
####
letter = {}
for l in str1:
    if l in letter.keys():
        letter[l] += 1
        print(l)
        break
    else: 
        letter[l] = 1

###
# using a counter 
for c in str1:
    count = str1.count(c)
    if count == 2:
        print(c)
        break

# moving all 0 zeros to the right 
test = [1,2,0,3,9,4,0,0]

len(test)
# count all zeros 
# create a new list of leading zeros 
zeros = [0]*test.count(0)
# remove zeros from original and append 
non_zero = [i for i in test if i != 0]
new_list = zeros + non_zero
len(new_list) == len(test)






