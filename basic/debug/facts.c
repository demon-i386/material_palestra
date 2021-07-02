
#include <stdlib.h>

// https://i.stack.imgur.com/WY54O.png <- diagrama de chamadas

void _start() {
	puts("Wtf? quem é esse???");
	int ret = caneta();
	exit(ret);
}

int caneta() {
	puts("No final, main() não é o principal...");
}

