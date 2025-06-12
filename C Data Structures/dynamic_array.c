#include "dynamic_array.h"
#include <stdio.h>
#include <stdlib.h>

void initArray(DynamicArray *arr) {
    arr->capacity = 4;
    arr->size = 0;
    arr->data = malloc(arr->capacity * sizeof(int));
}

void append(DynamicArray *arr, int value) {
    if (arr->size == arr->capacity) {
        arr->capacity *= 2;
        arr->data = realloc(arr->data, arr->capacity * sizeof(int));
    }
    arr->data[arr->size++] = value;
}

void printArray(DynamicArray *arr) {
    for (int i = 0; i < arr->size; i++) printf("%d ", arr->data[i]);
    printf("\n");
}

void freeArray(DynamicArray *arr) {
    free(arr->data);
}
