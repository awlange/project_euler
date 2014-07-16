/*
 * What is the largest prime factor of the number 600851475143 ?
 */

#define NUMBER 600851475143
#define NSQRT 775121

#include <stdio.h>
#include <stdlib.h>
#include "../lib/sieve.h"
#include "../lib/primetest.h"
#include "math.h"
#include "string.h"

using namespace std;

int main (int argc, char **argv) {

  // Largest prime factor bound (? still not sure why this worked)
  // b/c if n = a*b, then a and b must both be equal or less than n^0.5
  // and since we are counting up, we should have already seen lower primes
  unsigned int nsqrt = (unsigned int)sqrt(NUMBER);

  // Generate all primes up to bound with sieve
  bool *list = new bool [nsqrt + 1];
  Sieve sieve;
  sieve.getPrimesUpTo(nsqrt, list);

  // Of the list of primes, only keep the ones that divide NUMBER
  unsigned int max = 1;
  for (unsigned int i = 1; i < nsqrt; ++i) {
    if (list[i] && NUMBER % i == 0) {
      max = i;
    }
  }

  printf("max: %d\n", max);

  delete [] list;

  return 0;
}
