# Given an array, 'arr', of 'n' integers, calculate the respective first quartile (Q1), second quartile (Q2), 
# and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.
# Steps
# 1. Sort the array
# 2. Find the lower, middle, and upper medians.
# If the array is odd then the middle element in the middle median (Q2)
# If the array is even then the median is the middle_element + (middle_element -1)/2 = (Q2)

n =  9 
arr = [3, 7, 8, 5, 12, 14, 21, 13,18]

def mdn(sorted_array):
    n_s = len(sorted_array)
    if n_s%2 != 0:
        median = sorted_array[int(n_s/2)]
    else:
        middle_1 = sorted_array[int(n_s/2)]
        middle_2 = sorted_array[int(n_s/2) - 1]
        median = (middle_1 + middle_2) / 2
    return median

# sort the input 
sorted_list = sorted(arr)
int(len(sorted_list)/2)

def qrt(number_list):
    sorted_list = sorted(number_list)
    lower = sorted_list[:int(len(sorted_list)/2)]
    upper = sorted_list[int(len(sorted_list)/2)+1:len(sorted_list)]
    Q2 = mdn(sorted_list)
    Q1 = mdn(lower)
    Q3 = mdn(upper)
    return print(int(Q1), int(Q2), int(Q3))

def quartiles(n, number_list):
    sorted_list = sorted(number_list)
    lower = sorted_list[:int(n/2)]
    upper = sorted_list[int(n/2)+1:n]
    Q2 = mdn(sorted_list)
    Q1 = mdn(lower)
    Q3 = mdn(upper)
    return print('\n',int(Q1),'\n',int(Q2),'\n',int(Q3))

quartiles(n=9, number_list = arr)


