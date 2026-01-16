#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>


typedef struct 
  {
  	int rows;
  	int cols;
  	int *data;
 } Array_2d;


Array_2d init2DA( int rows, int cols , int filler){
	int *data = (int *)malloc(rows * cols * sizeof(int));
	for(int i = 0; i < rows * cols; i++){
		data[i] = filler;
	}
	Array_2d A = {rows, cols, data};
	return A;
}

int in_bounds(int x, int y, int w, int h){
	return 0 <= x && 
	x < w &&
	0 <= y && 
	y < h;
} 

int get_value2D(int *arr, int col_len, int row_len, int col, int row) {
	//https://stackoverflow.com/questions/17416543/access-a-1d-array-as-a-2d-array-in-c
	if (in_bounds(col, row, col_len, row_len)){
		return arr[row * col_len + col];
	}else
	{
		return arr[
		abs(row % row_len) * col_len + abs(col % col_len)
		];
	}
    
}

void set_value2D(int *arr, int col_len, int row_len, int col, int row, int value) {
    if (in_bounds(col, row, col_len, row_len)){
		arr[row * col_len + col] = value;
	}else
	{
		arr[
		abs(row % row_len) * col_len + abs(col % col_len)
		] = value;
	}
}

int get_value1D(int *arr, int arr_len, int idx) {
	//allows negative indexes and indexes larger than the array length
    return arr[ abs( idx % arr_len ) ];
}

void set_value1D(int *arr, int arr_len, int idx, int value) {
    arr[ abs( idx % arr_len )] = value; 
}

void print1DA( int arr_len, int *arr){
	for(int i = 0;i < arr_len; i++)
	{
		
		printf("%d ", get_value1D(arr, arr_len, i));
		
		
	}
}

void print2DA( int rows, int cols, int *arr){
	for(int y = 0;y < rows; y++)
	{
		for(int x = 0;x < cols; x++)
		{
			printf("%d ", get_value2D(arr, cols, rows, x, y));
		}
		printf("\n");
	}
}





int max(int a, int b) {
	// Ternary operator for concise comparison
	return (a > b) ? a : b; 
}



int *arrayAppend(int *arr, int *arr_len, int value) {
    int *temp = realloc(arr, (*arr_len + 1) * sizeof(int));
    if (temp == NULL) {
        fprintf(stderr, "Error: realloc failed\n");
        return arr;  // keep original
    }

    temp[*arr_len] = value;
    (*arr_len)++;         // update length
    return temp;          // return new pointer
}



int arrayPop(int **arr, int *arr_len, int idx)
{
    if (*arr_len == 0) {
        fprintf(stderr, "Error: array is empty.\n");
        return 0;
    }

    // wrap index safely
    if (idx < 0 || idx >= *arr_len) {
        idx = abs(idx % *arr_len);
    }

    int val = (*arr)[idx];

    // shift elements left
    for (int i = idx; i < *arr_len - 1; i++) {
        (*arr)[i] = (*arr)[i + 1];
    }

    // shrink the array
    int *tmp = realloc(*arr, (*arr_len - 1) * sizeof(int));
    if (tmp == NULL && *arr_len > 1) {
        // realloc failed but original pointer still valid
        fprintf(stderr, "Error: realloc failed.\n");
        return val;
    }

    *arr = tmp;           // update caller pointer
    (*arr_len)--;         // update size

    return val;
}


void floodFill(Array_2d *arr, int *start_coords, int filler) {
    int total_cells = arr->rows * arr->cols;

    int *visited = malloc(total_cells * 2 * sizeof(int));
    int v_len = 0;

    int *queue = malloc(total_cells * 2 * sizeof(int));
    int queue_len = 0;

    // push starting coordinate
    queue = arrayAppend(queue, &queue_len, start_coords[0]);
    queue = arrayAppend(queue, &queue_len, start_coords[1]);

    while (queue_len > 0) {
        // Pop last pair
        // Poping from 0 makes it a queue
        // From queue_len - 1 makes it a stack
        int cur_x = arrayPop(&queue, &queue_len, 0);
        int cur_y = arrayPop(&queue, &queue_len, 0);
        

        if (!in_bounds(cur_x, cur_y, arr->cols, arr->rows))
        {
            continue;
        }
        // Skip if already filled or visited
        if (get_value2D(arr->data, arr->cols, arr->rows, cur_x, cur_y) == filler)
        {
            continue;
        }
        // Check if in visited
        int in_visited = 0;
        for (int i = 0; i < v_len; i += 2) {
            if (visited[i] == cur_x && visited[i + 1] == cur_y) {
                in_visited = 1;
                break;
            }
        }
        if (in_visited) continue;

        print2DA(arr->rows, arr->cols, arr->data);
        printf("Cur X: %d Cur Y:%d \n", cur_x, cur_y);
        
        // Mark as visited
        visited = arrayAppend(visited, &v_len, cur_x);
        visited = arrayAppend(visited, &v_len, cur_y);

        // Fill cell
        set_value2D(arr->data, arr->cols, arr->rows, cur_x, cur_y, filler);

        // Add neighbors
        queue = arrayAppend(queue, &queue_len, cur_x + 1);
        queue = arrayAppend(queue, &queue_len, cur_y);
        
        queue = arrayAppend(queue, &queue_len, cur_x);
        queue = arrayAppend(queue, &queue_len, cur_y - 1);
        
        queue = arrayAppend(queue, &queue_len, cur_x - 1);
        queue = arrayAppend(queue, &queue_len, cur_y);


        

        
        queue = arrayAppend(queue, &queue_len, cur_x);
        queue = arrayAppend(queue, &queue_len, cur_y + 1);
    }

    free(queue);
    free(visited);
}
 
int main(){
	
	
	
	
	printf("\n");
	Array_2d A2D = init2DA(7, 9, 0);
	//print1DA(A2D.rows * A2D.cols, A2D.data);
	print2DA(A2D.rows, A2D.cols, A2D.data);
	printf("\n");
	srand(time(NULL));   // Initialization, should only be called once.
	int r1 = rand();      // Returns a pseudo-random integer between 0 and RAND_MAX.
	int r2 = rand();      // Returns a pseudo-random integer between 0 and RAND_MAX.
	int rx = (int) r1 % A2D.cols;
	int ry = (int) r2 % A2D.rows;
	
	printf("rx %d ry %d\n", rx, ry);
	int start[2] = {rx, ry};
	//set_value2D(A2D.data, A2D.cols, A2D.rows, rx, ry, 7);
	
	//set_value2D(A2D.data, A2D.cols, A2D.rows, rx + 1, ry, 1);
	//set_value2D(A2D.data, A2D.cols, A2D.rows, rx - 1, ry, 2);
	//set_value2D(A2D.data, A2D.cols, A2D.rows, rx, ry + 1, 3);
	//set_value2D(A2D.data, A2D.cols, A2D.rows, rx, ry - 1, 4);
	
	floodFill(&A2D, start , 5);
	print2DA(A2D.rows, A2D.cols, A2D.data);
	
	
	
	return 0;
}