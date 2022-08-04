#include <iostream>
#include <math.h>

bool isPrime(double n) {

    bool prime = true;

    for (int i = 2; i <= sqrt(n); i ++) {

        if (fmod(n, i) == 0) {
            prime = false;
            break;
        }

    }

    return prime;

}



int main() {

    double num = 600851475143;

    printf("%f", num);

    for (double i = floor(sqrt(num)); i > 0; i --) {

        if (isPrime(i) && (fmod(num, i) == 0)) {

            printf("The largest prime divisor of %f is %f", num, i);
            break;

        }

    }
}