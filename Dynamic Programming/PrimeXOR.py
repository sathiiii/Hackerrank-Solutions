'''
    Problem Statement:  Penny has an array of a integers, [a0, a1, ..., a(n - 1)]. She wants to find the number of unique multisets she 
    can form using elements from the array such that the bitwise XOR of all the elements of the multiset is a prime number. Recall that a 
    multiset is a set which can contain duplicate elements. Given q queries where each query consists of an array of integers, 
    can you help Penny find and print the number of valid multisets for each array? As these values can be quite large, modulo each 
    answer by 10 ^ 9 + 7 before printing it on a new line.
    
    Constraints:   1 <= q <= 10
                   1 <= n <= 10^5
                   3500 <= ai <= 4500
    
    Approach:  Breaking the problem down into two problems: First we have to find the number of subsets of each which gives XOR sums upto 
               maximum possible XOR sum. Then we have to filter out only the counts of the subsets which have prime XOR sums. Both of
               these problems require Dynamic Programming. 
               But first we have to focus about given constraints. There will be only 1001 (4500 - 3500 + 1) integers at most. The maximum 
               possible XOR sum can be found using the maximum possible integer of the array, which is 4500.
               For example: Suppose the maximum possible integer that the array can contain is 10 (1100 in binary). Then the maximum
               XOR sum is when the 4 bits are all set (1111). (One possibility is 1100 ^ 0011 = 1111).
               The number of bits required to represent 4500 is log2(4500). Therefore, the maximum XOR sum is 2 ^ (log2(4500) + 1) - 1.
               Hence, the range of the XOR sum is [0, 2 ^ (log2(4500) + 1) - 1].
               Sieving the prime numbers in the above range will also make the solution efficient. It can be done in many ways. I've used
               Sieve of Eratosthenes.
               
    (01). Subproblem:   dp[i][j] 
                        Number of subsets which gives XOR sum of j, using the numbers in range [3500, i].
                        #subproblems = 1001 * 2 ^ (log2(4500) + 1) = 1001 * 8192
    (02). Guessing:     dp[i][j] consists of two disjoint subproblems:
                            (1). dp[i - 1][j], i has no effect on XOR sum.
                            (2). dp[i - 1][j ^ i], i has an effect on XOR sum.
                        In the 1st case, dp[i][j] must be dp[i - 1][j] + XORSumOf(even number of i's) (Because XOR sum of even number of
                        i's result 0).
                        In the 2nd case, dp[i][j] must be dp[i- 1][j ^ i] + XORSumOf(odd number of i's).
                        Therefore, the guess to make is if the subset contains odd or even number of i's.
    (03). Recurrence:   
    (04). Toplogical Order:
    (05). Original Problem: sum(dp[-1][j] for all j if j is prime)
'''

