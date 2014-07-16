#include <stdio.h>
int number_of_divisors(int n) {
  int counter = 0;
  for (int i=1; (!(n % i) && counter++) || i <= (n/2); i++);
  return counter + 1;
}

int main() {

  for (int i = 3; i <= 20; ++i) {
    printf("%d : %d\n", i, number_of_divisors(i));
  }

  return 0;
}
