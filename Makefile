
USER_NAME=PUT_YOUR_USER_NAME_HERE

PythonHeaderLocation=C:\Users\$(USER_NAME)\anaconda3\include
PythonFlagLibLocation=C:\Users\$(USER_NAME)\anaconda3\libs
PythonVersionFlag=-lpython38

all:
	gcc -c -I $(PythonHeaderLocation) CExtension.c -o CExtension.o
	gcc -shared -s CExtension.o -L $(PythonFlagLibLocation) $(PythonVersionFlag) -o CExtension.pyd
	del CExtension.o

clean:
	rm CExtension.o
	rm CExtension.pyd

wclean:
	del CExtension.pyd