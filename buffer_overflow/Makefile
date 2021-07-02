LIBC := /lib/x86_64-linux-gnu/libc.so.6

all:
	gcc overflow.c -o overflow -z execstack -fno-stack-protector -no-pie -z norelro
	sudo apt install gdb neovim -y
	pip3 install pwntools --user
	pip install ropper --user
	git clone https://github.com/longld/peda.git ~/peda
	echo "source ~/peda/peda.py" >> ~/.gdbinit
	echo "Done!"

find-offsets:
	strings -t x $(LIBC) | grep "/bin/sh"
	readelf -s   $(LIBC) | grep system
	readelf -s   $(LIBC) | grep puts
	readelf -s   $(LIBC) | grep exit
	readelf -s   $(LIBC) | grep execl
	readelf -s   $(LIBC) | grep execve	
