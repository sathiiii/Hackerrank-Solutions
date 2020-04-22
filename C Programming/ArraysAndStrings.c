#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int digitFreq[10] = {0};
    char c;
    while (scanf("%c", &c) == 1)
        if (c >= '0' && c <= '9')
            digitFreq[c - '0']++;
    for (int i = 0; i < 10; i++)
        printf("%d ", digitFreq[i]);
}
