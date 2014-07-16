#ifndef SIEVE_H 
#define SIEVE_H

// Sieve of Eratoshtenes and related methods
class Sieve {

 public:

  Sieve();
  ~Sieve();

  void getPrimesUpTo(const unsigned int n, bool *list);
  void getPrimesUpToNFromMGivenListToM(const unsigned int N, bool *list_N,
      const unsigned int M, const bool *list_M);
  int getPrimeFactorsOfN(const unsigned int N, unsigned int *prime_factors, bool allocate);
  int getPrimeFactorsOfNWithSeedList(const unsigned int N, unsigned int *prime_factors, bool allocate,
      const unsigned int M, bool *seed_list);

};

#endif
