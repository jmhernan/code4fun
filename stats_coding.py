# Given an array, (X) of (N) integers, calculate and print the 
# respective mean, median, and mode on separate lines. 
# If your array contains more than one modal value, choose 
# the numerically smallest one.

import numpy as np

n = 10
ar = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060, 51135, 14216, 51135]
type(ar)
sum(ar)
sorted(ar)


def stats(n, number_list):
    
    mean = sum(number_list)/n
    
    sorted_array = sorted(number_list)
    
    if n%2 != 0:
        median = sorted_array[int(len(sorted_array)/2)]
    else:
        middle_1 = sorted_array[int(len(sorted_array)/2)]
        middle_2 = sorted_array[int(len(sorted_array)/2) - 1]
        median = (middle_1 + middle_2) / 2

    counter_dict = {}

    for item in sorted_array:
        if (item in counter_dict): 
            counter_dict[item] += 1
        else:
            counter_dict[item] = 1
        
    max_value = max(counter_dict.values())
    if max_value == 1:
        mode = sorted_array[0]
    else:
        most_frequent = [k for k,v in counter_dict.items() if v == max(counter_dict.values())]
        mode = min(most_frequent)
    
    return(print(mean, 
                 "\n", median,
                 "\n",mode))


if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    stats(n=n, number_list=ar)

test = '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060'
list(map(int, test.split()))
stats(n=n, number_list=ar)

# for odd
median = ar[int(len(ar)/2)]

# for even we need:
# find the the 2 middle value indeces 
middle_1 = ar[int(len(ar)/2)]
middle_2 = ar[int(len(ar)/2) - 1]

median = (middle_1 + middle_2) / 2

# mode

def mode(array): 
    sorted_array = np.sort(array)
    counter_dict = {}

    for item in sorted_array:
        if (item in counter_dict): 
            counter_dict[item] += 1
        else:
            counter_dict[item] = 1
        
    max_value = max(counter_dict.values())
    if max_value == 1:
        mode = sorted_array[0]
    else:
        most_frequent = [k for k,v in counter_dict.items() if v == max(counter_dict.values())]
        mode = min(most_frequent)
    return(mode)

mode(ar)

