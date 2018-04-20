/*
 * Project Euler Problem #29
 */

#include <stdio.h>
#include <string.h>

char nums[601] = {0};

int count(int n){
	int res = 0;
	for(int i = 1; i <= n; i++)
		for(int b = 2; b < 101; b++)
			if(nums[i*b] == 0){
				res += 1;
				nums[i*b] = 1;
			}
	memset(nums, 0, 601);
	return res;	
}

int main(){
	//2 4, 8, 16, 32, 64
	// 3, 9, 27, 81
	// 5, 25
	// 6, 36
	// 7, 49
	// 10, 100
	int sum = 8019;
	sum = 8019 + count(6) + count(4) + 4 * count(2);
	printf("sum: %d\n", sum);
	return 0;
}
