#include <iostream>
#include <string.h>
#include <stdio.h>

int main() {
    int prod;
    char prodStr[12];
    char prodStrRev[12];

    int largestPalin = 0; 


    for (int num1 = 100; num1 < 1000; num1 ++) {

        for (int num2 = 100; num2 < 1000; num2 ++) {

            prod = num1*num2;

            sprintf(prodStr, "%d", prod);
            sprintf(prodStrRev, "%d", prod);
            strrev(prodStrRev);

            // printf("the first number was %i, the second was %i, their product is %s and this reversed is %s\n",num1, num2, prodStr, prodStrRev);

            if (!strcmp(prodStr, prodStrRev) && prod > largestPalin) {

                largestPalin = prod;

            }

        }

    }

    printf("%i", largestPalin);

}