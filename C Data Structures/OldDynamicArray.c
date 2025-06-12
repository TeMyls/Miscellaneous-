#include <stdio.h>
#include <stdlib.h>

typedef struct 
{
    int *data; //pointer to the array of integers
    int length; // Number of Elements
    int capacity; //Maximum Capacity before resize
} List;

void initList(List *ls, int capacity){
    ls->data = calloc(capacity, sizeof(int));
    ls->length = 0;
    ls->capacity = capacity;
}

void resizeList(List *arr){
    arr->capacity += 1;
    arr->data = realloc(arr->data, arr->capacity*sizeof(int));
}

void appendList(List *ls, int item){
    if (ls->capacity == ls->length){
        resizeList(ls);
    }
    ls->data[ls->length++] = item;
}

int getListIndex(List *ls, int index){
    if (index < 0 || index >= ls->length){
        fprintf(stderr, "Index out of bounds\n");
        exit(EXIT_FAILURE);

    }
    return ls->data[index];
}

void freeList(List *ls){
    free(ls->data);
    ls->data = NULL;
    ls->length = 0;
    ls->capacity;
}

int main(){
    List ls;
    initList(&ls, 5);

    for (int i = 0; i < 10; i++){
        appendList(&ls, i * 2);
    }

    for (int i = 0; i < ls.length; i++){
        printf("Index %d: Element: %d\n", i, getListIndex(&ls, i));
    }

    freeList(&ls);
    return 0;
}