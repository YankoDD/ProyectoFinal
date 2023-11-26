# Crear un diccionario para almacenar los datos
import sys
from datetime import datetime, timedelta #Para generar el codigo unico utilizando la fecha
import random#Para el numero de guia
usuario = []
factura = []
paquete = []
guias= []
estado="Estado:Creado"
desicion = 0
corr=0
    
    
#Ingresar Usuario
def agregar_usuarios():
    global usuario
    print ("Ingrese los datos del usuario")
    correo_usuario= "Correo Usuario:   "+str(input("Por favor, ingrese su correo electrónico: "))
    nombre_comercio = "Nombre Comercio:  "+input("Ingrese el nombre de su comercio: ")
    telefono_comercio= "Telefono Comercio:   "+str(input("Ingrese el teléfono de su comercio: "))
    nombre_dueno="Nombre Dueño:   "+ input("Ingrese el nombre del dueño: ")
    ubicacion_local= "Ubicacion Local:   "+str(input("Ingrese la ubicación de su local: "))
    usuario=correo_usuario,nombre_comercio,telefono_comercio,nombre_dueno,ubicacion_local
    print(usuario)
    
   
             
#Agregar Datos de Facturacion
def datos_factura():
    global factura
    print ("Ingrese los datos de la factura electronica")
    tipo_de_cedula= "Tipo de Cedula:   "+input("Por favor, ingrese el tipo de cedula: ")
    numero_de_cedula= "Numero de Cedula:   "+input("Por favor, ingrese el numero de cedula: ")
    nombre_de_usuario= "Nombre del Usuario:    "+input("Por favor, ingrese el nombre de el usuario: ")
    numero_telefono= "Numero de Telefono:   "+input("Por favor, ingrese el numero de telefono: ")
    correo_electronico= "Correo Electronico:   "+input("Por favor, ingrese el correo electronico: ")
    print("Debe agregar los datos de la direccion")
    provincia= "Provincia:   "+input("Por favor, ingrese la provincia: ")
    canton= "Canton:   "+input("Por favor, ingrese el canton: ")
    distrito="Distrito:  "+input("Por favor, ingrese el distrito: ")
    factura=tipo_de_cedula,numero_de_cedula,nombre_de_usuario,numero_telefono,correo_electronico,provincia,canton,distrito
    print(factura)
    
#Agregar Datos de Paquete
def datos_paquetes():
    global paquete
    global usuario
    global factura
    global estado
    global hora_actual
    print ("Para crear el paquete llena los siguientes datos:")
    nombre_destinatario="Nombre Destinario:  "+input("Igrese el nombre del destinatario: ")
    telefono_destinatario="Telefono Destinario:  "+input("Ingrese el numero del destinatario: ")
    cedula="Cedula:  "+input("Ingrese numero cedula: ")
    peso_paquete="Peso del Paquete:  "+input("Ingrese el peso del paquete: ")
    pago_entrega="Pago de la Entrega:  "+input("Cuanto debe pagar el cliente cuando recibe el paquete: ")
    remitente=input("Ingrese el nombre del comercio remitente:  ")
    numer_telefono=input("Ingrese el telefono del comercio")
    archivo1="usuarios.txt"
    archivo2="facturas.txt"
    buscar=remitente
    buscar1=numer_telefono
    with open(archivo1, "r") as archivo:
        for linea in archivo:
            if buscar in linea:
                print("Comercio:  \n",linea.strip())
    with open(archivo2, "r") as archiv:
        for linea in archiv:
            if buscar1 in linea:
                print("Factura:  \n",linea.strip())
    
    paquete=hora_actual,nombre_destinatario,telefono_destinatario,cedula,peso_paquete,pago_entrega,estado
    print(paquete)


# Solicitar Creación de guías
def creacion_guias ():
    global monto
    global guias
    numero_guia="Numero de Guia:  ",random.randint(1000,9999)
    nombre_comercio="Nombre del Comercio:   "+input("Ingrese el nombre de su comercio: ")
    telefono_comercio="Telefono del Comercio:  "+input("Ingrese el teléfono de su comercio: ")
    nombre_destinatario="Nombre del Destinatario:  "+input("Igrese el nombre del destinatario: ")
    telefono_destinatario="Telefono del Dertinatario:  "+input("Ingrese el numero del destinatario: ") 
# Verificacion de cobro
    requiere_cobro = int(input("¿Se requiere cobro?\n1.Sí\n2.No "))
    if requiere_cobro==1:
        monto = float(input("Monto a cobrar: "))
    else:
        print("Sin monto a cobrar")
        monto="Sin monto a cobrar"
    
    guias=numero_guia,nombre_comercio,telefono_comercio,nombre_destinatario,telefono_destinatario,monto,estado
    print(guias)      

#Rastreo del Paquete
def rastreo_paquete(): 
    archivo1="guias.txt"
    buscar=str(input("Digite el numero de guia:  ")) 
    with open(archivo1, "r") as archivo:
        for linea in archivo:
            if buscar in linea:
                print("Su paquete:  \n",linea.strip())
def estado_paquete():
    global hora_actual
    hora=datetime.now()-hora_actual
    print(hora)
    if hora<=timedelta(seconds=60):
        ruta="guias.txt"
        buscar="Estado:Fallido"
        nuevo="Estado:Creado"
        with open(ruta,"r") as archivo:
            lineas=archivo.readlines()
        for i, linea in enumerate(lineas):
            if buscar in linea:
                lineas[i]=linea.replace(buscar,nuevo)
        with open(ruta,"w") as archivo:
            archivo.writelines(lineas)
    if hora>=timedelta(seconds=60):
        ruta="guias.txt"
        buscar="Estado:Creado"
        nuevo="Estado:Recolectado"
        with open(ruta,"r") as archivo:
            lineas=archivo.readlines()
        for i, linea in enumerate(lineas):
            if buscar in linea:
                lineas[i]=linea.replace(buscar,nuevo)
        with open(ruta,"w") as archivo:
            archivo.writelines(lineas)
    if hora>=timedelta(seconds=120):
        ruta="guias.txt"
        buscar="Estado:Recolectado"
        nuevo="Estado:Entregado"
        with open(ruta,"r") as archivo:
            lineas=archivo.readlines()
        for i, linea in enumerate(lineas):
            if buscar in linea:
                lineas[i]=linea.replace(buscar,nuevo)
        with open(ruta,"w") as archivo:
            archivo.writelines(lineas)
    if hora>=timedelta(seconds=300):
        ruta="guias.txt"
        buscar="Estado:Creado"
        nuevo="Estado:Fallido"
        with open(ruta,"r") as archivo:
            lineas=archivo.readlines()
        for i, linea in enumerate(lineas):
            if buscar in linea:
                lineas[i]=linea.replace(buscar,nuevo)
        with open(ruta,"w") as archivo:
            archivo.writelines(lineas)       
hora_actual=datetime.now()           
print("Bienvenido a Mensajeria Fidelitas")

# Desicion para introducir datos
while desicion==0:
    
    print("Menú")
    desicion=int(input("1. Ingresar nuevo usuario\n2. Ingresar datos de facturacion\n3. Agregar datos de un nuevo paquete\n4. Creación de guías\n5.Cambiar el estado de un paquete\n6.Rastreo de Paquete\n7.Salir\nQue desea realizar el dia de hoy?: "))

#Datos de Usuario
    while desicion==1:
        agregar_usuarios()
        dato1=(str(usuario))
        corr=int(input("Estan los datos correctos?\n1.Si\n2.No"))
        if corr==1:
            with open("usuarios.txt","a") as user:
                user.write(dato1+"\n")
            print("Datos Guardados")
            desicion=int(input("Desea realizar alguna otra gestion?\n1. Si\n2. Salir  "))
            if desicion==1:
                desicion=0
            if desicion==2:
                print("Gracias por preferirnos")
                sys.exit()
        if corr==2:
            desicion=1
       
        
# Solicitar Datos de Factura
    while desicion==2:
        datos_factura()
        dato1=(str(factura))
        corr=int(input("Estan los datos correctos?\n1.Si\n2.No"))
        if corr==1:
            with open("facturas.txt","a") as fact:
                fact.write(dato1+"\n")
            print("Datos Guardados")
            desicion=int(input("Desea realizar alguna otra gestion?\n1. Si\n2. Salir  "))
            if desicion==1:
                desicion=0
            if desicion==2:
                print("Gracias por preferirnos")
                sys.exit()
        if corr==2:
            desicion=2
        
        
# Solicitar datos de la creacion de paquetes
    while desicion==3:
        if usuario == {}:
            print("Primero debe registrar su usuario")
            desicion=0
        else:   
            datos_paquetes()
            dato1=(str(paquete))
            corr=int(input("Estan los datos correctos?\n1.Si\n2.No"))
            if corr==1:
                with open("paquetes.txt","a") as fact:
                    fact.write(dato1+"\n")
                print("Datos Guardados")
                desicion=int(input("Desea realizar alguna otra gestion?\n1. Si\n2. Salir  "))
                if desicion==1:
                    desicion=0
                if desicion==2:
                    print("Gracias por preferirnos")
                    sys.exit()
            if corr==2:
                desicion=3
    


    
    while desicion==4:
        creacion_guias()
        dato1=(str(guias))
        corr=int(input("Estan los datos correctos?\n1.Si\n2.No"))
        if corr==1:
            with open("guias.txt","a") as facte:
                facte.write(dato1+"\n")
            print("Datos Guardados")
            desicion=int(input("Desea realizar alguna otra gestion?\n1. Si\n2. Salir  "))
            if desicion==1:
                desicion=0
            if desicion==2:
                print("Gracias por preferirnos")
                sys.exit()
        if corr==2:
            desicion=4

    while desicion==5:
        
        estado_paquete()
        desicion=0
    
    while desicion==6:
        rastreo_paquete()
        desicion=0
       
        
            
    while desicion==7:
        print("Gracias por preferirnos")
        sys.exit()
        
