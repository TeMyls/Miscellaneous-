#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct 
 {
 	char *letters;
 	int width;
 } Str;

Str initStr(char *s){
	int i = 0;
	while (s[i] != '\0'){i++;}
	Str x = {s, i};
	return x;
}

char *fillerString(char c, int length){

	char *str = (char *)malloc((length + 1)*sizeof(char));
	for (int i = 0; i < length+1; i++){
		if (i == length){
			str[i] = '\0';
		}else{
			str[i] = c;
		}
	}
	return str;
}

char* splice(Str s, int begin, int end){
	if (begin < 0 || end > s.width || end <= begin){
		return "";
	}else
	{
		//char *c = malloc(sizeof(char)*(end-begin));         
		char *c = fillerString('_', end-begin);
		for (int i = begin; i < end; i++){
			//printf("%c", s.letters[i]);
			c[i] = s.letters[i];
		}
		//printf("\n");
		return c;
	}
	
}
 
int main(){
	
	Str s = initStr("Example");
	printf("%s %d\n", s.letters, s.width);
	printf("%s" ,splice(s, 3, 7));
	return 0;
}
