#ifndef DYNAMIC_ARRAY_H
#define DYNAMIC_ARRAY_H

typedef struct {
    int *data;
    int size;
    int capacity;
} DynamicArray;

void initArray(DynamicArray *arr);
void append(DynamicArray *arr, int value);
void printArray(DynamicArray *arr);
void freeArray(DynamicArray *arr);

#endif
