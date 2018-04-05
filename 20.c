/*
 * Project Euler Problem #20
 * Find the sum of the digits of 100!.
 */

#include <stdio.h>

#define MAX 256

int multiply(int n, int digits[], int size)
{
  int carry = 0;
  for(int i = 0; i < size; i++)
  {
    int new_val = digits[i] * n + carry;
    carry = new_val / 10;
    digits[i] = new_val % 10;
  }
  while(carry != 0)
  {
    digits[size++] = carry % 10;
    carry /= 10;
  }
  return size;
}

int main()
{
  int digits[MAX];
  digits[0] = 1;
  int size = 1, sum = 0;
  int num;
  printf("Input number to find factorial: ");
  scanf("%d", &num);

  for(int i = 1; i <= num; i++)
  {
    size = multiply(i, digits, size);
  }
  for(int i = size-1; i >= 0; i--)
  {
    sum += digits[i];
    printf("%d", digits[i]);
  }
  printf("\ndigits sum = %d\n", sum);
  return 0;
}
