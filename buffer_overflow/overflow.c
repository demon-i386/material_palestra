#include <stdio.h>

void roubarpremio(){
	puts("Falha no sistema, temos outro vencedor!\n");
}

void vencedor(){
	puts("Fulano ganhou, voce perdeu!!!!!!!!! lixooooo\n");

}

int main(){
	char name[12];
	puts("Sorteio, digite seu nome\n");
	gets(name);
	vencedor();
}
