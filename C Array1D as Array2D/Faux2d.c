#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct 
  {
  	int rows;
  	int cols;
  	int *data;
 } Array_2d;


Array_2d init2DA( int rows, int cols ){
	int *data = (int *)malloc(rows * cols * sizeof(int));
	for(int i = 0; i < rows * cols; i++){
		data[i] = i;
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


 
int main(){
	
	Array_2d A2D = init2DA(8, 11);
	print2DA(A2D.rows, A2D.cols, A2D.data);
	
	printf("\n");
	
	set_value1D(A2D.data, A2D.cols * A2D.rows, 4, -1);
	set_value2D(A2D.data, A2D.cols, A2D.rows, 5, 2, -2);
	
	print2DA(A2D.rows, A2D.cols, A2D.data);
	
	
	

	printf("\nAdd 2 rows:\n");
    add_rows(&A2D, 2);
    print2DA(A2D.rows, A2D.cols, A2D.data);

    printf("\nAdd 1 column:\n");
    add_cols(&A2D, 1);
    print2DA(A2D.rows, A2D.cols, A2D.data);

    printf("\nRemove 1 row and 1 column:\n");
    remove_rows(&A2D, 1);
    remove_cols(&A2D, 1);
    print2DA(A2D.rows, A2D.cols, A2D.data);

    free(A2D.data);

	return 0;
}
