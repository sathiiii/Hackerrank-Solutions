#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MIN_ELEMENT 1
#define MAX_ELEMENT 1000000
int  sum (int count,...) {
    va_list args;
    va_start(args, count);
    int sum = 0;
    for (int i = 0; i < count; i++) {
        sum += va_arg(args, int);
    }
    return sum;
}

int min(int count,...) {
    va_list args;
    va_start(args, count);
    int m = 0;
    for (int i = 0; i < count; i++) {
        int next = va_arg(args, int);
        if (next < m)
            m = next;
    }
    return m;
}

int max(int count,...) {
    va_list args;
    va_start(args, count);
    int m = 0;
    for (int i = 0; i < count; i++) {
        int next = va_arg(args, int);
        if (next > m)
            m = next;
    }
    return m;
}
