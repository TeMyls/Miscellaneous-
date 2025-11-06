#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


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
    if (in_bounds(col, row, col_len, row_len))
    {
        arr[row * col_len + col] = value;
    }
    else
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

void _arrayAppend(int *arr, int arr_len, int value){
    int *temp = (int *)realloc(arr, (arr_len + 1) * sizeof(int));
    temp[arr_len] = value;
    arr = temp;
}

int *arrayAppend(int *arr, int *arr_len, int value) {
    int *temp = realloc(arr, (*arr_len + 1) * sizeof(int));
    if (temp == NULL) 
    {
        fprintf(stderr, "Error: realloc failed\n");
        return arr; // keep original
    }

    temp[*arr_len] = value;
    (*arr_len)++; // update length
    return temp; // return new pointer
}

int _arrayPop(int *arr, int arr_len, int idx){
    //int al = round(sizeof(arr)/sizeof(arr[0]));
    //printf(" Int %d", al);
    if (idx == 0)
    {
        idx = abs( idx % arr_len );
        int val = arr[ idx ];
        int i = idx + 1;
        int *temp = (int *)realloc(arr, (arr_len - 1) * sizeof(int));

        while(i < arr_len)
        {
            temp[i - 1] = arr[i];
            i++;
        }

        arr = temp;
        return val;
    }
    else if(idx == arr_len - 1)
    {
        idx = abs( idx % arr_len );
        int val = arr[ idx ];
        int i = idx - 1;
        int *temp = (int *)realloc(arr, (arr_len - 1) * sizeof(int));
        while(i > -1)
        {
            temp[i] = arr[i];
            i--;
        }
        arr = temp;
        return val;
    }else
    {

    int *temp = (int *)realloc(arr, (arr_len - 1) * sizeof(int));
    int val = arr[ idx ];
    int left = idx - 1;
    int right = idx + 1;
    int i = arr_len - 1;
    //int mx = max(left, right);

    while (i >= 0) 
    {
        if (left >= 0){
            temp[left] = arr[left];
            left--;
        }
        if (right < arr_len){
            temp[right - 1] = arr[right];
            right++;
        }

    i--;
    }


    arr = temp;
    return val;
    }

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
    if (tmp == NULL && *arr_len > 1) 
    {
        // realloc failed but original pointer still valid
        fprintf(stderr, "Error: realloc failed.\n");
        return val;
    }

    *arr = tmp; // update caller pointer
    (*arr_len)--; // update size

    return val;
}

/*
void _floodFill(Array_2d *arr, int *start_coords, int filler){
    //holds x-y values
    printf("SX: %d SY: %d\n", start_coords[0], start_coords[1]);
    int tally = 0;
    int total_cells = arr->rows * arr->cols;
    int* visited = (int *)malloc(total_cells * 2 * sizeof(int));
    int* queue = (int *)malloc(total_cells * 2 * sizeof(int));
    //queue[0], queue[1] = start_coords[0], start_coords[1];
    queue[0] = start_coords[0];
    queue[1] = start_coords[1];

    //visited[0] = start_coords[0];
    //visited[1] = start_coords[1];
    set_value2D(arr, arr->cols, arr->rows, start_coords[0], start_coords[1], filler);


    //int idx2d = start_coords[1] * arr->cols + start_coords[0];
    //arr->data[idx2d] = filler;
    int queue_len = 2;
    int v_len = 0;
    //printf("2\n");
    while (queue_len > 0)
    {
        print1DA(queue_len, queue);
        int cur_y = arrayPop(&queue, &queue_len, 1);
        int cur_x = arrayPop(&queue, &queue_len, 0);
        //printf("4\n");

        //printf("3\n");
        //printf("\nCur X: %d Cur Y: %d\n", cur_x, cur_y);
        if (in_bounds(cur_x, cur_y, arr->cols, arr->rows)){
        //printf("agsgs\n");
        // skip the coordinate if it's inside visited

        int i = 0;
        int in_visited = 0;
    while(i < total_cells)
    {
        int vx = visited[i];
        int vy = visited[i + 1];
        if(cur_x == vx && cur_y == vy)
        {

        in_visited = 1;
        break;
        }
        i = i + 2;
        }
        if(in_visited)
        {
        printf("eagsd\n");
        //queue_len = queue_len - 2;
        continue;
        }else
        {
        arrayAppend(visited, &v_len, cur_x);
        arrayAppend(visited, &v_len, cur_y);
        }

        set_value2D(arr, arr->cols, arr->rows, cur_x, cur_y, filler);
        //int idx2d = cur_y * arr->cols + cur_x;
        //arr->data[idx2d] = filler;


    }
    printf("eagsd1\n");
    queue = arrayAppend(queue, &queue_len, cur_x + 1);
    queue = arrayAppend(queue, &queue_len, cur_y);
    //queue_len = queue_len + 2;

    printf("eagsd2\n");
    queue = arrayAppend(queue, &queue_len, cur_x - 1);
    queue = arrayAppend(queue, &queue_len, cur_y);
    //queue_len = queue_len + 2;

    printf("eagsd3\n");
    queue = arrayAppend(queue, &queue_len, cur_x);
    queue = arrayAppend(queue, &queue_len, cur_y + 1);
    //queue_len = queue_len + 2;

    printf("eagsd4\n");
    queue = arrayAppend(queue, &queue_len, cur_x);
    queue = arrayAppend(queue, &queue_len, cur_y - 1);
    //queue_len = queue_len + 2;
    //queue_len = queue_len - 2;

    tally++;
    if(tally == 4)
    {
    break;
    }
    }




}
    */

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
        int cur_y = arrayPop(&queue, &queue_len, queue_len - 1);
        int cur_x = arrayPop(&queue, &queue_len, queue_len - 1);

        if (!in_bounds(cur_x, cur_y, arr->cols, arr->rows))
            continue;

        // Skip if already filled or visited
        if (get_value2D(arr->data, arr->cols, arr->rows, cur_x, cur_y) == filler)
            continue;

        // Check if in visited
        int in_visited = 0;
        for (int i = 0; i < v_len; i += 2) {
            if (visited[i] == cur_x && visited[i + 1] == cur_y) {
                in_visited = 1;
                break;
            }
        }
        if (in_visited) continue;

        // Mark as visited
        visited = arrayAppend(visited, &v_len, cur_x);
        visited = arrayAppend(visited, &v_len, cur_y);

        // Fill cell
        set_value2D(arr->data, arr->cols, arr->rows, cur_x, cur_y, filler);

        // Add neighbors
        queue = arrayAppend(queue, &queue_len, cur_x + 1);
        queue = arrayAppend(queue, &queue_len, cur_y);

        queue = arrayAppend(queue, &queue_len, cur_x - 1);
        queue = arrayAppend(queue, &queue_len, cur_y);

        queue = arrayAppend(queue, &queue_len, cur_x);
        queue = arrayAppend(queue, &queue_len, cur_y + 1);

        queue = arrayAppend(queue, &queue_len, cur_x);
        queue = arrayAppend(queue, &queue_len, cur_y - 1);
    }

    free(queue);
    free(visited);
}



int main(){
/*
int *arr = (int *)malloc(10 * sizeof(int));
for(int i = 0; i < 10; i++){
arr[i] = i;
}
print1DA(10, arr);


_arrayPop(arr, 10, 9);
printf("\n");
print1DA(9, arr);
arrayAppend(arr, 9, -11);
printf("\n");
print1DA(10, arr);
free(arr);
*/

/*

int len = 5;
int *arr = malloc(len * sizeof(int));

for (int i = 0; i < len; i++)
arr[i] = i + 1; // 1 2 3 4 5

int popped = arrayPop(&arr, &len, 2); // remove element at index 2

printf("Popped: %d\n", popped);
for (int i = 0; i < len; i++)
printf("%d ", arr[i]);
printf("\n");

free(arr);
*/



printf("\n");
Array_2d A2D = init2DA(8, 11, 0);
//print1DA(A2D.rows * A2D.cols, A2D.data);
print2DA(A2D.rows, A2D.cols, A2D.data);
printf("\n");
int start[2] = {3, 4};
floodFill(&A2D, start , 5);
print2DA(A2D.rows, A2D.cols, A2D.data);


/*
Array_2d A2D = init2DA(8, 11, -1);
print1D(A2D.rows, A2D.cols, A2D.data);
print2DA(A2D.rows, A2D.cols, A2D.data);

printf("\n");

set_value1D(A2D.data, A2D.cols * A2D.rows, 4, 8);

set_value2D(A2D.data, A2D.cols, A2D.rows, 5, 2, 7);

print2DA(A2D.rows, A2D.cols, A2D.data);
print2DA(A2D.rows, A2D.cols, A2D.data);


free(A2D.data);
A2D.data = NULL;
*/



return 0;
}