#include <stdio.h>

int main() {
	
    int a = 10;
    void *ptr_void = &a; // void pointer pointing to an int

    // Attempting to dereference directly will cause a compilation error:
    // printf("%d\n", *ptr_void); // Invalid use of void expression

    // Correct way: Cast and then dereference
    int *ptr_int = (int *)ptr_void;
    printf("Value of a: %d\n", *ptr_int); // Output: Value of a: 10

    // Modifying the value through the casted pointer
    *ptr_int = 20;
    printf("New value of a: %d\n", a); // Output: New value of a: 20
    
    //https://stackoverflow.com/questions/15468441/dereference-void-pointer
    int lVNum = 2;
    void *lVptr;
    lVptr = &lVNum;
    printf("\nlVptr[60 ] is  %d \n",*(int *)lVptr);

    return 0;
}
