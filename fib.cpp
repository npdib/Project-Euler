#include <iostream>

int main() {

    int sum = 0;

    int fib = 1;
    int prevFib = 1;
    int temp;

    while (fib < 4000000) {

        // printf("%i\n", fib);

        if (fib % 2 == 0) {

            sum += fib;

        }

        temp = fib;
        fib += prevFib;
        prevFib = temp;

    }

    printf("%i", sum);
}