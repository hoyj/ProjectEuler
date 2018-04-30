#include <stdio.h>
#include <stdlib.h>
#include <math.h>

char isPrime(int* arr, int n, int val){
	int sqrt_val = (int)sqrt((double)val);
	for(int i = 2; i <= sqrt_val; i++){
		if(arr[i] & (val % i == 0)){
			return 0;
		}
	}
	return 1;
}

char isCircularPrime(int* arr, int n, int prime, int len){
	int num = prime;
	for(int i = 0; i < len-1; i++){
		num = (num % 10) * (int)(pow(10, len-1)) + num / 10;
		if(arr[num])
			return 0;
	}
	return 1;
}

int main(int argc, char* argv[]){
	if(argc != 2){
		printf("./35 N\nN: natural number\n");
		exit(0);
	}
	int n = atoi(argv[1]);
	printf("n: %d\n", n);
	int* arr = NULL;

	arr = calloc(n, sizeof(int));
	arr[1] = 1;
	arr[2] = 0;
	arr[3] = 0;
	
	for(int i = 2; i < n; ++i){
		if(arr[i] == 1)
			continue;
		int ptr = i;
		arr[i] = isPrime(arr, n, i) ? 0 : 1;
		ptr += i;
		while(ptr < n){
			arr[ptr] = 1;
			ptr += i;
		}
	}	
	
	int len = 1;
	int nth = 10;
	int count = 0;
	for(int i = 2; i < n; ++i){
		if(i % nth == 0){
			nth *= 10;
			len += 1;
		}
		if(!arr[i]){
			if(isCircularPrime(arr, n, i, len)){
				printf("%d,", i);
				count += 1;
			}
		}
	}
	printf("\n");
	printf("counted: %d circular primes\n", count);
	return 0;
}
