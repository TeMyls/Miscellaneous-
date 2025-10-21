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


 
int main(){
	
	Array_2d A2D = init2DA(8, 11);
	print1DA(A2D.rows * A2D.cols, A2D.data);
	print2DA(A2D.rows, A2D.cols, A2D.data);
	
	printf("\n");
	
	set_value1D(A2D.data, A2D.cols * A2D.rows, 4, -8);
	
	set_value2D(A2D.data, A2D.cols, A2D.rows, 5, 2, -7);
	
	print1DA(A2D.rows * A2D.cols, A2D.data);
	print2DA(A2D.rows, A2D.cols, A2D.data);
	
	
	free(A2D.data);
	A2D.data = NULL;
	return 0;
}
