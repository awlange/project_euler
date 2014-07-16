// Simple primality test

#include "math.h"
#include <stdio.h>

bool isPrime(const unsigned int n) {

  // Base for loop 
  if (n < 3) return true;

  // Quick even check to let loop have stride of 2
  if (n % 2 == 0) return false;

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
