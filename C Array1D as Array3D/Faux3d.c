#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct 
  {
  	int rows;
  	int cols;
    int depth;
  	int *data;
 } Array_3d;


Array_3d init3DA( int rows, int cols, int depth ){
	int *data = (int *)malloc(rows * cols * depth * sizeof(int));
	for(int i = 0; i < rows * cols * depth; i++){
		data[i] = i;
	}
	Array_3d A = {rows, cols, depth, data};
	return A;
}

int in_bounds(int x, int y, int z, int w, int h, int l){
	return 0 <= x && 
	x < w &&
	0 <= y && 
	y < h &&
    0 <= z &&
    z < l;
} 

int get_value3D(int *arr, int col_len, int row_len, int depth_len, int col, int row, int depth) {
	//https://stackoverflow.com/questions/17416543/access-a-1d-array-as-a-2d-array-in-c
	//if (in_bounds(col, row, col_len, row_len))
    if (in_bounds(col, row, depth, col_len, row_len, depth_len))
    {
		return arr[depth * (row_len * col_len) + row * col_len + col];
	}else
	{
        int d = abs(depth % depth_len);
        int r = abs(row % row_len);
        int c = abs(col % col_len);
		return arr[
            d * (row_len * col_len) + r * col_len + c
		];
	}
    
}

void set_value3D(int *arr, int col_len, int row_len, int depth_len, int col, int row, int depth, int value) {
    if (in_bounds(col, row, depth, col_len, row_len, depth_len))
    {
		arr[depth * (row_len * col_len) + row * col_len + col] = value;
	}else
	{
        int d = abs(depth % depth_len);
        int r = abs(row % row_len);
        int c = abs(col % col_len);
		arr[
		d * (row_len * col_len) + r * col_len + c
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



void print3DA( int row_len, int col_len, int depth_len, int *arr){
    for (int z = 0; z < depth_len; z++)
    {
        printf("Layer %d\n", z);
        for(int y = 0; y < row_len; y++)
        {
            for(int x = 0; x < col_len; x++)
            {
                printf("%d ", get_value3D(arr, col_len, row_len, depth_len, x, y, z));
            }
            printf("\n");
        }
        printf("\n");
    }
}


 
int main(){
	
	Array_3d A3D = init3DA(3, 4, 5);
	print3DA(A3D.rows, A3D.cols, A3D.depth, A3D.data);
	
	printf("\n");
	
	set_value1D(A3D.data, A3D.cols * A3D.rows * A3D.depth, 2, -1);
	set_value3D(A3D.data, A3D.cols, A3D.rows, A3D.depth,  1, 2, 1, -4);
	
	print3DA(A3D.rows, A3D.cols, A3D.depth, A3D.data);
	
	free(A3D.data);
	A3D.data = NULL;
	return 0;
}
