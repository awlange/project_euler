#ifndef FIBONACCI_H
#define FIBONACCI_H

// Simple fibonacci calculator
unsigned int fibonacci(unsigned int n);

#define FIBONACCI_MAX_STORED_NUMBER 64

// Fibonacci class
class Fibonacci {

 public:

  Fibonacci();
  ~Fibonacci();

  unsigned long long int getFibonacci(const int n);

 private:
  void init();

  unsigned long long int *storedNumbers;

};

#endif
