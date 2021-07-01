all:
	gcc overflow.c -o overflow -z execstack -fno-stack-protector -no-pie -z norelro
	sudo apt install gdb
	git clone https://github.com/longld/peda.git ~/peda
	echo "source ~/peda/peda.py" >> ~/.gdbinit
	echo "Done!"
