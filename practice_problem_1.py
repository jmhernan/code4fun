#Practice Problems 03/16/2020

#Return first repeated character
import math
import os
import random
import re
import sys

a = 'geeksforgeeks'


def return_first():


def countPairs(arr, n): 
  
    mp = dict() 
  
    # Finding frequency of each number. 
    for i in range(n): 
        if arr[i] in mp.keys(): 
            mp[arr[i]] += 1
        else: 
            mp[arr[i]] = 1
              
    # Calculating pairs of each value. 
    ans = 0
    for it in mp: 
        count = mp[it] 
        ans += (count * (count - 1)) // 2
    return ans 

n = 9
a = [10, 20, 20, 10, 10, 30, 50, 10, 20]


countPairs(a, n)