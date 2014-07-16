/*
 *  First triangle number with over 500 divisors
 */
#include <stdio.h>
#include <stdlib.h>
#include "../lib/sieve.h"
#include "math.h"
#include "string.h"
#include <vector>
#include <algorithm>

using namespace std;

#define TARGET_N_FACTORS 501
#define NUM 1000

// -------------------------------------------------------------------------- //
unsigned int triangle_number(unsigned int n) {
  if (n % 2 == 0) {
    return (n/2) * (n+1);
  }
  return ((n+1)/2) * n;
}

// -------------------------------------------------------------------------- //
bool isPerfectSquare(int x) {
  int t = (int)(sqrt(x));
  return t*t == x;
}

// -------------------------------------------------------------------------- //
bool isTriangleNumber(int x) {
  return isPerfectSquare(8*x + 1);
}

// -------------------------------------------------------------------------- //
int main (int argc, char **argv) {

  unsigned long long

  return 0;
}
