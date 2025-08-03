#include <stdio.h>
#include <stdlib.h>
#include <math.h>


typedef struct{
    char **dynamicArray;
    int height;
    int width;
} Grid;

void fillGrid(Grid *g){ 
    for (int i = 0; i < g->height; i++) {
        for (int j = 0; j < g->width + 1; j++) {
            if (j == g->width){
                g->dynamicArray[i][j] = '\0';
            }else{
                g->dynamicArray[i][j] = 'a';
            }
            
        }
    }
}

char**createMatrix (int rows, int cols){
	char **arr = (char **)malloc(rows * sizeof(
char *));
	// Allocate memory for each row (1D array)
	for (int i = 0; i < rows; i++){
		arr[i] = (char *)malloc((cols + 1) * sizeof(char));
	}
	return arr;
}

Grid initGrid(int rows, int cols, char c){
	
	Grid newGrid = {
		createMatrix(rows, cols), 
		rows, 
		cols
		};
	fillGrid(&newGrid);
	return newGrid;
}

void resizeGrid(Grid *g, int new_rows, int new_cols) {
     // Free extra rows if shrinking
    if (new_rows < g->height){
        for (int i = new_rows; i < g->height; i++) {
            free(g->dynamicArray[i]);
        }
    }

    // Reallocate outer array (array of char* pointers)
    g->dynamicArray = (char **)realloc(g->dynamicArray, new_rows * sizeof(char *));

   

    // Resize or allocate each row
    for (int i = 0; i < new_rows; i++) {
        if (i >= g->height) {
            // New row
            g->dynamicArray[i] = (char *)malloc((new_cols + 1) * sizeof(char));
        } else {
            // Existing row: reallocate
            g->dynamicArray[i] = (char *)realloc(g->dynamicArray[i], (new_cols + 1) * sizeof(char));
        }
    }

    
    
    

    

    g->height = new_rows;
    
    g->width = new_cols;
    fillGrid(g);
}

void freeGrid(Grid *g){
    //freeing each row
    for (int i = 0; i < g->height; i++) {
        free(g->dynamicArray[i]);
    }
    //freeing the entire array
    free(g->dynamicArray);
}

void printGrid(int rows, char** s){
    //Prints one row string at a time
    char** r = s;
    int i = 0;
    while (i < rows)
    {
        printf("%s\n", r[i]);
        i++;
    }
}

int main(){
    Grid testGrid = initGrid(15, 5);

    printGrid(testGrid.height, testGrid.dynamicArray);

    
    printf("Resized\n\n");
    resizeGrid(&testGrid, 5, 20);
    printGrid(testGrid.height, testGrid.dynamicArray);

    
    printf("Resized\n\n");
    resizeGrid(&testGrid, 5, 5);
    printGrid(testGrid.height, testGrid.dynamicArray);

    
    printf("Resized\n\n");
    resizeGrid(&testGrid, 7, 5);
    printGrid(testGrid.height, testGrid.dynamicArray);
    

    printf("Resized\n\n");
    freeGrid(&testGrid);
    printf("Finished");
    return 0;
}