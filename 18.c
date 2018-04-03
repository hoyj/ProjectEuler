/*
 * Project Euler Problem #18
 *
 * In the given triangle of numbers, find the path where the sum of the path's 
 * numbers is max
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int HEIGHT = 15;

const int SIZE = HEIGHT * (HEIGHT + 1) / 2;

char triangle[] = "\
75 \
95 64 \
17 47 82 \
18 35 87 10 \
20 04 82 47 65 \
19 01 23 75 03 34 \
88 02 77 73 07 63 67 \
99 65 04 28 06 16 70 92 \
41 41 26 56 83 40 80 70 33 \
41 48 72 33 47 32 37 16 94 29 \
53 71 44 65 25 43 91 52 97 51 14 \
70 11 33 28 77 73 17 78 39 68 17 57 \
91 71 52 38 17 14 91 43 58 50 27 29 48 \
63 66 04 68 89 53 67 30 73 16 69 87 40 31 \
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23";

// test data
/*
const int HEIGHT = 4;
const int SIZE = HEIGHT * (HEIGHT + 1) / 2;
char triangle [] = "\
3 \
7 4 \
2 4 6 \
8 5 9 3";
*/
struct node {
  int val;
  int sum;
};

struct node nodes[SIZE];

void char_to_int_array(char *triangle_array, int num_array[], int size)
{
  char *token = NULL;
  char *next_ptr;
  int index = 0;

  for (token = strtok_r(triangle_array, " ", &next_ptr);
       token != NULL;
       token = strtok_r(NULL, " ", &next_ptr))
  {
    num_array[index++] = atoi(token);
  }
}

/*
 * given a node, print the values in node
 */
void print_node(int offset, struct node *n)
{
  printf("node %d: val=%d, sum=%d\n",offset, n->val,n->sum);
}

/*
 * given the max _ height, and num array
 * parse through elements to fill in the missing values in struct node in nodes
 */
void fill_node_info(int max_height, int* num_array)
{
  for (int h = 0; h < max_height; h++)
  {
	// check if node is already filled. Assume node was filled IF sum field is filled.
	for(int i = 0; i < h + 1; i++)
	{
		if(h == 0 && i == 0)
		{
			struct node *cur = &nodes[0];
			printf("num_array: %d\n", num_array[0]);
			printf("%x\n", cur);
			cur->val = num_array[0];
  			cur->sum = num_array[0];
			print_node(0, cur);
		}else{
			
			int offset = h * (h+1) / 2 + i;
			struct node *n = &nodes[offset];
			n->val = num_array[offset];

			int prev_offset = (h-1) * h / 2 + i;
			if (i== 0)
				n->sum = nodes[prev_offset].sum;
			else if (i == h)
				n->sum = nodes[prev_offset-1].sum;
			else
				n->sum = (nodes[prev_offset].sum > nodes[prev_offset-1].sum) ? nodes[prev_offset].sum : nodes[prev_offset-1].sum;
			n->sum = n->sum + n->val;
		}
	}
  }
}

int main()
{
  // printf("triangle as string = %s\n", triangle);
  int num_array[SIZE];
  char_to_int_array(triangle, num_array, SIZE);
  // str -> int array comlete. Proceed with int array -> struct array

  fill_node_info(HEIGHT, num_array);
  int max = -1;
  for (int i = 0; i <  SIZE; i++)
  {
	print_node(i, &nodes[i]);
	if (max < nodes[i].sum)
		max = nodes[i].sum;
  }
  printf("max: %d\n", max);

  return 0;
}
