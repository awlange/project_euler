/*
 * Fibonacci number functions
 */

#include "stdlib.h"
#include "fibonacci.h"

// Simple
unsigned int fibonacci(unsigned int n) {
  if (n == 0 || n == 1) {
    return 1;
  }
  return fibonacci(n-1) + fibonacci(n-2);
}

// More advanced class stuff
Fibonacci::Fibonacci() {
  storedNumbers = NULL;

  // meh, just put the init in here
  init();
}

Fibonacci::~Fibonacci() {
  if (storedNumbers != NULL) {
    delete [] storedNumbers;
  }
}

void Fibonacci::init() {
  storedNumbers = new unsigned long long int [FIBONACCI_MAX_STORED_NUMBER + 1];

  storedNumbers[0] = 1;
  storedNumbers[1] = 1;
  storedNumbers[2] = 2;
  storedNumbers[3] = 3;
  storedNumbers[4] = 5;
  storedNumbers[5] = 8;
  storedNumbers[6] = 13;
  storedNumbers[7] = 21;
  storedNumbers[8] = 34;
  storedNumbers[9] = 55;
  storedNumbers[10] = 89;
  storedNumbers[11] = 144;
  storedNumbers[12] = 233;
  storedNumbers[13] = 377;
  storedNumbers[14] = 610;
  storedNumbers[15] = 987;
  storedNumbers[16] = 1597;
  storedNumbers[17] = 2584;
  storedNumbers[18] = 4181;
  storedNumbers[19] = 6765;
  storedNumbers[20] = 10946;
  storedNumbers[21] = 17711;
  storedNumbers[22] = 28657;
  storedNumbers[23] = 46368;
  storedNumbers[24] = 75025;
  storedNumbers[25] = 121393;
  storedNumbers[26] = 196418;
  storedNumbers[27] = 317811;
  storedNumbers[28] = 514229;
  storedNumbers[29] = 832040;
  storedNumbers[30] = 1346269;
  storedNumbers[31] = 2178309;
  storedNumbers[32] = 3524578;
  storedNumbers[33] = 5702887;
  storedNumbers[34] = 9227465;
  storedNumbers[35] = 14930352;
  storedNumbers[36] = 24157817;
  storedNumbers[37] = 39088169;
  storedNumbers[38] = 63245986;
  storedNumbers[39] = 102334155;
  storedNumbers[40] = 165580141;
  storedNumbers[41] = 267914296;
  storedNumbers[42] = 433494437;
  storedNumbers[43] = 701408733;
  storedNumbers[44] = 1134903170;
  storedNumbers[45] = 1836311903;
  storedNumbers[46] = 2971215073;
  storedNumbers[47] = 4807526976;
  storedNumbers[48] = 7778742049;
  storedNumbers[49] = 12586269025;
  storedNumbers[50] = 20365011074;
  storedNumbers[51] = 32951280099;
  storedNumbers[52] = 53316291173;
  storedNumbers[53] = 86267571272;
  storedNumbers[54] = 139583862445;
  storedNumbers[55] = 225851433717;
  storedNumbers[56] = 365435296162;
  storedNumbers[57] = 591286729879;
  storedNumbers[58] = 956722026041;
  storedNumbers[59] = 1548008755920;
  storedNumbers[60] = 2504730781961;
  storedNumbers[61] = 4052739537881;
  storedNumbers[62] = 6557470319842;
  storedNumbers[63] = 10610209857723;
  storedNumbers[64] = 17167680177565;
}

unsigned long long int Fibonacci::getFibonacci(const int n) {
  if (n < FIBONACCI_MAX_STORED_NUMBER) {
    return storedNumbers[n];
  }

  unsigned long long int last = storedNumbers[FIBONACCI_MAX_STORED_NUMBER - 1];
  unsigned long long int nextToLast = storedNumbers[FIBONACCI_MAX_STORED_NUMBER - 2];
  unsigned long long int result;

  for(unsigned int i = FIBONACCI_MAX_STORED_NUMBER; i <= n; ++i){
    result = last + nextToLast;
    nextToLast = last;
    last = result;
  }

  return result;
}
