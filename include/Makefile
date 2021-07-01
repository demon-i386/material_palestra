.PHONY: success
PWD := `pwd`
CC = gcc

linkererror:
	@ gcc main.c -o failed

static:
	@ $(CC) -c main.c -o main.o
	@ $(CC) -c external.c -o external.o
	@ ar crv ./libstatic.a ./external.o
	@ $(CC) main.o  -L. -lstatic -o main-static

shared:
	# gcc assume que todas as bibliotecas compartilhadas começam com "lib" e terminam
	# com a extenção .so

	@ $(CC) -c -Wall -Werror -fpic external.c # compilando com PIC (position independant code)
	@ $(CC) -shared -o libexternal.so external.o # criando shared object do objeto
	@ $(CC) -L. -o main-shared main.c -lexternal
	@ export LD_LIBRARY_PATH=$(PWD)/:$(LD_LIBRARY_PATH)

	# LD_LIBARY_PATH é uma váriável de ambiente que enumera pastas onde devem
	# ser procuradas bibliotecas

	# bibliotecas compartilhadas tem seus simbolos "mapeados" na memória virtual
	# de um processo

	#
