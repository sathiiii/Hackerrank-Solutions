/*
    Problem Statement:    https://www.hackerrank.com/challenges/red-john-is-back/problem
    
    Approach:   This problem can be solved using Dynamic Programming and Sieve of Eratosthenes (Or any other algorithm for sieving
    primes) easily.
*/
#include <bits/stdc++.h>

using namespace std;

int dp[61];
bool prime[10000001];

void sieveOfEratosthenes(int n) 
{
    memset(prime, true, sizeof(prime)); 
    for (int p = 2; p * p <= n; p++) 
    {
        if (prime[p] == true) 
        {
            for (int i = p * p; i <= n; i += p) 
                prime[i] = false;
        } 
    }
} 

int redJohn(int n) {
    dp[0] = dp[1] = dp[2] = dp[3] = 1;
    for (int i = 4; i <= n; i++)
        dp[i] = dp[i - 1] + dp[i - 4];
    int count = 0;
    for (int i = 2; i <= dp[n]; i++) {
        if (prime[i])
            count++;
    }
    return count;
}
