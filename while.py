#  ciclo while
import time
import os 
import sys 

inicio= time.time()
while contador < 10:
    print(contador)
    contador += 1
fin= time.time()
print("Tiempo transcurrido while:", fin-inicio)
inicio= time.time()
for contador in range(10):
    print(contador)
fin= time.time()
print("Tiempo transcurrido for:", fin-inicio)
if sys.platform == "win32":
    print ("el sistemas operativo win 32")
    os.system('cls')
else:
    print("el sistema operativo es otro win 64")
    os.system('clear')

    #manejo d fecha 
    from datetime import datetime 
    fecha = datetime.now()
    print(fecha)