// Simple primality test

// 10001st prime

#include "math.h"
#include <iostream>

using namespace std;

#define NUMBER 10001
//#define NUMBER 200

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

  int i = 0;
  unsigned long n = 3;
  int n_found = 2; // already know 2 and 3
  unsigned long m = 6;

  while (n_found < NUMBER) {
    if (isPrime(m-1)) {
      ++n_found;
      cout << n_found << ": " << m-1 << endl;
      if (n_found == NUMBER) {
        n = m-1;
        break;
      }
    }
    if (isPrime(m+1)) {
      ++n_found;
      cout << n_found << ": " << m+1 << endl;
      if (n_found == NUMBER) {
        n = m+1;
        break;
      }
    }
    m += 6;
  }

  return 0;
}
