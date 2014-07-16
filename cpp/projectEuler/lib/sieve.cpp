#include "stdlib.h"
#include "string.h"
#include "sieve.h"
#include "primetest.h"
#include "math.h"
#include <vector>

// ---------------------------------------------------------------------------------- //
Sieve::Sieve() {}

// ---------------------------------------------------------------------------------- //
Sieve::~Sieve() {}

// ---------------------------------------------------------------------------------- //
void Sieve::getPrimesUpTo(const unsigned int n, bool *list) {
  // For convenience, let list be of size n+1, so that we can use list[n] as indexing.
  // For example, list[4] = false

  // Initialize all to true
  memset(list, 1, (n+1) * sizeof(bool));

  for (unsigned int i = 2; i*i <= n; ++i) {
    if (list[i]) {
      for (unsigned int j = i*i; j <= n; j += i) {
        list[j] = false;
      }
    }
  }
}

// ---------------------------------------------------------------------------------- //
void Sieve::getPrimesUpToNFromMGivenListToM(const unsigned int N, bool *list_N,
    const unsigned int M, const bool *list_M) {

  // Same as getPrimesUpToN except that we are provided a list up to M already
  // For convenience, let list be of size n+1, so that we can use list[n] as indexing.

  // Copy list_M, initialize rest to true
  memcpy(list_N, list_M, (M+1) * sizeof(bool));
  memset(list_N + M+1, 1, (N - M) * sizeof(bool));

  // Do the usual sieve. Advantage is that several will already be false from list_M. 
  // There might be more optimization still available, but this will suffice.

  for (unsigned int i = 2; i*i; ++i) {
    if (list_N[i]) {
      for (unsigned int j = i*i; j <= N; j += i) {
        list_N[j] = false;
      }
    }
  }
}

// ---------------------------------------------------------------------------------- //
int Sieve::getPrimeFactorsOfN(const unsigned int N, unsigned int *prime_factors, bool allocate) {
  // Generate all primes up to bound with sieve
  bool *list = new bool [N+1];
  getPrimesUpTo(N, list);

  // Of the list of primes, only keep the ones that divide N (ignore 1)
  std::vector<unsigned int> vector_prime_divisors;
  for (unsigned int i = 2; i <= N; ++i) {
    if (list[i] && N % i == 0) {
      vector_prime_divisors.push_back(i);
    }
  }

  // Clean up no long needed memory
  delete [] list;

  // Convert vector to array
  if (allocate) {
    prime_factors = new unsigned int [vector_prime_divisors.size() + 1];
  }
  for (int i=0; i<vector_prime_divisors.size(); ++i) {
    prime_factors[i] = vector_prime_divisors[i];
  }

  return vector_prime_divisors.size();
}

// ---------------------------------------------------------------------------------- //
int Sieve::getPrimeFactorsOfNWithSeedList(const unsigned int N, unsigned int *prime_factors, bool allocate,
    const unsigned int M, bool *seed_list) {
  // Generate all primes up to bound with sieve
  bool *list = new bool [N];
  getPrimesUpToNFromMGivenListToM(N, list, M, seed_list);

  // Of the list of primes, only keep the ones that divide N (ignore 1)
  std::vector<unsigned int> vector_prime_divisors;
  for (unsigned int i = 2; i <= N; ++i) {
    if (list[i] && N % i == 0) {
      vector_prime_divisors.push_back(i);
    }
  }

  // Clean up no long needed memory
  delete [] list;

  // Convert vector to array
  if (allocate) {
    prime_factors = new unsigned int [vector_prime_divisors.size()];
  }
  for (int i=0; i<vector_prime_divisors.size(); ++i) {
    prime_factors[i] = vector_prime_divisors[i];
  }

  return vector_prime_divisors.size();
}
