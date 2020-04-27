'''
    Copyright (C) 2020, Sathira Silva.
    
    Problem Statement:  Nikita just came up with a new array game. The rules are as follows:
                            Initially, Nikita has an array of integers.
                            
                            In each move, Nikita must partition the array into 2 non-empty contiguous parts such that the sum of the 
                            elements in the left partition is equal to the sum of the elements in the right partition. 
                            If Nikita can make such a move, she gets 1 point; otherwise, the game ends.

                            After each successful move, Nikita discards either the left partition or the right partition and continues 
                            playing by using the remaining partition as array arr.

                        Nikita loves this game and wants your help getting the best score possible. Given arr, can you find and print 
                        the maximum number of points she can score?
                        
    Approach:   This problem can be solved without Dynamic Programming in O(n) time using a simple logic. If the sum of the array is
                even, then the array can be splitted. Therefore, recursively search if the sum of the current split is even and if that 
                sum is possible in the array (This can be done by creating a prefix sum array and checking if the current sum is in the
                prefix sum).
'''

import os
from sys import stdin, stdout
from itertools import accumulate

def maxScore(prefixSum, left, right):
    splitSum = (left + right) // 2
    # Sum of the current split is odd ==> The array can't be splitted further.
    if ((left + right) % 2 == 0 and splitSum in partialSum):
        return 1 + max(maxScore(prefixSum, left, splitSum, maxScore(prefixSum, splitSum, right))
    return 0

def arraySplitting(arr):
    # If the array is all zeros, then we can split the array into n - 1 splits.
    if arr == [0] * len(arr):
        return len(arr) - 1
    s = sum(arr)
    prefixSum = list(accumulate(arr))
    return maxScore(prefixSum, 0, s)

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        arr_count = int(stdin.readline())
        arr = list(map(int, stdin.readline().rstrip().split()))
        result = arraySplitting(arr)
        stdout.write(str(result) + '\n')
