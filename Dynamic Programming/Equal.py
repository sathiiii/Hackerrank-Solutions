'''
    Problem Statement: Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. 
    She is biased towards her friends and plans to give them more than the others. One of the program managers hears of this and tells her 
    to make sure everyone gets the same number. To make things difficult, she must equalize the number of chocolates in a series of 
    operations. For each operation, she can give 1, 2 or 5 chocolates to all but one colleague. Everyone who gets chocolate in a round receives 
    the same number of pieces.
    For example, assume the starting distribution is [1, 2, 5]. She can give 2 bars to the first two and the distribution will be [3, 3, 5]. 
    On the next round, she gives the same two 2 bars each, and everyone has the same number: [5, 5, 5]

    Given a starting distribution, calculate the minimum number of operations needed so that every colleague has the same number 
    of chocolates.
'''

def equal(arr):
    # Aim for the minimum (Because that will consume the least number of operations). Try to get all values to the minimum.
    m = min(arr)
    result = float("inf")
    # But will the minimum always be the optimal solution? Therefore, guess the optimal solution between min and min - 4.
    for offset in range(5):
        operations = 0
        for i in arr:
            # The value we need to subtract to reach the minimum
            t = i - (m - offset)
            # How many times do we have to subtract by 5 -> t //5
            # After subtracting by 5, how many times do can we subtract by 2 -> (t % 5) // 2
            # Finally, how many times do we have to subtract by 1 (or the remainder after subtracting 5s and 2s) -> t % 5 % 2
            operations += t // 5 + (t % 5) // 2 + (t % 5) % 2
        result = min(result, operations)    # Select the optimal solution
    return result
