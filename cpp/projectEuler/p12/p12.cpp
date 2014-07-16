/*
 *  First triangle number with over 500 divisors
 */
#include <stdio.h>
#include <stdlib.h>
#include "math.h"
#include "string.h"
#include <vector>
#include <algorithm>
#include "../lib/sieve.h"

using namespace std;

// Shouldn't ever get to this many...
#define MAX_PRIME_FACTORS 50
#define TARGET_N_FACTORS 501
#define DEBUG 1

//#define INITIAL 1
#define INITIAL 12000

unsigned int triangle_number(unsigned int n) {
  if (n % 2 == 0) {
    return (n/2) * (n+1);
  }
  return ((n+1)/2) * n;
}

int number_of_divisors(unsigned int n) {
  int counter = 0;
  for (int i=1; (!(n % i) && counter++) || i <= (n/2); i++);
  return counter + 1;
}


int computeFactorsOfN2(unsigned int N, unsigned int *prime_factors, int n_prime_factors) {
  // Smarter way using sigma function
  // \sigma_0(n) = \prod_{i=1}^r (a_i + 1)
  // where r = # prime factors of n, a_i is the maximum power by which n is divisible by the i-th prime
  int prod = 1;
  for (int i=0; i < n_prime_factors; ++i) {
    unsigned int pi = prime_factors[i];
    unsigned int q = pi;
    int ai = 0;
    while (N % q == 0) {
      ai += 1;
      q *= pi;
    }
    prod *= ai + 1;
    //printf("prime_factor[%d] = %d : ai = %d\n", i, pi, ai);
  }
  return prod;
}

int computeFactorsOfN(unsigned int N, unsigned int *prime_factors, int n_prime_factors) {
  vector<int> factors;

  // Build factor list out of primes
  for (int i=0; i < n_prime_factors; ++i) {
    factors.push_back(prime_factors[i]);
  }

  // Build out all the factors
  for (int i = 0; i < factors.size(); ++i) {
    unsigned int p = factors[i];
    for (int j = 0; j < factors.size(); ++j) {
      unsigned int pq = p * factors[j];
      if (pq < N && N % pq == 0) {
        bool contains_pq = false;
        for (int k=0; k < factors.size(); ++k) {
          if (factors[k] == pq) {
            contains_pq = true;
          }
        }
        if (!contains_pq) {
          factors.push_back(pq);
        }
      }
    }
  }

  // Need to include 1 as a divisor as well as N, so +2
  factors.push_back(1);
  bool contains_N = false;
  for (int k=0; k < factors.size(); ++k) {
    if (factors[k] == N) {
      contains_N = true;
    }
  }
  if (!contains_N) {
    factors.push_back(N);
  }

  // deugging
  if (DEBUG == 1) {
    sort(factors.begin(), factors.end());
    for (int i = 0; i < factors.size(); ++i) {
      printf("%u, ", factors[i]);
    }
    printf("\n");
  }

  return factors.size();
}

// -------------------------------------------------------------------------- //

int main (int argc, char **argv) {

  Sieve sieve;
  int M = 504;
  unsigned int *prime_factors = new unsigned int [M];
  int m = sieve.getPrimeFactorsOfN(M, prime_factors, false);
  for (int i=0; i < m; ++i) {
    printf("%u, ", prime_factors[i]);
  }
  printf("\n");
  computeFactorsOfN(M, prime_factors, m);

  delete [] prime_factors;

  bool found = true;
  unsigned int n = INITIAL; // triangle number index
  unsigned int t = triangle_number(n);
  int n_factors = 0;
  while (!found) {
    t = triangle_number(n);
    n_factors = number_of_divisors(t);
    printf("n = %d : t = %u : n_factors = %d\n", n, t, n_factors);
    if (n_factors >= TARGET_N_FACTORS) {
      found = true;
      break;
    }
    n++;
  }


  if (found) {
    printf("n = %d : t = %u : n_factors = %d\n", n, t, n_factors);
  } else {
    printf("Something went wrong.\n");
  }

  return 0;
}
