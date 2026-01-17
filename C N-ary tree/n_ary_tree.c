#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct 
  {
  	int rows;
  	int cols;
  	int *data;
 } Array_2d;


Array_2d init2DA( int rows, int cols, int filler){
	int *data = (int *)malloc(rows * cols * sizeof(int));
	for(int i = 0; i < rows * cols; i++){
		data[i] = filler;
	}
	Array_2d A2D = {rows, cols, data};
	return A2D;
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

void displayMatrix( int rows, int cols, int *arr){
	for(int y = 0;y < rows; y++)
	{
		printf("Row %d: ", y);
		for(int x = 0;x < cols; x++)
		{
			int val = get_value2D(arr, cols, rows, x, y);
			if (val >= 0)
			{
				printf("%d ", val);
			}
			else
			{
				printf("_ ");
			}
		}
		printf("\n");
	}
}

void add_rows(Array_2d *A2D, int add) {
    if (add <= 0) return;

    int new_rows = A2D->rows + add;
    int new_size = new_rows * A2D->cols;

    A2D->data = realloc(A2D->data, new_size * sizeof(int));

    // initialize new rows
    for (int i = A2D->rows * A2D->cols; i < new_size; i++) {
        A2D->data[i] = 0;
    }

    A2D->rows = new_rows;
}

void remove_rows(Array_2d *A2D, int remove) {
    if (remove <= 0 || remove >= A2D->rows) return;

    A2D->rows -= remove;
    A2D->data = realloc(A2D->data, A2D->rows * A2D->cols * sizeof(int));
}

void add_cols(Array_2d *A2D, int add) {
    if (add <= 0) return;

    int new_cols = A2D->cols + add;
    int *new_data = malloc(A2D->rows * new_cols * sizeof(int));

    for (int y = 0; y < A2D->rows; y++) {
        for (int x = 0; x < new_cols; x++) {
            if (x < A2D->cols)
                new_data[y * new_cols + x] =
                    A2D->data[y * A2D->cols + x];
            else
                new_data[y * new_cols + x] = 0;
        }
    }

    free(A2D->data);
    A2D->data = new_data;
    A2D->cols = new_cols;
}


void remove_cols(Array_2d *A2D, int remove) {
    if (remove <= 0 || remove >= A2D->cols) return;

    int new_cols = A2D->cols - remove;
    int *new_data = malloc(A2D->rows * new_cols * sizeof(int));

    for (int y = 0; y < A2D->rows; y++) {
        for (int x = 0; x < new_cols; x++) {
            new_data[y * new_cols + x] =
                A2D->data[y * A2D->cols + x];
        }
    }

    free(A2D->data);
    A2D->data = new_data;
    A2D->cols = new_cols;
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



void traverse(Array_2d *arr, int idx, int is_bfs) {
	int rows = arr->rows;
	int cols = arr->cols;
    int total_cells = rows * cols;

    int *visited = malloc(total_cells * 2 * sizeof(int));
    int v_len = 0;

    int *deque = malloc(total_cells * 2 * sizeof(int));
    int deque_len = 0;

    idx = abs(idx % cols);
    (is_bfs) ? printf("Breadth First Search\n") : printf("Depth First Search\n");
    printf("Start idx %d\n",idx);
    // push starting coordinate
    deque = arrayAppend(deque, &deque_len, idx);
    visited = arrayAppend(visited, &v_len, idx);
    
    while (deque_len > 0) {
        // Pop last pair
        int item = -1;
        if(is_bfs)
        {
        	// bfs is a queue
        	item = arrayPop(&deque, &deque_len, 0);
        }
        else
        {
        	// dfs is a stack
        	item = arrayPop(&deque, &deque_len, deque_len - 1);
        }
        
        
        for (int i = 0; i < arr->cols; i++)
        {
        	//get_value2D(int *arr, int col_len, int row_len, int col, int row);
        	
        	int vtx = get_value2D(arr->data, cols, rows, i, item);
        	int in_visited = 0;
        	
        	if (vtx > -1)
        	{
        		printf("Parent: %d Child:%d\n", item, vtx);
        		
        		// Check if in visited
        		for (int j = 0; j < v_len; j++) 
        		{
        			if (visited[j] == vtx)
        			{
        				in_visited = 1;
        				
        				
        			}
        			
        		}
        		visited = arrayAppend(visited, &v_len, vtx);
        		deque = arrayAppend(deque, &deque_len, vtx);
        		if (in_visited){
        			arrayPop(&deque, &deque_len, deque_len - 1);
        			arrayPop(&visited, &v_len, v_len - 1);
        		};
        		//printf("\nyep");
        		
        		// Mark as visited
        		
        	}
        	
        
        }
        (is_bfs) ? printf("Queue: ") : printf("Stack: ");
        print2DA(1, deque_len, deque);
        
        printf("visited: ");
        print2DA(1, v_len, visited);

        //print2DA(arr->rows, arr->cols, arr->data);
        
        
        

        // Fill cell
        //set_value2D(arr->data, arr->cols, arr->rows, cur_x, cur_y, filler);

        // Add neighbors
        //queue = arrayAppend(queue, &queue_len, cur_x + 1);
        

        

        
        //queue = arrayAppend(queue, &queue_len, cur_x);
        //queue = arrayAppend(queue, &queue_len, cur_y + 1);
    }

    printf("\nVisited\n");
    print2DA(1, v_len, visited);
    free(deque);
    free(visited);
}

void bfs(Array_2d *arr, int idx){
	traverse(arr, idx, 1);
}

void dfs(Array_2d *arr, int idx){
	traverse(arr, idx, 0);
}

/*
def bfs(tree: dict[any, list[any]], node: any):
	visited = [node]
	queue = [node]
	print(tree)
	
	while queue:
		print(queue)
		item = queue.pop(0)
		if tree.get(item):
			for i in tree[item]:
				if i not in visited:
					queue.append(i)
					visited.append(i)
		
	print(visited)
	
def dfs(tree: dict[any, list[any]], node: any):
	visited = [node]
	stack = [node]
	print(tree)
	
	while stack:
		print(stack)
		item = stack.pop()
		if tree.get(item):
			for i in range(len(tree[item]) - 1,-1,-1):
				if tree[item][i] not in visited:
					stack.append(tree[item][i])
					visited.append(tree[item][i])
					

	print(visited)
*/

int main() {
	/*
	Copying a adjcently list from my Python implementation
	a = {
		 0: [5, 1, 6],
		 1: [0, 4],
		 2: [5, 3, 4],
		 3: [2, 4],
		 4: [2, 3, 1], 
		 5: [0, 2, 6],
		 6: [0, 5]
		 }
	
	the indexes would be each row
	the values would be in each column
		 they would be other indexes the current
		 index is connected to
	together they would form a graph/tree
	where each index has multiple values as childern
	
		 
	the above adjency list would translate to
		 
	Index: Array - ? is a filler integer,-1 
	0 :	 ?, 1, ?, ?, ?, 5, 6
	1 :	 0, ?, ?, ?, 4, ?, ?
	2 :	 ?, ?, ?, 3, 4, 5, ?
	3 :	 ?, ?, 2, ?, 4, ?, ?
	4 :  ?, 1, 2, 3, ?, ?, ?
	5 :	 0, ?, 2, ?, ?, ?, 6
	6 :	 0, ?, ?, ?, ?, 5, ?
	
		 
	*/
	
	Array_2d Matrix = init2DA(7, 7, -1);
	int *d = Matrix.data;
	int r = Matrix.rows;
	int c = Matrix.cols;
		 
	int idx = -1;
	int val = -1;
	//set_value2D(int *arr, int col_len, int row_len, int col, int row, int value)
		 
	// index 0: ?, 1, ?, ?, ?, 5, 6
	idx = 0;
		 
	val = 1;
	set_value2D(d, c, r, val, idx, val);
		 
	val = 5;
	set_value2D(d, c, r, val, idx, val);
		 
	val = 6;
	set_value2D(d, c, r, val, idx, val);
	
	// index 1: 0, ?, ?, ?, 4, ?, ?
	idx = 1;
		 
	val = 0;
	set_value2D(d, c, r, val, idx, val);
		 
	val = 4;
	set_value2D(d, c, r, val, idx, val);
		 
	// index 2: ?, ?, ?, 3, 4, 5, ?
	idx = 2;
		 
	val = 3;
	set_value2D(d, c, r, val, idx, val);
		 
	val = 4;
	set_value2D(d, c, r, val, idx, val);
	
	val = 5;
	set_value2D(d, c, r, val, idx, val);
		 
	// index 3: ?, ?, 2, ?, 4, ?, ?
	idx = 3;
		 
	val = 2;
	set_value2D(d, c, r, val, idx, val);
		 
	val = 4;
	set_value2D(d, c, r, val, idx, val);
	
	// index 4: ?, 1, 2, 3, ?, ?, ?
	idx = 4;
		 
	val = 1;
	set_value2D(d, c, r, val, idx, val);
		 
	val = 2;
	set_value2D(d, c, r, val, idx, val);
	
	val = 3;
	set_value2D(d, c, r, val, idx, val);
		 
	// index 5: 0, ?, 2, ?, ?, ?, 6
	idx = 5;
		 
	val = 0;
	set_value2D(d, c, r, val, idx, val);
		 
	val = 2;
	set_value2D(d, c, r, val, idx, val);
	
	val = 6;
	set_value2D(d, c, r, val, idx, val);
		 
		 
	// index 6: 0, ?, ?, ?, ?, 5, ?
	idx = 6;
		 
	val = 0;
	set_value2D(d, c, r, val, idx, val);
		 
	val = 5;
	set_value2D(d, c, r, val, idx, val);
	
	
	displayMatrix(r, c, d);
	bfs(&Matrix, 1);
	free(Matrix.data);
    return 0;
}

