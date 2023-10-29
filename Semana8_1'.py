# Crear un diccionario para almacenar los datos
import sys
usuario = {}
factura = {}
paquete = {}
desicion = 0

print("Bienvenido a Mensajeria Fidelitas")

# Desicion para introducir datos
while desicion==0:
    print("Que desea realizar el dia de hoy?")
    desicion=float(input("1. Ingresar nuevo usuario\n2. Ingresar datos de facturacion\n3. Agregar datos de un nuevo paquete\n4. Salir"))

#Datos de Usuario
    while desicion==1:
        print ("Ingrese los datos del usuario")
        usuario["correo_usuario"] = input("Por favor, ingrese su correo electrónico: ")
        usuario["nombre_comercio"] = input("Ingrese el nombre de su comercio: ")
        usuario["telefono_comercio"] = input("Ingrese el teléfono de su comercio: ")
        usuario["nombre_dueno"] = input("Ingrese el nombre del dueño: ")
        usuario["ubicacion_local"] = input("Ingrese la ubicación de su local: ")

# Mostrar los datos ingresados de la informacion del usuario
        print("Los datos ingresados son:  ")
        print("Los datos ingresados son los siguientes:")
        print("Correo electrónico: ", usuario["correo_usuario"])
        print("Nombre del comercio: " , usuario["nombre_comercio"])
        print("Teléfono del comercio: " , usuario["telefono_comercio"])
        print("Nombre del dueño: " , usuario["nombre_dueno"])
        print("Ubicación del local: " , usuario["ubicacion_local"])
        corr=float(input("Estan los datos correctos?\n1.Si\n2.No"))
        if corr==1:
            print("Datos Guardados")
            desicion=float(input("Desea realizar alguna otra gestion?\n1. Si\n2. Salir  "))
            if desicion==1:
                desicion=0
            if desicion==2:
                print("Gracias por preferirnos")
                sys.exit()
        if corr==2:
            desicion=1
    



# Solicitar Datos de Factura
    while desicion==2:
        print ("Ingrese los datos de la factura electronica")
        factura["tipo de cedula"] = input("Por favor, ingrese el tipo de cedula: ")
        factura["numero de cedula"] = input("Por favor, ingrese el numero de cedula: ")
        factura["nombre de el usuario"] = input("Por favor, ingrese el nombre de el usuario: ")
        factura["numero de telefono"] = input("Por favor, ingrese el numero de telefono: ")
        factura["correo electronico"] = input("Por favor, ingrese el correo electronico: ")
        print("Debe agregar los datos de la direccion")
        factura["provincia"] = input("Por favor, ingrese la provincia: ")
        factura["canton"] = input("Por favor, ingrese el canton: ")
        factura["distrito"] = input("Por favor, ingrese el distrito: ")
        
        


# Mostrar los datos de factura
        print("Datos de factura electronica")
        print("Tipo de cedula: ", factura["tipo de cedula"])
        print("Numero de cedula: ", factura["numero de cedula"])
        print("Nombre del usuario: ", factura["nombre de el usuario"])
        print("Numero de telefono: ", factura["numero de telefono"])
        print("Correo electronico: ", factura["correo electronico"])
        print("Direccion: \nProvincia", factura["provincia"])
        print("Canton: ", factura["canton"])
        print("Distrito: ", factura["distrito"])
        corr=float(input("Estan los datos correctos?\n1.Si\n2.No"))
        if corr==1:
            print("Datos Guardados")
            desicion=float(input("Desea realizar alguna otra gestion?\n1. Si\n2. Salir  "))
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
        if usuario!= {}:
            print ("Para crear el paquete llena los siguientes datos:")
            factura["nombre_destinatario"] = input("Igrese el nombre del destinatario: ")
            factura["telefono_destinatario"] = input("Ingrese el numero del destinatario: ")
            factura["cedula"] = input("Ingrese numero cedula: ")
            factura["peso_paquete"] = input("Ingrese el peso del paquete: ")
            factura["pago_entrega"] = input("Cuanto debe pagar el cliente cuando recibe elpaquete: ")
        

# Mostrar los datos de la creacion de paquetes
        
        
            print("Los datos del paquete ingresados son los siguientes:")
            print("Nombre del destinatario: ",factura["nombre_destinatario"])
            print("Numero de telefono: " , factura["telefono_destinatario"])
            print("Numero cedula: " , factura["cedula"])
            print("Peso del paquete: " , factura["peso_paquete"])
            print("Pago al recibir: " , factura["pago_entrega"])
            print("Ubicación del local: " , usuario["ubicacion_local"])
            corr=float(input("Estan los datos correctos?\n1.Si\n2.No"))
            if corr==1:
                print("Datos Guardados")
                desicion=float(input("Desea realizar alguna otra gestion?\n1. Si\n2. Salir  "))
                if desicion==1:
                    desicion=0
                if desicion==2:
                    print("Gracias por preferirnos")
                    sys.exit()
            if corr==2:
                desicion=3
    while desicion==4:
        print("Gracias por preferirnos")
        sys.exit()
        
