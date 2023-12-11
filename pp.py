
import re 
nombre_archivo = 'stats.txt'
n=0
numero_linea = 0
posicion_argumento = 19  
with open(nombre_archivo, 'r') as archivo:
    lineas = archivo.readlines()
    while numero_linea < len(lineas):
        palabras = lineas[numero_linea].split()
        if 19 < len(palabras):
            
            for i,linea in enumerate(lineas):
                if palabras[posicion_argumento] in linea:
                    numeros_solo = re.sub(r'\D', '', palabras[posicion_argumento])
                    n=n+int(numeros_solo)
            print("La cantidad total de coste de envio es de:  "+str(n))
        numero_linea=numero_linea+1
        n=0