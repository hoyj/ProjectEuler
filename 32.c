/*
 * Project Euler Problem #32
 *
 * Find sum of 1~9 pandigital number
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * to be palindigital
 * 1. contain no 0's
 * 2. each digit should be unique
 */

int getLen(int n){
	int tmp = n;
	int count = 0;
	while(tmp != 0){
		tmp /= 10;
		count += 1;
	}
	return count;
}



char checkUnique(char* s, int a, int b, int c){
	const int max_size = 10;
	char const digit[] = "0123456789";
	char unique[10] = {0};
	int tmp = a;
	int index = 0;
	int d;
	while(tmp != 0){
		if(index == max_size)
			return 0;
		d = tmp % 10;
		if(d == 0)
			return 0;
		if(unique[d] == 1)
			return 0;
		strncpy(s+index, digit+d, 1);
		unique[d] = 1;
		index += 1;
		tmp /= 10;
	}
	tmp = b;
	while(tmp != 0){
		if(index == max_size)
			return 0;
		d = tmp % 10;
		if(d == 0)
			return 0;
		if(unique[d] == 1)
			return 0;
		strncpy(s+index, digit+d, 1);
		unique[d] = 1;
		index += 1;
		tmp /= 10;
	}
	tmp = c;
	while(tmp != 0){
		if(index == max_size)
			return 0;
		d = tmp % 10;
		if(d == 0)
			return 0;
		if(unique[d] == 1)
			return 0;
		strncpy(s+index, digit+d, 1);
		unique[d] = 1;
		index += 1;
		tmp /= 10;
	}
	return 1;
}

int isPandigital(int a, int b, int c){
	char const digit[] = "0123456789";
	if(getLen(a) + getLen(b) + getLen(c) != 9)
		return 0;
	char* s = calloc(10, 1);
	char isUnique = checkUnique(s, a,b,c);
	if(isUnique == 0){
		return 0;
	}
	free(s);
	return c;
}

char found(int* ans, int size, int n){
	for(int i = 0; i < size; i++)
		if(ans[i] == n)
			return 1;
	return 0;
}

void resize(int* ans, int *size){
	printf("RESIZE\n");
	int* new_ans = realloc(ans, *size + 5);
	if(new_ans == NULL){
		free(ans);
		printf("[ERROR] Unable to allocate memeory\n");
		exit(0);
	}
	ans = new_ans;
	*size += 5;
       	return;	
}

int main(){ // a = 1 , b = 4, c = 4
	int a,b;
	int count = 0, sum = 0, res;
	int max_size = 5;
	int* ans = malloc(max_size * sizeof(int));
	for(a = 1; a < 10; a++)
		for(b = 1111; b < 9877; b++)
			if((res = isPandigital(a,b,a*b))){
				if(!found(ans, count, res)){
					if(count == max_size){
						resize(ans, &max_size);
						printf("max_size: %d\n", max_size);
					}
					ans[count] = res;
					printf("#%d: %d\n", count++ + 1, res);
					sum += res;
				}
			}
	for(a = 11; a < 99; a++)
		for(b = 111; b < 988; b++)
			if((res = isPandigital(a,b,a*b))){
				if(!found(ans, count, res)){
					if(count == max_size){
						resize(ans, &max_size);
						printf("max_size: %d\n", max_size);
					}
					ans[count] = res;
					printf("#%d: %d\n", count++ + 1, res);
					sum += res;
				}
			}
	printf("Total %d pandigital numbers found\n", count);
	printf("Sum: %d\n", sum);
	free(ans);
	return 0;
}
