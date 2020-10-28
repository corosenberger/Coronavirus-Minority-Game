
USER_NAME=chrisor

PythonHeaderLocation=C:\Users\$(USER_NAME)\anaconda3\include
PythonFlagLibLocation=C:\Users\$(USER_NAME)\anaconda3\libs
PythonVersionFlag=-lpython38

all:
	gcc -c -I $(PythonHeaderLocation) Disease.c -o DiseaseC.o
	gcc -shared -s DiseaseC.o -L $(PythonFlagLibLocation) $(PythonVersionFlag) -o DiseaseC.pyd
	del DiseaseC.o
	gcc -c -I $(PythonHeaderLocation) Group.c -o GroupC.o
	gcc -shared -s GroupC.o -L $(PythonFlagLibLocation) $(PythonVersionFlag) -o GroupC.pyd
	del GroupC.o

clean:
	rm DiseaseC.o
	rm DiseaseC.pyd
	rm GroupC.o
	rm GroupC.pyd

wclean:
	del DiseaseC.pyd
	del GroupC.pyd