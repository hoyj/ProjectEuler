/*
 * Project Euler Problem #23
 *
 * A perfect number is a number for which the sum of its proper divisors is 
 * exactly equal to the number. For example, the sum of the proper divisors 
 * of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect 
 * number.
 *
 * A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
 *
 * As 12 is the smallest abundant number, 1+2+3+4+6 = 16, the smallest number 
 * that can be written as the sum of two abundant numbers is 24. By 
 * mathematical analysis, it can be shown that all integers greater than 28123 
 * can be written as the sum of two abundant numbers. However, this upper 
 * limit cannot be reduced any further by analysis even though it is known 
 * that the greatest number that cannot be expressed as the sum of two 
 * abundant numbers is less than this limit.
 *
 * Find the sum of all the positive integers which cannot be written as the 
 * sum of two abundant numbers.
 */
#include <stdio.h>
#include <math.h> // sqrt, pow
#include <stdlib.h> //exit

int MAX_VAL = 28123;
int MIN_ABUNDANT_NUMBER = 12;

/*
 * int isAbundant(int n)
 *
 * :param n: number to check if abundant
 *
 * description:
 * 	1) find if abundant number
 * 	1-a) Find divisors other than itself
 * 	1-b) Find sum and compare
 */
int isAbundant(int n){
    double d = sqrt((double)n);
    int sum = 1;
    for(int i = 2; i <= d; i++) {
	if(n % i == 0) {
	    //printf("i = %d, sum = %d\n", i, sum);
	    if(i * i == n) 
		sum += i;
	    else
	        sum += i + n / i;
	}
    }
    return (sum > n) ? 1 : 0;
}

void test_isAbundant() {
    printf("12 is abundant? %s\n", isAbundant(12) ? "true" : "false");
}

int main() {
    char bit_array[28124] = {0, }; //28123 + 0 keeps track of abundunt numbers
    char bool_array[28124] = {0, };
    int size = 28124;
    int ab_count = 0;

    for(int i = 12; i < 28124; i++) // since 12 is the min abundant number
        if(isAbundant(i)) {
            bit_array[i] = bit_array[i] | 1;
	    ab_count += 1;
	}

    printf("total of %d abundunt number discovered.\n", ab_count);
    int* ab_arr = (int*)malloc(sizeof(int) * ab_count);
    int ab_arr_index = 0;
    for(int i = 0; i < size; i++)
	if(bit_array[i] == 1)
	    ab_arr[ab_arr_index++] = i;

    for(int i = 0; i <= ab_count; i++)
    {
	for(int j = i; j <= ab_count; j++)
	{
	    int total = ab_arr[i] + ab_arr[j];
	    if(total > 28123) break;
	    if(bool_array[total] == 0) {
		bool_array[total] = 1;
//		printf("%d\n", total);
	    }
	}
    }
    int sum = 0;
    for(int i = 0; i < 28124; i++)
	if(bool_array[i] == 0)
	    sum += i;

    printf("sum = %d\n", sum);
    return 0;
}
