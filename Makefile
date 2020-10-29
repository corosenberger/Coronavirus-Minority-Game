
USER_NAME=chrisor

PythonHeaderLocation=C:\Users\$(USER_NAME)\anaconda3\include
PythonFlagLibLocation=C:\Users\$(USER_NAME)\anaconda3\libs
PythonVersionFlag=-lpython38

all:
	gcc -c -I $(PythonHeaderLocation) ".\C Code\Disease.c" -o DiseaseC.o
	gcc -shared -s DiseaseC.o -L $(PythonFlagLibLocation) $(PythonVersionFlag) -o ".\Python Code\pyc\DiseaseC.pyd"
	del DiseaseC.o
	gcc -c -I $(PythonHeaderLocation) ".\C Code\Group.c" -o GroupC.o
	gcc -shared -s GroupC.o -L $(PythonFlagLibLocation) $(PythonVersionFlag) -o ".\Python Code\pyc\GroupC.pyd"
	del GroupC.o

clean:
	rm DiseaseC.o
	rm ".\Python Code\DiseaseC.pyd"
	rm GroupC.o
	rm ".\Python Code\GroupC.pyd"

wclean:
	del ".\Python Code\pyc\DiseaseC.pyd"
	del ".\Python Code\pyc\GroupC.pyd"