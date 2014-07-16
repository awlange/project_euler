#include <stdio.h>
#include "../lib/fibonacci.h"

using namespace std;

int main (int nargs, char** argv) {

  Fibonacci fibo;

  int i = 0;
  unsigned long long currentFibo = fibo.getFibonacci(i);

  unsigned long long sum = 0;

  while (currentFibo < 4000000) {
    sum += (currentFibo % 2 == 0) ? currentFibo : 0;
    i++;
    currentFibo = fibo.getFibonacci(i);
  }

  printf("%lld\n", sum);

  return 0;
}
