import customtkinter, tkinter
from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
import tkinter.messagebox
import random
import re
global paquete



with open ("guias.txt","r") as archivoo:
    lineas=archivoo.readlines()
for i,linea in enumerate(lineas):    
    azar=random.randint(00,99)
    if azar<100 and azar >=80:
        with open ("guias.txt","r") as fa:
            lines=fa.readlines()
        for i,lin in enumerate(lines):
            if "Estado:  Entregado" not in lin and "Estado:  Fallido" in lin: 
                lines[i]=lin.replace("Estado:  Fallido","Estado:  Entregado")
                with open ("guias.txt","w") as fa:
                    fa.writelines(lines)
            elif "Estado:  Entregado" not in lin and "Estado:  Creado" in lin:
                lines[i]=lin.replace("Estado:  Creado","Estado:  Entregado")
                with open ("guias.txt","w") as fa:
                    fa.writelines(lines)
            elif "Estado:  Entregado" not in lin and "Estado:  Recolectado" in lin:
                lines[i]=lin.replace("Estado:  Recolectado","Estado:  Entregado")
                with open ("guias.txt","w") as fa:
                    fa.writelines(lines)

    if azar<80 and azar >=60:
        with open ("guias.txt","r") as fa:
            lines=fa.readlines()
        for a,lina in enumerate(lines):
            if "Estado:  Recolectado" not in lina and "Estado:  Fallido" in lina: 
                lines[a]=lina.replace("Estado:  Fallido","Estado:  Recolectado")
                with open ("guias.txt","w") as fa:
                    fa.writelines(lines)
            elif "Estado:  Recolectado" not in lina and "Estado:  Creado" in lina:
                lines[a]=lina.replace("Estado:  Creado","Estado:  Recolectado")
                with open ("guias.txt","w") as fa:
                    fa.writelines(lines)
            elif "Estado:  Recolectado" not in lina and "Estado:  Entregado" in lina:
                lines[a]=lina.replace("Estado:  Entregado","Estado:  Recolectado")
                with open ("guias.txt","w") as fa:
                    fa.writelines(lines)

    if azar<60 and azar >=30:
        with open ("guias.txt","r") as fa:
            lines=fa.readlines()
        for e,lia in enumerate(lines):
            if "Estado:  Creado" not in lia and "Estado:  Fallido" in lia: 
                lines[e]=lia.replace("Estado:  Fallido","Estado:  Creado")
                with open ("guias.txt","w") as fa:
                    fa.writelines(lines)
            elif "Estado:  Creado" not in lia and "Estado:  Entregado" in lia:
                lines[e]=lia.replace("Estado:  Entregado","Estado:  Creado")
                with open ("guias.txt","w") as fa:
                    fa.writelines(lines)
            elif "Estado:  Creado" not in lia and "Estado:  Recolectado" in lia:
                lines[e]=lia.replace("Estado:  Recolectado","Estado:  Creado")
                with open ("guias.txt","w") as fa:
                    fa.writelines(lines)

    if azar<30 and azar >=1:
        with open ("guias.txt","r") as fa:
            lines=fa.readlines()
        for o,lie in enumerate(lines):
            if "Estado:  Fallido" not in lie and "Estado:  Entregado" in lie: 
                lines[o]=lie.replace("Estado:  Entregado","Estado:  Fallido")
                with open ("guias.txt","w") as fa:
                    fa.writelines(lines)
            elif "Estado:  Fallido" not in lie and "Estado:  Creado" in lie:
                lines[o]=lie.replace("Estado:  Creado","Estado:  Fallido")
                with open ("guias.txt","w") as fa:
                    fa.writelines(lines)
            elif "Estado:  Fallido" not in lie and "Estado:  Recolectado" in lie:
                lines[o]=lie.replace("Estado:  Recolectado","Estado:  Fallido")
                with open ("guias.txt","w") as fa:
                    fa.writelines(lines)

def registrar_cuenta():
    app1=customtkinter.CTk()
    app1.title("Registrar Cuenta")
    app1.geometry("800x600")
    # Crear y configurar los elementos de entrada
    entry_correo = tk.Entry(app1, width=30)
    entry_nombre_comercio = tk.Entry(app1, width=30)
    entry_telefono_comercio = tk.Entry(app1, width=30)
    entry_nombre_dueno = tk.Entry(app1, width=30)
    entry_ubicacion_local = tk.Entry(app1, width=30)
    def presion():
        correo_usuario = "Correo electronico:  "+entry_correo.get()
        nombre_comercio = "Nombre del Comercio:  "+entry_nombre_comercio.get()
        telefono_comercio = "Telefono del Comercio:   "+entry_telefono_comercio.get()
        nombre_dueno = "Nombre del Dueño:  "+entry_nombre_dueno.get()
        ubicacion_local = "Ubicacion del Local:  "+entry_ubicacion_local.get()
        usuario=correo_usuario,nombre_comercio,telefono_comercio,nombre_dueno,ubicacion_local
        pregunta1=tkinter.messagebox.askquestion("Verificacion de Datos",f"Estan los datos correctos?\n{correo_usuario}\n{nombre_comercio}\n{telefono_comercio}\n{nombre_dueno}\n{ubicacion_local}")
        if pregunta1=="yes":
            dato1=(str(usuario))
            with open("usuarios.txt","a") as user:
                user.write(dato1+"\n")
            tkinter.messagebox.showinfo("Datos Guardados!","Datos Guardados correctamente, gracias!")
            app1.destroy()
# Ubicar los elementos de entrada en la ventana usando place
    
    entry_correo.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    entry_nombre_comercio.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    entry_telefono_comercio.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    entry_nombre_dueno.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    entry_ubicacion_local.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    
    label_mensaje2 = customtkinter.CTkLabel(app1, text="Por favor, ingrese los datos de la cuenta.", font=("Helvetica", 16, "bold"), bg_color="black", padx=20, pady=10)
    label_mensaje2.pack(side=tk.TOP, fill=tk.X)
    
    label_correo = customtkinter.CTkLabel(app1, text="Ingrese el correo electronico:", font=("Helvetica", 16, "bold"),width=300)
    label_correo.place(relx=0.5,rely=0.15,anchor=tkinter.CENTER)
    
    label_nombre_comercio = customtkinter.CTkLabel(app1, text="Ingrese el nombre del comercio:", font=("Helvetica", 16, "bold"),width=300)
    label_nombre_comercio.place(relx=0.5,rely=0.25,anchor=tkinter.CENTER)
    
    label_telefono_comercio = customtkinter.CTkLabel(app1, text="Ingrese el telefono del comercio:", font=("Helvetica", 16, "bold"),width=300)
    label_telefono_comercio.place(relx=0.5,rely=0.35,anchor=tkinter.CENTER)
    
    label_nombre_dueno = customtkinter.CTkLabel(app1, text="Ingrese el nombre del dueño:", font=("Helvetica", 16, "bold"),width=300)
    label_nombre_dueno.place(relx=0.5,rely=0.45,anchor=tkinter.CENTER)
    
    label_ubicacion = customtkinter.CTkLabel(app1, text="Ingrese la ubicacion:", font=("Helvetica", 16, "bold"),width=300)
    label_ubicacion.place(relx=0.5,rely=0.55,anchor=tkinter.CENTER)
    
    agrego=customtkinter.CTkButton(app1,text="Agregar Cuenta",font=("Helvetica", 16, "bold"),bg_color="black",command=presion)
    agrego.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)
    
    app1.mainloop()

def registrar_factura():
    app1=customtkinter.CTk()
    app1.title("Registrar Factura")
    app1.geometry("800x600")
    # Crear y configurar los elementos de entrada
    entry_tipo_cedula = tk.Entry(app1, width=30)
    entry_numero_cedula = tk.Entry(app1, width=30)
    entry_nombre_usuario = tk.Entry(app1, width=30)
    entry_numero_telefono = tk.Entry(app1, width=30)
    entry_correo_electronico = tk.Entry(app1, width=30)
    entry_provincia = tk.Entry(app1, width=30)
    entry_canton = tk.Entry(app1, width=30)
    entry_distrito = tk.Entry(app1, width=30)
    def presion():
        tipo_cedula = "Tipo de Cedula:  "+entry_tipo_cedula.get()
        numero_cedula = "Numero de Cedula:  "+entry_numero_cedula.get()
        nombre_usuario = "Nombre de Usuario:   "+entry_nombre_usuario.get()
        numero_telefono = "Numero de Telefono:  "+entry_numero_telefono.get()
        correo_electronico = "Correo Electronico:  "+entry_correo_electronico.get()
        provincia= "Provincia:  "+entry_provincia.get()
        canton = "Canton:  "+entry_canton.get()
        distrito = "Distrito:  "+entry_distrito.get()
        usuario=tipo_cedula,numero_cedula,nombre_usuario,numero_telefono,correo_electronico,provincia,canton,distrito
        pregunta1=tkinter.messagebox.askquestion("Verificacion de Datos",f"{tipo_cedula}\n{numero_cedula}\n{nombre_usuario}\n{numero_telefono}\n{correo_electronico}\n{provincia}\n{canton}\n{distrito}")
        if pregunta1=="yes":
            dato1=(str(usuario))
            with open("facturas.txt","a") as user:
                user.write(dato1+"\n")
            tkinter.messagebox.showinfo("Datos Guardados!","Datos Guardados correctamente, gracias!")
            app1.destroy()
# Ubicar los elementos de entrada en la ventana usando place
    entry_tipo_cedula.place(relx=0.3, rely=0.2, anchor=tk.CENTER)
    entry_numero_cedula.place(relx=0.3, rely=0.3, anchor=tk.CENTER)
    entry_nombre_usuario.place(relx=0.3, rely=0.4, anchor=tk.CENTER)
    entry_numero_telefono.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
    entry_correo_electronico.place(relx=0.3, rely=0.6, anchor=tk.CENTER)
    entry_provincia.place(relx=0.7, rely=0.2, anchor=tk.CENTER)
    entry_canton.place(relx=0.7, rely=0.3, anchor=tk.CENTER)
    entry_distrito.place(relx=0.7, rely=0.4, anchor=tk.CENTER)
    
    label_mensaje2 = customtkinter.CTkLabel(app1, text="Por favor, ingrese los datos de Facturacion.", font=("Helvetica", 16, "bold"), bg_color="black", padx=20, pady=10)
    label_mensaje2.pack(side=tk.TOP, fill=tk.X)
    
    label_correo = customtkinter.CTkLabel(app1, text="Ingrese el tipo de cedula:", font=("Helvetica", 16, "bold"),width=300)
    label_correo.place(relx=0.3,rely=0.15,anchor=tkinter.CENTER)
    
    label_nombre_comercio = customtkinter.CTkLabel(app1, text="Ingrese numero de cedula:", font=("Helvetica", 16, "bold"),width=300)
    label_nombre_comercio.place(relx=0.3,rely=0.25,anchor=tkinter.CENTER)
    
    label_telefono_comercio = customtkinter.CTkLabel(app1, text="Ingrese el usuario:", font=("Helvetica", 16, "bold"),width=300)
    label_telefono_comercio.place(relx=0.3,rely=0.35,anchor=tkinter.CENTER)
    
    label_nombre_dueno = customtkinter.CTkLabel(app1, text="Ingrese el numero de telefono:", font=("Helvetica", 16, "bold"),width=300)
    label_nombre_dueno.place(relx=0.3,rely=0.45,anchor=tkinter.CENTER)
    
    label_ubicacion = customtkinter.CTkLabel(app1, text="Ingrese el correo electronico:", font=("Helvetica", 16, "bold"),width=300)
    label_ubicacion.place(relx=0.3,rely=0.55,anchor=tkinter.CENTER)
    
    label_ubicacion = customtkinter.CTkLabel(app1, text="Ingrese la provincia:", font=("Helvetica", 16, "bold"),width=300)
    label_ubicacion.place(relx=0.7,rely=0.15,anchor=tkinter.CENTER)
    
    label_ubicacion = customtkinter.CTkLabel(app1, text="Ingrese el canton:", font=("Helvetica", 16, "bold"),width=300)
    label_ubicacion.place(relx=0.7,rely=0.25,anchor=tkinter.CENTER)
    
    label_ubicacion = customtkinter.CTkLabel(app1, text="Ingrese el distrito:", font=("Helvetica", 16, "bold"),width=300)
    label_ubicacion.place(relx=0.7,rely=0.35,anchor=tkinter.CENTER)
    
    agrego=customtkinter.CTkButton(app1,text="Registrar Factura",font=("Helvetica", 16, "bold"),bg_color="black",command=presion)
    agrego.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)
    
    app1.mainloop()
    
def creacion_paquetes():
    global paquete
    app1=customtkinter.CTk()
    app1.title("Crear Paquete")
    app1.geometry("800x600")
    # Crear y configurar los elementos de entrada
    entry_destinatario = tk.Entry(app1, width=30)
    entry_telefono_destinatario = tk.Entry(app1, width=30)
    entry_cedula_destinatario = tk.Entry(app1, width=30)
    entry_peso_paquete = tk.Entry(app1, width=30)
    entry_coste_envio = tk.Entry(app1, width=30)
    entry_remitente = tk.Entry(app1, width=30)
    entry_telefono=tk.Entry(app1, width=30)
    
    
                
    def presion():
        global paquete
        nombre_destinatario = "Nombre del Destinatario:  "+entry_destinatario.get()
        telefono_destinatario = "Telefono del Destinatario:  "+entry_telefono_destinatario.get()
        numero_cedula_destinatario = "Cedula del Destinatario:   "+entry_cedula_destinatario.get()
        peso_paquete = "Peso del Paquete:  "+entry_peso_paquete.get()
        coste_envio = "Coste de Envio:  "+entry_coste_envio.get()
        remitente=entry_remitente.get()
        numer_telefono=entry_telefono.get()
        archivo1="usuarios.txt"
        archivo2="facturas.txt"
        buscar=remitente
        buscar1=numer_telefono
        with open(archivo1, "r") as archivo:
            for linea in archivo:
                if buscar in linea:
                    comer="Comercio:  \n"+linea.strip()
        with open(archivo2, "r") as archiv:
            for linea in archiv:
                if buscar1 in linea:
                    fact="Factura:  \n"+linea.strip()
        paquete=nombre_destinatario,telefono_destinatario,numero_cedula_destinatario,peso_paquete,coste_envio,"Estado:  Creado",comer,fact
        pregunta1=tkinter.messagebox.askquestion("Verificacion de Datos",f"{nombre_destinatario}\n{telefono_destinatario}\n{numero_cedula_destinatario}\n{peso_paquete}\n{coste_envio}\n{comer}\n{fact}")
        if pregunta1=="yes":
            dato1=(str(paquete))
            with open("paquetes.txt","a") as user:
                user.write(dato1+"\n")
            tkinter.messagebox.showinfo("Datos Guardados!","Datos Guardados correctamente, gracias!")
            app1.destroy()
# Ubicar los elementos de entrada en la ventana usando place
    entry_destinatario.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    entry_telefono_destinatario.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    entry_cedula_destinatario.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    entry_peso_paquete.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    entry_coste_envio.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    entry_remitente.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    entry_telefono.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    
    label_mensaje2 = customtkinter.CTkLabel(app1, text="Por favor, ingrese los datos del paquete.", font=("Helvetica", 16, "bold"), bg_color="black", padx=20, pady=10)
    label_mensaje2.pack(side=tk.TOP, fill=tk.X)
    
    label_correo = customtkinter.CTkLabel(app1, text="Ingrese el nombre del destinatario:", font=("Helvetica", 16, "bold"),width=300)
    label_correo.place(relx=0.5,rely=0.15,anchor=tkinter.CENTER)
    
    label_nombre_comercio = customtkinter.CTkLabel(app1, text="Ingrese el telefono del destinatario:", font=("Helvetica", 16, "bold"),width=300)
    label_nombre_comercio.place(relx=0.5,rely=0.25,anchor=tkinter.CENTER)
    
    label_telefono_comercio = customtkinter.CTkLabel(app1, text="Ingrese la cedula del destinatario:", font=("Helvetica", 16, "bold"),width=300)
    label_telefono_comercio.place(relx=0.5,rely=0.35,anchor=tkinter.CENTER)
    
    label_nombre_dueno = customtkinter.CTkLabel(app1, text="Ingrese el peso del paquete:", font=("Helvetica", 16, "bold"),width=300)
    label_nombre_dueno.place(relx=0.5,rely=0.45,anchor=tkinter.CENTER)
    
    label_ubicacion = customtkinter.CTkLabel(app1, text="Ingrese coste de envio:", font=("Helvetica", 16, "bold"),width=300)
    label_ubicacion.place(relx=0.5,rely=0.55,anchor=tkinter.CENTER)
    
    label_ubicacion = customtkinter.CTkLabel(app1, text="Ingrese el nombre del comercio:", font=("Helvetica", 16, "bold"),width=300)
    label_ubicacion.place(relx=0.5,rely=0.65,anchor=tkinter.CENTER)
    
    label_ubicacion = customtkinter.CTkLabel(app1, text="Ingrese el telefono del comercio:", font=("Helvetica", 16, "bold"),width=300)
    label_ubicacion.place(relx=0.5,rely=0.75,anchor=tkinter.CENTER)
    
    agrego=customtkinter.CTkButton(app1,text="Agregar Paquete",font=("Helvetica", 16, "bold"),bg_color="black",command=presion)
    agrego.place(relx=0.5,rely=0.9,anchor=tkinter.CENTER)
    
    app1.mainloop()

def creacion_guias():
    global paquete
    app1=customtkinter.CTk()
    app1.title("Creacion de Guias")
    app1.geometry("800x600")
    # Crear y configurar los elementos de entrada
    numero_guia="Numero de Guia:  ",random.randint(1000,9999)
    entry_cobro = tk.Entry(app1, width=30)
    entry_nombre_comercio = tk.Entry(app1, width=30)
    entry_telefono_comercio = tk.Entry(app1, width=30)
    entry_nombre_destinatario = tk.Entry(app1, width=30)
    entry_telefono_destinatario = tk.Entry(app1, width=30)
    def presion():
        global paquete
        nombre_comercio = "Nombre del Comercio:  "+entry_nombre_comercio.get()
        telefono_comercio = "Telefono del Comercio:   "+entry_telefono_comercio.get()
        nombre_destinatario = "Nombre del Destinatario:  "+entry_nombre_destinatario.get()
        telefono_destinatario = "Telefono del Destinatario:  "+entry_telefono_destinatario.get()
        cobrar = "Monto:  "+entry_cobro.get()
        estado="Estado:  Creado"
        guias=numero_guia,nombre_comercio,telefono_comercio,nombre_destinatario,telefono_destinatario,cobrar,estado
        pregunta1=tkinter.messagebox.askquestion("Verificacion de Datos",f"Estan los datos correctos?\n{nombre_comercio}\n{telefono_comercio}\n{nombre_destinatario}\n{telefono_destinatario}\n{cobrar}\n{numero_guia}\n{estado}")
        if pregunta1=="yes":
            dato1=(str(guias))
            with open("guias.txt","a") as user:
                user.write(dato1+"\n")
            tkinter.messagebox.showinfo("Datos Guardados!","Datos Guardados correctamente, gracias!")
            app1.destroy()
# Ubicar los elementos de entrada en la ventana usando place
    entry_nombre_comercio.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    entry_telefono_comercio.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    entry_nombre_destinatario.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    entry_telefono_destinatario.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    entry_cobro.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    
    label_mensaje2 = customtkinter.CTkLabel(app1, text="Por favor, ingrese los datos del paquete.", font=("Helvetica", 16, "bold"), bg_color="black", padx=20, pady=10)
    label_mensaje2.pack(side=tk.TOP, fill=tk.X)
    
    label_correo = customtkinter.CTkLabel(app1, text="Ingrese el nombre del comercio:", font=("Helvetica", 16, "bold"),width=300)
    label_correo.place(relx=0.5,rely=0.15,anchor=tkinter.CENTER)
    
    label_nombre_comercio = customtkinter.CTkLabel(app1, text="Ingrese el telefono del comercio:", font=("Helvetica", 16, "bold"),width=300)
    label_nombre_comercio.place(relx=0.5,rely=0.25,anchor=tkinter.CENTER)
    
    label_telefono_comercio = customtkinter.CTkLabel(app1, text="Ingrese el nombre del destinatario:", font=("Helvetica", 16, "bold"),width=300)
    label_telefono_comercio.place(relx=0.5,rely=0.35,anchor=tkinter.CENTER)
    
    label_nombre_dueno = customtkinter.CTkLabel(app1, text="Ingrese el telefono del destinatario:", font=("Helvetica", 16, "bold"),width=300)
    label_nombre_dueno.place(relx=0.5,rely=0.45,anchor=tkinter.CENTER)
    
    label_cobro = customtkinter.CTkLabel(app1, text="Ingrese el monto a pagar:", font=("Helvetica", 16, "bold"),width=300)
    label_cobro.place(relx=0.5,rely=0.55,anchor=tkinter.CENTER)
    
    agrego=customtkinter.CTkButton(app1,text="Agregar Guia",font=("Helvetica", 16, "bold"),bg_color="black",command=presion)
    agrego.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)
    app1.mainloop()

def rastreo_paquetes():
    app1=customtkinter.CTk()
    app1.title("Rastrear Paquete")
    app1.geometry("400x200")
    
    entry_guia_number = tk.Entry(app1, width=30)
    
    
    label_guia = customtkinter.CTkLabel(app1, text="Ingrese su numero de guia:", font=("Helvetica", 16, "bold"),width=300)
    label_guia.place(relx=0.5,rely=0.15,anchor=tkinter.CENTER)
    def ras():
        numer=entry_guia_number.get()  
        with open ("guias.txt","r") as file:
            lineas=file.readlines()
            for i, linea in enumerate(lineas):
                if numer in linea:
                    tkinter.messagebox.showinfo("Rastreo segun numero de guia",linea)
                    app1.destroy()
    entry_guia_number.place(relx=0.5, rely=0.3, anchor=tk.CENTER) 
    rastrear=customtkinter.CTkButton(app1,text="Rastrear",font=("Helvetica", 16, "bold"),bg_color="black",command=ras)
    rastrear.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
    app1.mainloop()

def modulo_estadisticas():
    pato=customtkinter.CTk()
    pato.title("Modulo Estadistico")
    pato.geometry("400x200")
    entry_ingresar_negocio = tk.Entry(pato, width=30)
    def stats():
        
        with open ("stats.txt","w") as jua:
            jua.writelines("")
        n=0
        buscar=entry_ingresar_negocio.get()
        with open("paquetes.txt","r") as tex:
            lineas=tex.readlines()
        for i,linea in enumerate(lineas):
            if buscar in linea:
                n=n+1
                with open ("stats.txt","a") as jua:
                    jua.writelines(linea+"\n")
                    
                    
        with open ("stats.txt","r") as jua:
            lineas=jua.readlines()
        nombre_archivo = 'stats.txt'
        m=0
        numero_linea = 0
        posicion_argumento = 7  
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            while numero_linea < len(lineas):
                palabras = lineas[numero_linea].split()
                if 7 < len(palabras):
        
                    print(palabras[posicion_argumento])
                    
                    for i,linea in enumerate(lineas):
                        if palabras[posicion_argumento] in linea:
                            m=m+1
                    potatoe="La cantidad de paquetes para el numero "+palabras[posicion_argumento]+"es de :  "+str(m)+"\n"
                numero_linea=numero_linea+1
                m=0
        
        s=0
        numero_linea = 0
        posicion_argumento = 11  
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            while numero_linea < len(lineas):
                palabras = lineas[numero_linea].split()
                if 11 < len(palabras):
        
                    print(palabras[posicion_argumento])
                    
                    for i,linea in enumerate(lineas):
                        if palabras[posicion_argumento] in linea:
                            s=s+1
                    potatoe1="La cantidad de paquetes para la cedula "+palabras[posicion_argumento]+"es de :  "+str(s)+"\n"
                numero_linea=numero_linea+1
                s=0
        
        p=0
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
                            p=p+int(numeros_solo)
                    potatoe2=("La cantidad total de coste de envio es de:  "+str(p))
                numero_linea=numero_linea+1
                p=0                   
        app1=customtkinter.CTk()            
        app1.title("Modulo Estadistico")
        app1.geometry("900x700")
        nos="Cantidad de Paquetes Enviados:  "+str(n)
        info = customtkinter.CTkLabel(app1, text=(nos+"\n"+potatoe+potatoe1+potatoe2), font=("Helvetica", 16, "bold"),width=300)
        info.place(relx=0.5,rely=0.15,anchor=tkinter.CENTER)
        info1 = customtkinter.CTkTextbox(app1, font=("Helvetica", 16, "bold"),width=600,height=500,wrap=tkinter.NONE)
        info1.place(relx=0.5,rely=0.60,anchor=tkinter.CENTER)
        info1.insert(tkinter.END,lineas)
        barra1=customtkinter.CTkScrollbar(info1,command=info1.yview)
        barra1.grid(row=0,column=1,sticky="ns")
        barra2=customtkinter.CTkScrollbar(info1,command=info1.xview)
        barra2.grid(row=0,column=1,sticky="ns")
        info1.configure(yscrollcommand=barra2.set)
        app1.destroy()
        app1.mainloop()
    
    instruccion=customtkinter.CTkLabel(pato, text="Introduzca el nombre del Comercio:", font=("Helvetica", 16, "bold"),width=300)
    instruccion.place(relx=0.5,rely=0.15,anchor=tkinter.CENTER)
    entry_ingresar_negocio.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    buscar_boton=customtkinter.CTkButton(pato,text="Buscar",font=("Helvetica", 16, "bold"),bg_color="black",command=stats)
    buscar_boton.place(relx=0.5,rely=0.45, anchor=tkinter.CENTER)
        
    pato.mainloop()
        
    
customtkinter.set_appearance_mode("dark")


app=customtkinter.CTk()
app.title("Mensajeria Fidelitas")
app.geometry("800x600")


label_mensaje = customtkinter.CTkLabel(app, text="Bienvenido a Mensajeria Fidelitas", font=("Helvetica", 16, "bold"), bg_color="black", padx=20, pady=10)
label_mensaje.pack(side=tk.TOP, fill=tk.X)

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
image = Image.open("fidelitas.jpg")  
image = image.resize((screen_width, screen_height))
tk_image = ImageTk.PhotoImage(image)
label = tk.Label(app, image=tk_image)
label.pack(fill="both", expand=True)


frame=customtkinter.CTkFrame(app,
                             width=300,
                             height=350,
                             bg_color="black"
                             )
frame.place(relx=0.5, rely=0.5,anchor=tkinter.CENTER)

label_menu = customtkinter.CTkLabel(frame, text="¿Que desea hacer hoy?", font=("Helvetica", 16, "bold"), bg_color="black",width=300)
label_menu.place(relx=0.5,rely=0.04,anchor=tkinter.CENTER)
button_cuenta=customtkinter.CTkButton(frame,text="Registrar Cuenta", font=("Helvetica", 16, "bold"),bg_color="black",command=registrar_cuenta)
button_cuenta.place(relx=0.5,rely=0.15,anchor=tkinter.CENTER)
button_factura=customtkinter.CTkButton(frame,text="Registrar Factura", font=("Helvetica", 16, "bold"),bg_color="black",command=registrar_factura)
button_factura.place(relx=0.5,rely=0.30,anchor=tkinter.CENTER)
button_paquete=customtkinter.CTkButton(frame,text="Crear Paquete", font=("Helvetica", 16, "bold"),bg_color="black",command=creacion_paquetes)
button_paquete.place(relx=0.5,rely=0.45,anchor=tkinter.CENTER)
button_guia=customtkinter.CTkButton(frame,text="Crear Guias", font=("Helvetica", 16, "bold"),bg_color="black",command=creacion_guias)
button_guia.place(relx=0.5,rely=0.60,anchor=tkinter.CENTER)
button_rastreo=customtkinter.CTkButton(frame,text="Rastreo de Paquetes", font=("Helvetica", 16, "bold"),bg_color="black",command=rastreo_paquetes)
button_rastreo.place(relx=0.5,rely=0.75,anchor=tkinter.CENTER)
button_modulo=customtkinter.CTkButton(frame,text="Estadisticas", font=("Helvetica", 16, "bold"),bg_color="black",command=modulo_estadisticas)
button_modulo.place(relx=0.5,rely=0.90,anchor=tkinter.CENTER)

app.mainloop()