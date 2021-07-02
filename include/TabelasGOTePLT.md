# Tabelas GOT e PLT

Usadas ao linkar shared libraries, diferente de um estático, um compartilhado é mais leve, até
por que vive fora do arquivo compilado

- Static:
	- Elementos da biblioteca são martelados dentro do binário

- Shared:
	- Biblioteca mapeada dentro da memória do processo, referencias a simbolos feitos pelas
	  tabelas GOT e PLT

#### OBS ::. Por conta do ASLR, a base do objeto, assim como endereços como stack e heap são 
#### randomizados
### ldd binario <- mostra bibliotecas compartilhadas consumidas pelo binário

- Bibliotecas estáticas = binários pesados
- Bibliotecas dinâmicas = binários leves lmao


### GOT (Global Offset Table)
-	Lista de endereços, seus endereços referenciam simbolos externos
-	Preenchidos ao executar o binário <- biblioteca mapeada na memória virtual
		gdb> info proc mappings

### PLT (Procedure Linkage Table)
-	"Trampolim", pula para a referência especificada


call lmao@plt -> plt section -> GOT -> lmao (dentro do shared object) -> ret 
exemplo:  "switch case"

```
switch(funcao):
	case printf:
		jmp endereço
	case system:
		jmp endereço
```

Isso é chamado "relocation"

### Para os hackers... GOT Hijack!
https://systemoverlord.com/2017/03/19/got-and-plt-for-pwning.html
https://nuc13us.wordpress.com/2015/09/04/format-string-exploit-overwrite-got/

exemplo:
	gdb> set {int}GOT_ADDRESS = ADDRESS

format string...

