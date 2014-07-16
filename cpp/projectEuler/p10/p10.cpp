// Simple primality test

// Sum of primes below 2 million 

#include "math.h"
#include <iostream>

using namespace std;

#define LIMIT 2000000

bool isPrime(const unsigned long n) {

  // Base for loop
  if (n < 3) return true;

  // Quick even check to let loop have stride of 2
  //if (n % 2 == 0) return false;

  // Factorization bound
  unsigned int sqrtn = (unsigned int)sqrt(n);

  // Skip all even numbers b/c those are obviously not prime
  for (unsigned int i = 3; i <= sqrtn; i += 2) {
    if (n % i == 0) {
      return false;
    }
  }

  return true;
}

int main(int argc, char **argv) {
  unsigned long sum = 2 + 3;
  for (unsigned long i=6; i<LIMIT; i += 6) {
    if (isPrime(i-1)) {
      sum += i-1;
    }
    if (isPrime(i+1)) {
      sum += i+1;
    }
  }
  cout << sum << endl;

  return 0;
}
