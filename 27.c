#include <stdio.h>
#include <stdlib.h>
#include <math.h> // sqrt, floor
#include <string.h> //memset
#include <time.h> 

#define DEBUG 0
#define dprint(fmt, ...) \
	do { if (DEBUG) fprintf(stderr, fmt, __VA_ARGS__); } while (0)
time_t start, end;
char* nums = NULL; // keeps track of number status 1 = prime, 0 = composite
char* checked = NULL; // keeps track of numbers that went through primality test 1 = yes 0 = no
int size = 1000, offset = 1000;

void printArr(char* arr);

int f(int n, int a, int b){
	if( (1000 <= a) | (a <= -1000) | (1000 <= b) | (b <= -1000) ){
		printf("[ERROR] Invalid argument for f a:%d, b:%d\n", a,b);
		exit(0);
	}
	return n*n + a*n + b;
}

/*
 * resize array to current size + 100
 */
void resize(){
	int new_size = size + offset;
	char* new_nums = NULL, *new_checked = NULL;
	if( (new_nums = (char*)realloc(nums, new_size)) == NULL) {
		if(nums != NULL)
			free(nums);
		nums = NULL;
		printf("[ERROR] Unable to reallocate memory for nums\n");
		exit(0);
	}
	if( (new_checked = (char*)realloc(checked, new_size)) == NULL) {
		if(checked != NULL)
			free(checked);
		checked = NULL;
		printf("[ERROR] Unable to reallocate memory for checked\n");
		exit(0);
	}
	// below two lines using memset is necessary
	// since realloc, when cannot expand from current location,
	// will give a new memory address but DOES NOT INITIALIZE
	// new memory to a specific value. Only previous contents are copied.
	memset(new_nums+size, 0, offset);
	memset(new_checked+size, 0, offset);
	nums = new_nums;
	checked = new_checked;
	size = new_size;
}

void printArr(char* arr){
	printf("----------\n");
	for(int i = 0; i < size; i++)
		printf("%d: %d\n", i, arr[i]);
        printf("----------\n");	
}

/*
 * given integer n, check whether n is prime through trial division
 * check if bit for the integer has already been set as 1 which indicates,
 * it has gone through the test and is a prime.
 */
int isPrime(int n) {
	if(n < 2)
		return 0;

	dprint("Checking isPrime(%d)\n", n);
	if(n >= size){
		dprint("%s\n", "Resize array");
		resize();
	}

	if(checked[n]){
		dprint("Already checked %d. It is %s\n", n, nums[n] == 1 ? "Prime" : "Composite");
		return nums[n];
	}else{
		int n_sqrt = (int)floor(sqrt((double)n));
		for(int i = 2; i <= n_sqrt; ++i){
			if( isPrime(i) & (n % i == 0) ){
				dprint("%d is divisible by %d and thus is not prime\n", n, i);
				checked[n] = 1;
				nums[n] = 0;
				return 0;
			}
		}
		dprint("%d is prime\n", n);
		checked[n] = 1;
		nums[n] = 1;
		return 1;
	}
}

int main(){
	start = clock();
	nums = (char*)calloc(size, 1);
	checked = (char*)calloc(size, 1);
	int max = 0, max_a, max_b;
	for(int a = -999; a < 1000; a++){
		for(int b = -999; b < 1000; b++){
			int n = 0;
			int count = 0;
			int res = isPrime(f(n,a,b));
			while(isPrime(f(n++,a,b)))
				count += 1;
			//printf("a:%d, b:%d, count: %d\n", a, b, count);
			if(count > max){
				max = count;
				max_a = a;
				max_b = b;
			}
		}
	}
	printf("max_a:%d, max_b:%d, max: %d\n", max_a, max_b, max);
	printf("%d x %d = %d\n", max_a, max_b, max_a * max_b);
	end = clock();
	printf("Time taken: %ldms\n", (1000*(end-start)/CLOCKS_PER_SEC));
	free(nums);
	free(checked);
	nums = NULL;
	checked = NULL;
	return 0;
}
