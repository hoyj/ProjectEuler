/*
 *  Project Euler Problem #22
 *
 *  A list of names is in 'names.txt'.
 *  For a name, the alphabets each correspond to a score(A=1, B=2, ..., Z=26)
 *  and by adding them all and multiplying by the order of the name 
 *  within the list of names, a name's score can be calculated.
 *
 *  Ex), "COLIN" has alphabets with corresponding numbers 3, 15, 12, 9, and 14
 *  and it is the 938th name in the list.
 *  Thus, the score is 938 x 53 = 49714.
 *
 *  Then what is the sum of the scores in names.txt
 *
 *  1) Order list
 *  2) get each score by rule
 *  3) add rule
 */
#include <stdio.h>
#include <string.h> // strcmp
#include <ctype.h> // toupper
#include <stdlib.h>

char * TEST_ERROR = "[%s] FAIL - %s";

int OFFSET = 16; // this is the offset of 'A' from 'a';
const char * FILE_NAME = "./tmp/names.txt";

unsigned int getNameScore(int order, char * name);
char **readFile(const char* fname, int *name_list_size);
void compare(char**, char**);
void orderList(char ** list, int size);

// tests
void test_compare() {
    char* s1 = "JACOB";
    char* s2 = "MARY";
    compare(&s1, &s2);
    if(strcmp(s1,"JACOB") | strcmp(s2, "MARY")) {
	puts("[test_compare] FAIL");
	exit(0);
    }

    s1 = "MARILYN";
    s2 = "MACY";
    compare(&s1, &s2);
    if(strcmp(s1,"MACY") | strcmp(s2, "MARILYN")) {
	puts("[test_compare] FAIL");
	exit(0);
    }

    s1 = "MACBETH";
    s2 = "MAC";
    compare(&s1, &s2);
    if(strcmp(s1,"MAC") | strcmp(s2, "MACBETH")) {
	puts("[test_compare] FAIL");
	exit(0);
    }
    
    puts("[test_compare] SUCCESS");
    return;
}

void test_orderList() {
    char * l[7] = { "MACBETH", "JACOB", "MACY", "MARILYN", "MARY", "ARON", "MAC" };
    char * answer[7] = { "ARON", "JACOB", "MAC", "MACBETH", "MACY", "MARILYN", "MARY"};
    orderList(l, 7);
    for(int i = 0; i < 7; i++)
    {
        if(strcmp(l[i], answer[i])) {
	    puts("[test_orderList] FAIL");
	    exit(0);
	}
    }
    puts("[test_orderList] SUCCESS");
    return;
}

void test() {
    test_compare();
    test_orderList();
    return;
}

int main(int argc, char**argv)
{
    char ** names;
    char * specific;
    int size = 0;
    int score;
    int total_score = 0;

    names = readFile(FILE_NAME, &size);
    orderList(names, size);

    if(argc > 1){
	specific = argv[1];
	int order = -1;
	printf("Searching for %s...", specific);
	for(int i = 0; i < size; i++) {
	    if(i % 10 == 0)
		printf(".");
	    if(!strcmp(specific, names[i])){
	        order = i;
		printf("found at %d\n", order);
	        break;
	    }
	}
	if(order == -1) {
	    puts("Unable to find name in list.");
	    exit(0);
	}
	score = getNameScore(order+1, specific);
	printf("%-15s\t%d\n", specific, score);
	exit(0);
    }

    for(int i = 0; i < size; i++) {
        score = getNameScore(i+1, names[i]);    
        //printf("%-15s\t%d\n", names[i], score);
	total_score += score;
    }
    printf("total score = %d\n", total_score);
    return 0;
}

unsigned int getNameScore(int order, char * name)
{
    size_t len = strlen(name);
    int sum = 0;
    for(int i = 1; i < len-1; i++)
    {
	sum += toupper(name[i]) - '0' - OFFSET;
	//printf("%c: %d\n", toupper(name[i]), toupper(name[i]) - '0');
    }
    sum *= order;
    return sum;
}

/*
 * char ** readFile(char* fname)
 *
 * :param fname: string of the file to open
 * :param name_list_size: address to put name_list's size
 * return list of strings(char**)
 * 
 * desc: from a file that is delimited by ',' with each name surrounded with ",
 *       1) read in the data
 *       2) split data by delimiter ','
 *       3) add to list
 *       4) return list
 */
char** readFile(const char* fname, int* save_count){
    FILE * fp;
    long size;
    char * buffer;
    size_t size_read;

    fp = fopen("./tmp/names.txt", "r");
    if(fp == NULL)
    {
	puts("File error");
	exit(0);
    }

    fseek(fp, 0, SEEK_END);
    size = ftell(fp);
    rewind(fp);

    buffer = (char*) malloc(sizeof(char) * size);
    if(buffer == NULL) {
	puts("Memory error");
	exit(0);
    }
    size_read = fread(buffer, 1, size, fp);
    if(size_read != size) {
	puts("Reading error");
	exit(0);
    }

    fclose(fp);

    // with buffer
    // 1) get number of names in buffer by counting occurrences of ',' + 1
    int name_count = 0;
    for(int i = 0; i < size; i++) {
        if(buffer[i] == ',')
	    ++name_count;
    }
    name_count += 1;

    // 2) create char** to save the words from tokenizing the buffer.
    char** name_list = (char**)malloc(sizeof(char*) * name_count);
    char * token;
    *save_count = 0;

    token = strtok(buffer, ",");
    while(token != NULL) {
        name_list[*save_count] = token;
	*save_count += 1;
	token = strtok(NULL, ",");
    }
    
    free(buffer);
    if(*save_count != name_count) {
	puts("Saving error");
	exit(0);
    }
    printf("%d\n", *save_count);

    return name_list;
}

/*
 * orderList(char** list)
 *
 * :param list: input is a list of strings int the format "NAME"
 * :param size: list of the size given
 *
 * description: 
 * 	order the list in alphabetical order using bubble sort
 */
void orderList(char** list, int size) {
    int window = size - 1;
    while(window != 0) {
	for(int i = 0; i < window; i++) {
	    compare(&list[i], &list[i+1]);
	}
	window -= 1;
    }
}

/*
 * void compare(char* s1, char* s2)
 *
 * :param s1, s2: address of strings to compare
 * 
 * desc: compare strings @ s1 and s2.
 * 	*s1 > *s2: switch values in memory
 */
void compare(char** s1, char** s2) {
   if(s1 == NULL || s2 == NULL) {
        printf("Compare error. Invalid parameter accepted.");
        exit(0);
    }
    
    char *a = *s1;
    char *b = *s2;
 
    //printf("[compare] before - %s, %s\n", a, b);
    int index = 0;
    char* tmp;
    int res = strcmp(a, b);
    //printf("%s\n", res <= 0 ? "a <= b" : "a > b");
    if(res > 0) {
	tmp = *s1;
	*s1 = *s2;
	*s2 = tmp;
    }
    //printf("[compare] after - %s, %s\n", *s1, *s2);
    return;

}
