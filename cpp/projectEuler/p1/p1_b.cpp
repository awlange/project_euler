#include <stdio.h>

using namespace std;

#define MAX 999

int sumDivisibleBy(int n) {
  int p = MAX / n;
  return n*(p*(p + 1))/2;
}

int main(int nargs, char** argv) {
  printf("%d\n", sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15));
  return 0;
}
