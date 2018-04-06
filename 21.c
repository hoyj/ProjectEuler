#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/*
 * d(n)
 * :param n: integer
 * description: find sum of proper divisors of n
 * (numbers less than n which divide evenly into n)
 */
int d(int n)
{
  int sum = 1;

  for(int i = 2; i <= sqrt(n); i++)
    if(n % i == 0)
      sum += i + (n / i);

  return sum;
}

int main(int argc, char **argv)
{
  int nums[10001] = {0};
  int sum = 0;
  int size = 10000;
  if(argc > 1)
    size = atoi(argv[1]);

  for(int i = 0; i <= size; i++)
  {
    if(nums[i] == 0)
    {
      int j = d(i);
      if(i != j && d(j) == i && j <= size)
      {
        sum += i + j;  
	nums[j] = 1;
	printf("%d, %d\n", i, j);
      }
      nums[i] = 1;
    }
  }
  printf("Sum = %d\n", sum);
  return 0;
}
