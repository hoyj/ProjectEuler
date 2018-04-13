/*
 * Project Euler Problem #25
 *
 * What's the first fibonacci number that has 1000digits?
 */
#include <stdio.h>

int DIGITS = 1000;

void add(int* cur, int* cur_digits, int* next, int* next_digits) {
	// we can assume the next_digits >= cur_digits
	int carry = 0;
	int res = 0;
	for(int i = 0; i < *next_digits; i++) {
		res = cur[i] + next[i] + carry;
		if(res >= 10) {
			carry = res / 10;
			res = res % 10;
		}else{
			carry = 0;
		}
		cur[i] = next[i];
		next[i] = res;
	}
	if(carry != 0) {
		next[*next_digits] = carry;
	}

	*cur_digits = *next_digits;
	*next_digits = (carry == 0) ? *next_digits: *next_digits + 1;
	return;
}

void print_arr(int* arr, int size){
	for(int i = size-1; i >= 0; --i)
		printf("%d", arr[i]);
}

int main() {
	int cur[1000] = {0, };
	int next[1000] = {0, };
	int cur_digits, next_digits, count;
	cur[0] = 1;
	next[0] = 1;
	cur_digits = 1;
	next_digits = 1;
	count = 1;

	while(cur_digits != DIGITS) {
		printf("F%d:", count);
		print_arr(cur, cur_digits);
		printf("\n");
		add(cur, &cur_digits, next, &next_digits);
		count += 1;
	}
	printf("F%d:", count);
	print_arr(cur, cur_digits);
	printf("\n");
	return 0;
}

