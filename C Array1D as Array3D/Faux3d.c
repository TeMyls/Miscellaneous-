#include <stdio.h>
#include <stdlib.h>
//#include <string.h>
#define IDX(x,y,z,cols,rows) ((z)*(rows)*(cols) + (y)*(cols) + (x))


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
	Array_3d A3D = {rows, cols, depth, data};
	return A3D;
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

void add_rows3D(Array_3d *A3D, int add) {
    if (add <= 0) return;

    int new_rows = A3D->rows + add;
    int old_layer = A3D->rows * A3D->cols;
    int new_layer = new_rows * A3D->cols;

    int *new_data = malloc(new_layer * A3D->depth * sizeof(int));

    for (int z = 0; z < A3D->depth; z++) {
        for (int y = 0; y < new_rows; y++) {
            for (int x = 0; x < A3D->cols; x++) {
                if (y < A3D->rows)
                    new_data[IDX(x,y,z,A3D->cols,new_rows)] =
                        A3D->data[IDX(x,y,z,A3D->cols,A3D->rows)];
                else
                    new_data[IDX(x,y,z,A3D->cols,new_rows)] = 0;
            }
        }
    }

    free(A3D->data);
    A3D->data = new_data;
    A3D->rows = new_rows;
}


void remove_rows3D(Array_3d *A3D, int remove) {
    if (remove <= 0 || remove >= A3D->rows) return;

    int new_rows = A3D->rows - remove;
    int *new_data = malloc(new_rows * A3D->cols * A3D->depth * sizeof(int));

    for (int z = 0; z < A3D->depth; z++)
        for (int y = 0; y < new_rows; y++)
            for (int x = 0; x < A3D->cols; x++)
                new_data[IDX(x,y,z,A3D->cols,new_rows)] =
                    A3D->data[IDX(x,y,z,A3D->cols,A3D->rows)];

    free(A3D->data);
    A3D->data = new_data;
    A3D->rows = new_rows;
}

void add_cols3D(Array_3d *A3D, int add) {
    if (add <= 0) return;

    int new_cols = A3D->cols + add;
    int *new_data = malloc(A3D->rows * new_cols * A3D->depth * sizeof(int));

    for (int z = 0; z < A3D->depth; z++)
        for (int y = 0; y < A3D->rows; y++)
            for (int x = 0; x < new_cols; x++)
                new_data[IDX(x,y,z,new_cols,A3D->rows)] =
                    (x < A3D->cols)
                        ? A3D->data[IDX(x,y,z,A3D->cols,A3D->rows)]
                        : 0;

    free(A3D->data);
    A3D->data = new_data;
    A3D->cols = new_cols;
}

void remove_cols3D(Array_3d *A3D, int remove) {
    if (remove <= 0 || remove >= A3D->cols) return;

    int new_cols = A3D->cols - remove;
    int *new_data = malloc(A3D->rows * new_cols * A3D->depth * sizeof(int));

    for (int z = 0; z < A3D->depth; z++)
        for (int y = 0; y < A3D->rows; y++)
            for (int x = 0; x < new_cols; x++)
                new_data[IDX(x,y,z,new_cols,A3D->rows)] =
                    A3D->data[IDX(x,y,z,A3D->cols,A3D->rows)];

    free(A3D->data);
    A3D->data = new_data;
    A3D->cols = new_cols;
}

void add_layers3D(Array_3d *A3D, int add) {
    if (add <= 0) return;

    int old_size = A3D->rows * A3D->cols * A3D->depth;
    int new_depth = A3D->depth + add;
    int new_size = A3D->rows * A3D->cols * new_depth;

    A3D->data = realloc(A3D->data, new_size * sizeof(int));

    for (int i = old_size; i < new_size; i++)
        A3D->data[i] = 0;

    A3D->depth = new_depth;
}

void remove_layers3D(Array_3d *A3D, int remove) {
    if (remove <= 0 || remove >= A3D->depth) return;

    A3D->depth -= remove;
    A3D->data = realloc(
        A3D->data,
        A3D->rows * A3D->cols * A3D->depth * sizeof(int)
    );
}

 
int main(){
	
	Array_3d A3D = init3DA(6, 8, 2);
	printf("Initialed \'3D Array\'\n");
	print3DA(A3D.rows, A3D.cols, A3D.depth, A3D.data);
	
	printf("\nEditing \'3D Array\' as 1D Array\n");
	set_value1D(A3D.data, A3D.cols * A3D.rows * A3D.depth, 2, -1);
	print3DA(A3D.rows, A3D.cols, A3D.depth, A3D.data);

	printf("\nEditing \'3D Array\' as 3D Array\n");
	set_value3D(A3D.data, A3D.cols, A3D.rows, A3D.depth,  1, 2, 1, -4);
	print3DA(A3D.rows, A3D.cols, A3D.depth, A3D.data);
	


	printf("\nCurrent \'3D Array\'\n");
	print3DA(A3D.rows, A3D.cols, A3D.depth, A3D.data);
	


	printf("\nAdding two rows to \'3D Array\'\n");
	add_rows3D(&A3D, 2);
	print3DA(A3D.rows, A3D.cols, A3D.depth, A3D.data);

	printf("\nAdding three columns to \'3D Array\'\n");
	add_cols3D(&A3D, 3);
	print3DA(A3D.rows, A3D.cols, A3D.depth, A3D.data);

	printf("\nAdding one layers to \'3D Array\'\n");
	add_layers3D(&A3D, 1);
	print3DA(A3D.rows, A3D.cols, A3D.depth, A3D.data);



	printf("\nDeleting one row from \'3D Array\'\n");
	remove_rows3D(&A3D, 1);
	print3DA(A3D.rows, A3D.cols, A3D.depth, A3D.data);

	printf("\nDeleted one column from \'3D Array\'\n");
	remove_cols3D(&A3D, 1);
	print3DA(A3D.rows, A3D.cols, A3D.depth, A3D.data);

	printf("\nDeleted one layer from \'3D Array\'\n");
	remove_layers3D(&A3D, 1);
	print3DA(A3D.rows, A3D.cols, A3D.depth, A3D.data);

	free(A3D.data);

	return 0;
}
