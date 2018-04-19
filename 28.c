/*
 * Project Euler Problem #28
 *
 * Approach:
 * 	1) the numbers to be added on the outer circle grow by 2*n
 * 	where n is the nth circle with 1 as start.
 * 	ex)
 * 	21 22 23 24 25
 * 	20  7  8  9 10
 * 	19  6  1  2 11
 * 	18  5  4  3 12
 * 	17 16 15 14 13
 *
 * 	1 is in the 1st circle n = 1
 * 	3,5,7,9 are in the 2nd circle n = 2 and thus grow by 4
 * 	13,17,21,25 are in the 3rd circle n = 3 and thus grow by 6
 */
#include <stdio.h>
#define SIZE 1001
int main(){
	int max = SIZE * SIZE;
	int degree = 2;
	int n = 1;
	int sum = 0;
	int count = 0;
	while(n <= max){
		//printf("Add %d\n", n);
		sum += n;
		n += degree;
		count += 1;
		if(count % 4 == 0){
			count = 0;
			degree += 2;
		}
	}
	printf("Sum: %d\n", sum);
}
