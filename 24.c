/*
 * Project Euler Problem #24
 *
 * A permutation is an ordered arrangement of objects. 
 * For example, 3124 is a permutation made from 1,2,3,4.
 *
 * If all of the permutations are listed numerically or alphabetically,
 * we call it lexicographic order.
 *
 * 0,1,2 =>
 * 012    021    102    120    201    210
 * 
 * 0,1,2,3 =>
 * 0123  0132  0213  0231  0312 / 0321  1023  1032  1203  1230 / 1302  1320  2013  2031  2103 / 2130  2301  2310  3012  3021 / 3102  3120  3201  3210
 * What is the millionth lexicographic permutation of the digits 0~9?
 */
#include <stdio.h>
#include <stdlib.h>
// CHANGE THIS DEPENDING ON TEST VALUE.
int MAX = 1000000;

/*
 * Approach
 *
 * set 0th digit.
 * 	- get first number that is not used so far
 * 	- set the number
 * 	- calculate possible permutation
 * 	- check if it goes over 1000000
 * 		- yes -> return back raise value
 * 		- no -> proceed
 */
int getFactorial(int n) {
    //printf("calculate %d!=", n);
    int res = 1;
    for(int i = n; i >= 2; --i)
        res *= i;
    //printf("%d\n", res);
    return res;
}
/*
 * isUsed(int* arr, int size, int n)
 *
 * :param arr: array containing current values
 * :param size: size of arr
 * :param n: value to search for in the array
 */
int isUsed(int * arr, int size, int n) {
    for(int i = 0; i < size; i++)
	if(arr[i] == n)
	    return 1;
    return 0;
}

/*
 * getPermutation(int *arr, int size, int index)
 * 
 * :param arr: array containing current status
 * :param size: size of arr
 * :param index: index to fill with value
 */
int getPermutation(int * arr, int size, int index, int pos) {
    //printf("[getPermutation] searching for %dth val with array", index);
    //for(int i = 0; i < size; i++)
    //	printf("%d", arr[i]);
    //puts("\n");
    if(index == size - 1){
	for(int i = 0; i < size; i++){
	    if(!isUsed(arr, size, i)){
	        arr[index] = i;
	        break;
	    }
	}
	return pos+1;	    
    } 
    for(int i = 0; i < size; i++){
        if(!isUsed(arr, size, i)){
	    int n, fac;
	    n = i;
	    //printf("try %d\n", n);
	    fac = getFactorial(size-index-1);
	    //printf("fac: %d\n", fac);
	    //printf("perm: %d\n", pos+fac);
	    if(pos + fac < MAX) {
		pos += fac;
	        //printf("try next value \n");
	    }else{
	        //printf("went past max. \n");
		arr[index] = i;
		//printf("try next index.\n");
	        break;
	    }
	}
    }
    return getPermutation(arr, size, index+1, pos);
}
    
int main() {
    int arr[10];
    int size = 10;
    // initialize array
    for(int i = 0; i < size; i++)
	arr[i] = -1;
    int perm = getPermutation(arr, size, 0, 0);
    if(perm != MAX){
        printf("[main] getPermutation() return value does not match MAX.\n");
	exit(0);
    }
    printf("%dth permutation = ", MAX);
    for(int i = 0; i < size; i++)
        printf("%d", arr[i]);
    puts("\n");
    return 0;
}
