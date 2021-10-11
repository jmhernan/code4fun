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
assert len(new_list) == len(test)

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
nums = [2, 7, 11, 15]
target = 9

nums = [0,2,3,1,3]
target = 6
# works for adjacent numbers 
for i in range(len(nums)-1):
    test = nums[i] + nums[i+1] 
    if test == target:
        print(i, i+1)
    else:
        i += 1 

# THIS WORKS BUT YOU NEED TO REVISIT!!!
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        test = nums[i] + nums[j]
        if test == target:
            print(i, j)
        elif j <= len(nums):
            j =+ 1
    else:
        i += 1

# Longest substring 
# 1. hash to count all occurences 
# create a sublist of everything that is 1 

def len_substr(s):
    counter_dict = {}
    for item in s:
            if (item in counter_dict): 
                counter_dict[item] += 1
            else:
                counter_dict[item] = 1
    if len(counter_dict) == 0:
        return len(counter_dict)
    if counter_dict[s[0]] != 1:
        return len(counter_dict)
    else: 
        return  len(counter_dict)-1    

s = 'abcabcbb'
len_substr(s)
s = "bbbbb"
len_substr(s)
s = "pwwkew"
len_substr(s)
s = " "
len_substr(s)

