#include <stdio.h>
#include <stdlib.h>

/*
 * 1) Need binary and base
 * 	-> convert base to binary
 * 2) go through numbers and check if palindrome
 * 	-> check for palindrome
 */

void toBinary(char* bin, int* len, int n){
	if(n == 0 || n == 1){
		bin[*len] = n == 0 ? '0' : '1';
		*len += 1;
		return;
	}
	bin[*len] = n % 2 == 0 ? '0' : '1';
	*len += 1;
	toBinary(bin, len, n / 2);
	return;
}

void toStr(char* dec, int* len, int n){
	const char* digits = "0123456789";
	int tmp = n;
	while(tmp > 0){
		dec[*len] = digits[tmp % 10];
		*len += 1;
		tmp /= 10;
	}
	return;
}

char isPalindrome(char * s, int len){
	int mid = len / 2; // if len is odd then -1 +1 else -1 regular
	int start = 0, end = len-1;
	//printf("len: %d, mid: %d\n", len, mid);
	while(start <= end){
		//printf("start: %d, %c, end: %d, %c\n", start, s[start], end, s[end]); 
		if(s[start] != s[end])
			return 0;
		start += 1;
		end -= 1;
	}
	return 1;
}

int main(){
	char bin[21] = {0}; // since 1,000,000 has 20 digits at max
	char dec[8] = {0};
	bin[20] = '\0';
	dec[7] = '\0';
	int sum = 0;
	int b_len, d_len;
	for(int i = 1; i <= 1000000; i++){
		b_len = 0, d_len = 0;
		toBinary(bin, &b_len, i);
		toStr(dec, &d_len, i);
		//printf("%d => b %s: %d, d %s: %d\n", i, bin, b_len, dec, d_len);
		if(isPalindrome(dec, d_len) & isPalindrome(bin, b_len)){
			printf("%d, %s\n", i,isPalindrome(dec, d_len) == 1 ? "True" : "False");
			sum += i;
		}
		//printf("%d: %s, len: %d\n", i, bin, len);
		//printf("%d: %s\n", i, isPalindrome(atoi(i), len) ? "True" : "False");
	}	
	printf("Sum: %d\n", sum);
	return 0;
}
