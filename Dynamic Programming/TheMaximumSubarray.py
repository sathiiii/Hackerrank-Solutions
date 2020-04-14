'''
    Copyright (C) 2020, Sathira Silva
    
    Problem Statement: We define subsequence as any subset of an array. We define a subarray as a contiguous subsequence in an array.
    Given an array, find the maximum possible sum among:
    (1). all nonempty subarrays.
    (2). all nonempty subsequences.
    Print the two values as space-separated integers on one line.

    Note that empty subarrays/subsequences should not be considered.
    
    Approach: Finding the maximum possible sum of all subsequences is really simple. If the array isn't all negative, the maximum 
    possible sum of all subsequences is just the sum of all elements. Otherwise, the minimum element in the array.
    Finding the maximum possible sum of all subsets is bit challenging. Because we have to find the sum of all 2^n - 1 subsets. 
    But Dynamic Programming can handle this very easily. (This approach is also known as Kadane's Algorithm)
    
    (01). Subproblem: currentSubarraySum
                      The maximum sum of subarray ending at current element.
                      #subproblems = n
    (02). Guessing:   Did previous subarray contain all negative integers?
    (03). Recurrence: currentSubarraySum = element + max(0, currentSubarraySum)
    (04). Topological order: The order of the original array.
    (05). Original problem: Maximum of all subarray sums.
    
    Time Complexity: O(n)
'''

def maxSubarray(arr):
    subarrayMax = float("-inf")
    currentSubarraySum = 0
    for element in arr:
        # This line is equivalent to: currentSubarraySum = element + max(0, currentSubarraySum)
        currentSubarraySum = max(element, currentSubarraySum + element)
        subarrayMax = max(subarrayMax, currentSubarraySum)
    arr.sort()
    subsequenceMax = arr[-1] if arr[-1] <= 0 else sum(n for n in arr if n > 0)
    return subarrayMax, subsequenceMax
