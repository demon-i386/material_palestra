#include <stdio.h>

void add_addr(int *number){ // * = ponteiro que aponta para algo, se *x aponta para algo, x é
// esse algo
	*number += 1;
	printf("\nadd by memory address :: %p\n", *number);
}

void add(int number){
	number += 1;
	printf("\nsimple call address :: %p\n", &number);
}

int add_ret(int number){
	number +=1;
	return number;
}

int main(){
	int number = 666;
	printf("Address of variable :: %p\n", &number);
	add(number);
	printf("Copy object :: %d\n", number);

	add_addr(&number); // & = endereço, no caso, endereço de number
	printf("Send address :: %d\n", number);

	number = 666;
	number = add_ret(number);	// Python !!!!!!!!!!!!!!!!!!!!!!!

	printf("Get from return :: %d\n", number);
}
