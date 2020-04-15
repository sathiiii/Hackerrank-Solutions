'''
    Copyright (C) 2020, Sathira Silva
    
    Problem Statement: You can perform the following operations on the string, a:
                       (1). Capitalize zero or more of a's lowercase letters.
                       (2). Delete all of the remaining lowercase letters in a.
    Given two strings, a and b, determine if it's possible to make a equal to b as described. If so, print YES on a new line. 
    Otherwise, print NO.
    
    Approach: This's a variant of the Edit Distance problem. There two operations available. We have to check whether b is a
              subsequence(since we cannot change the order) of a with the constraint that a can only discard lower case characters.
    
    (01). Subproblem: suffixes of a and b, a[:i] and b[:j]. Is b[:j] a subsequence of a[:i]?
                      #subproblems = nm
          
    (02). Guessing:   Check one of two possibilities (Try them all):
                          (1). Delete a[i] if a[i] is lower and doesn't match with b[j].
                          (2). Capitalize a[i] if a[i] is lower case.
                          
    (03). Recursion:      (1). If a[i] is upper and a[i] == b[j],   dp[i + ][j + 1] = dp[i][j]
                               (If a[i] is lower and matches with b[j], b[:j + 1] is an abbreviation of a[:j + 1] only if b[:j] is an
                               abbreviation of a[:i])   
                          (2). If a[i] is lower (Capitalize or Delete),
                                  if a[i].upper() == b[j],  dp[i + ][j + 1] = dp[i][j] or dp[i][j + 1]
                                  (when a[i] is capitalized it matches with b[j], if either b[:j + 1] is an abbreviation of a[:i + 1] or
                                  b[:j + 1] is an abbreviation of a[:i], b[:j + 1] is an abbreviation of a[:i + 1]).
                                  else dp[i + ][j + 1] = dp[i][j + 1]
                                  (Otherwise(when a[i] is capitalized it doesn't match with b[j]), b[:j + 1] is an abbreviation of 
                                  a[:i + 1] only if b[:j + 1] is an abbreviation of a[:i])
                         
   (04). Topological Order: The order doesn't matter.
   (05). Original Problem:  dp[-1][-1] (Is b an abbreviation of a?)
   
   Time Complexity: O(|a||b|)
'''

def abbreviation(a, b):
    dp = [[False] * (len(b) + 1) for _ in range(len(a) + 1)]
    # Base Case: empty b is an abbreviation of empty a)
    dp[0][0] = True
    # When b is empty, if a[i] is lower, b is an abbreviation of a if all of the previous letters of a were lower.
    # (If all of the letters of a can be deleted b is an abbreviation a)
    for i in range(len(a)):
        if not a[i].isupper():
            dp[i + 1][0] = dp[i][0]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i].isupper() and a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j]
            if not a[i].isupper():
                if a[i].upper() == b[j]:
                    dp[i + 1][j + 1] = dp[i][j] or dp[i][j + 1]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]
    return "YES" if dp[-1][-1] else "NO"
