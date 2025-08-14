#include <stdio.h>


int add (int a, int b) {
	return a + b;
}
	
int main() {
	// Declare a function pointer that matches
	// the signature of add() fuction

	int (*fptr) (int, int);
	// Assign to add()
	fptr = &add;
	// Call the function via ptr
	printf ("%d", fptr(10, 5));
	return 0;
}
