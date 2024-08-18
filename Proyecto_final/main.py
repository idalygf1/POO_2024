import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Para usar estilos modernos
from Usuarios.usuarios import *
from Movimientos.movimientos import *
from Cuentas.cuentas import *
from funciones import *
from datetime import datetime

class BanfuturoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BANFUTURO")
        self.geometry("1024x768")  # Tamaño optimizado para una pantalla de 16 pulgadas
        self.resizable(True, True)  # Permite redimensionar la ventana
        self.config(bg="#283149")  # Fondo azul oscuro
        self.numero_cuenta = None
        self.estilo = ttk.Style()  # Para estilos modernos
        self.estilo.configure("TButton", font=("Arial", 14), padding=10, background="#000000", foreground="#000000")
        self.estilo.configure("TLabel", font=("Arial", 16), background="#283149", foreground="#ffffff")
        self.crear_menu_principal()

    def crear_menu_principal(self):
        self.limpiar_ventana()

        frame_principal = tk.Frame(self, bg="#404B69")
        frame_principal.place(relx=0.5, rely=0.5, anchor="center")  # Centro en la pantalla

        tk.Label(frame_principal, text="...:: BIENVENIDO A BANFUTURO ::...", font=("Arial", 36, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=30)
        tk.Label(frame_principal, text="Ingrese su número de cuenta:", font=("Arial", 28), bg="#404B69", fg="#DBEDF3").pack(pady=20)

        self.entrada_cuenta = tk.Entry(frame_principal, font=("Arial", 28), width=30)
        self.entrada_cuenta.pack(pady=20)

        tk.Label(frame_principal, text="Ingrese su pin:", font=("Arial", 28), bg="#404B69", fg="#DBEDF3").pack(pady=20)

        self.entrada_pin = tk.Entry(frame_principal, show="*", font=("Arial", 28), width=30)
        self.entrada_pin.pack(pady=20)

        ttk.Button(frame_principal, text="Iniciar Sesión", command=self.iniciar_sesion, style="TButton").pack(pady=30)
        self.estilo.configure("TButton", font=("Arial", 24), padding=20)



    def iniciar_sesion(self):
        self.numero_cuenta = int(self.entrada_cuenta.get())
        pin = self.entrada_pin.get()

        if Adminsitradores.iniciarSesion(self.numero_cuenta, pin):
            self.crear_menu_admin()
        elif Clientes.iniciarSesion(self.numero_cuenta, pin):
            cliente = Clientes.obtenerClientePorNumeroCuenta(self.numero_cuenta)
            print(f"Cliente encontrado: {cliente}")  # Depuración

            if cliente:
                self.id_credito = cliente.get("id_credito", None)
                self.id_debito = cliente.get("id_debito", None)
                self.crear_menu_clientes()
            else:
                messagebox.showerror("Error", "No se encontró la cuenta de crédito o débito asociada")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectas")




    
    def crear_menu_admin(self):
        self.limpiar_ventana()
        frame_admin = tk.Frame(self, bg="#404B69")
        frame_admin.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(frame_admin, text="..:: CONTROL DE USUARIOS ::..", font=("Arial", 24, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        ttk.Button(frame_admin, text="ADMINISTRAR CLIENTES", command=self.admin_clientes).pack(pady=10)
        ttk.Button(frame_admin, text="ADMINISTRAR GERENTES", command=self.admin_gerentes).pack(pady=10)
        ttk.Button(frame_admin, text="SALIR", command=self.crear_menu_principal).pack(pady=10)
    
    def admin_clientes(self):
        self.limpiar_ventana()
        frame_clientes = tk.Frame(self, bg="#404B69")
        frame_clientes.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(frame_clientes, text="ADMINISTRAR CLIENTES", font=("Arial", 24, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        ttk.Button(frame_clientes, text="Agregar Cliente", command=self.agregar_cliente).pack(pady=10)
        ttk.Button(frame_clientes, text="Mostrar Clientes", command=self.mostrar_clientes).pack(pady=10)
        ttk.Button(frame_clientes, text="Actualizar Cliente", command=self.actualizar_cliente).pack(pady=10)
        ttk.Button(frame_clientes, text="Eliminar Cliente", command=self.eliminar_cliente).pack(pady=10)
        ttk.Button(frame_clientes, text="Regresar", command=self.crear_menu_admin).pack(pady=10)
    
    def agregar_cliente(self):
        self.limpiar_ventana()
        frame_agregar = tk.Frame(self, bg="#404B69")
        frame_agregar.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_agregar, text="Agregar Cliente", font=("Arial", 24, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        self.crear_formulario_cliente(frame_agregar)
        ttk.Button(frame_agregar, text="Guardar", command=self.guardar_cliente).pack(pady=20)
        ttk.Button(frame_agregar, text="Regresar", command=self.admin_clientes).pack(pady=10)

    def crear_formulario_cliente(self, frame):
        self.campos = {}
        campos_texto = [
            "ID Cuenta", "PIN", "Nombres", "Apellido Paterno",
            "Apellido Materno", "Fecha de Nacimiento", "RFC",
            "Régimen", "Calle", "Número de Casa", "Colonia",
            "ID Débito", "ID Crédito", "Saldo Aprobado"
        ]

        # Ajusta el ancho de las etiquetas y entradas
        label_width = 20
        entry_width = 35

        for i in range(0, len(campos_texto), 2):
            frame_form = tk.Frame(frame, bg="#404B69")
            frame_form.pack(fill='x', pady=5)

            # Primera columna de campos
            tk.Label(frame_form, text=f"{campos_texto[i]}:", 
                    font=("Arial", 16), width=label_width, anchor="e", bg="#404B69", fg="#DBEDF3").pack(side="left", padx=5)
            self.campos[campos_texto[i]] = tk.Entry(frame_form, 
                                                    font=("Arial", 16), width=entry_width)
            self.campos[campos_texto[i]].pack(side="left", padx=5)

            # Verifica si hay un segundo campo en la misma fila
            if i + 1 < len(campos_texto):
                # Segunda columna de campos
                tk.Label(frame_form, text=f"{campos_texto[i + 1]}:", 
                        font=("Arial", 16), width=label_width, anchor="e", bg="#404B69", fg="#DBEDF3").pack(side="left", padx=5)
                self.campos[campos_texto[i + 1]] = tk.Entry(frame_form, 
                                                            font=("Arial", 16), width=entry_width)
                self.campos[campos_texto[i + 1]].pack(side="left", padx=5)





    def guardar_cliente(self):
        datos_cliente = {campo: self.campos[campo].get() for campo in self.campos}
        cliente = Clientes(
            int(datos_cliente["ID Cuenta"]), datos_cliente["PIN"], datos_cliente["Nombres"], 
            datos_cliente["Apellido Paterno"], datos_cliente["Apellido Materno"], 
            datos_cliente["Fecha de Nacimiento"], datos_cliente["RFC"], datos_cliente["Régimen"], 
            datos_cliente["Calle"], datos_cliente["Número de Casa"], datos_cliente["Colonia"], 
            datos_cliente["ID Débito"], datos_cliente["ID Crédito"], float(datos_cliente["Saldo Aprobado"])
        )
        resultado = cliente.crearCliente()
        if resultado:
            messagebox.showinfo("Éxito", "Cliente agregado correctamente")
        else:
            messagebox.showerror("Error", "No se pudo agregar el cliente")
        self.admin_clientes()

    def mostrar_clientes(self):
        self.limpiar_ventana()
        frame_mostrar = tk.Frame(self, bg="#404B69")
        frame_mostrar.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_mostrar, text="Mostrar Clientes", font=("Arial", 24, "bold"), bg="#404B69", fg="#DBEDF3").grid(row=0, column=0, columnspan=10, pady=20)

        headers = ["N_Cuenta", "Nombres", "Apellido Paterno", "Apellido Materno", "Fecha nacimiento", "RFC", "Regimen", "Calle", "N°", "Colonia"]
        for col, header in enumerate(headers):
            tk.Label(frame_mostrar, text=header, font=("Arial", 14, "bold"), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=1, column=col, sticky="nsew")

        clientes = Clientes.mostrarClientes()
        
        if len(clientes) > 0:
            for index, i in enumerate(clientes):
                tk.Label(frame_mostrar, text=i[0], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=0, sticky="nsew")
                tk.Label(frame_mostrar, text=i[2], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=1, sticky="nsew")
                tk.Label(frame_mostrar, text=i[3], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=2, sticky="nsew")
                tk.Label(frame_mostrar, text=i[4], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=3, sticky="nsew")
                tk.Label(frame_mostrar, text=i[5], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=4, sticky="nsew")
                tk.Label(frame_mostrar, text=i[6], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=5, sticky="nsew")
                tk.Label(frame_mostrar, text=i[7], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=6, sticky="nsew")
                tk.Label(frame_mostrar, text=i[8], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=7, sticky="nsew")
                tk.Label(frame_mostrar, text=i[9], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=8, sticky="nsew")
                tk.Label(frame_mostrar, text=i[10], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=9, sticky="nsew")
        else:
            tk.Label(frame_mostrar, text="No existen clientes registrados...", font=("Arial", 14), bg="#404B69", fg="#DBEDF3").grid(row=2, column=0, columnspan=10, pady=10)
        
        ttk.Button(frame_mostrar, text="Regresar", command=self.admin_clientes).grid(row=index+3, column=0, columnspan=10, pady=20)



    def actualizar_cliente(self):
        self.limpiar_ventana()
        frame_actualizar = tk.Frame(self, bg="#404B69")
        frame_actualizar.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_actualizar, text="Actualizar Cliente", font=("Arial", 24, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        self.crear_formulario_cliente(frame_actualizar)
        ttk.Button(frame_actualizar, text="Actualizar", command=self.guardar_actualizacion_cliente).pack(pady=20)
        ttk.Button(frame_actualizar, text="Regresar", command=self.admin_clientes).pack(pady=10)

    def guardar_actualizacion_cliente(self):
        datos_cliente = {campo: self.campos[campo].get() for campo in self.campos}
        resultado = Clientes.actualizarCliente(
            int(datos_cliente["ID Cuenta"]), datos_cliente["PIN"], datos_cliente["Nombres"], 
            datos_cliente["Apellido Paterno"], datos_cliente["Apellido Materno"], 
            datos_cliente["Fecha de Nacimiento"], datos_cliente["RFC"], datos_cliente["Régimen"], 
            datos_cliente["Calle"], datos_cliente["Número de Casa"], datos_cliente["Colonia"]
        )
        if resultado:
            messagebox.showinfo("Éxito", f"El cliente con N_cuenta {datos_cliente['ID Cuenta']} se actualizó correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo actualizar el cliente")
        self.admin_clientes()

    def eliminar_cliente(self):
        self.limpiar_ventana()
        frame_eliminar = tk.Frame(self, bg="#404B69")
        frame_eliminar.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        tk.Label(frame_eliminar, text="Eliminar Cliente", font=("Arial", 28, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=30)

        # Etiqueta y campo de entrada con mejoras
        tk.Label(frame_eliminar, text="ID del cliente a eliminar:", font=("Arial", 20), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        self.entrada_id_eliminar = tk.Entry(frame_eliminar, font=("Arial", 18), width=30, bd=5, relief="solid") # Cambios aquí
        self.entrada_id_eliminar.pack(pady=15, ipadx=10, ipady=5)  # Padding adicional

        # Botones
        ttk.Button(frame_eliminar, text="Eliminar", command=self.confirmar_eliminar_cliente).pack(pady=20)
        ttk.Button(frame_eliminar, text="Regresar", command=self.admin_clientes).pack(pady=10)



    def confirmar_eliminar_cliente(self):
        id_cuenta = int(self.entrada_id_eliminar.get())
        resultado = Clientes.eliminarCliente(id_cuenta)
        if resultado:
            messagebox.showinfo("Éxito", f"El cliente con N_cuenta {id_cuenta} se eliminó correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo eliminar el cliente")
        self.admin_clientes()

    def admin_gerentes(self):
        self.limpiar_ventana()
        frame_gerentes = tk.Frame(self, bg="#404B69")
        frame_gerentes.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(frame_gerentes, text="ADMINISTRAR GERENTES", font=("Arial", 24, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        ttk.Button(frame_gerentes, text="Agregar Gerente", command=self.agregar_gerente).pack(pady=10)
        ttk.Button(frame_gerentes, text="Mostrar Gerentes", command=self.mostrar_gerentes).pack(pady=10)
        ttk.Button(frame_gerentes, text="Actualizar Gerente", command=self.actualizar_gerente).pack(pady=10)
        ttk.Button(frame_gerentes, text="Eliminar Gerente", command=self.eliminar_gerente).pack(pady=10)
        ttk.Button(frame_gerentes, text="Regresar", command=self.crear_menu_admin).pack(pady=10)

    def agregar_gerente(self):
        self.limpiar_ventana()
        frame_agregar = tk.Frame(self, bg="#404B69")
        frame_agregar.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_agregar, text="Agregar Gerente", font=("Arial", 24, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        self.crear_formulario_gerente(frame_agregar)
        ttk.Button(frame_agregar, text="Guardar", command=self.guardar_gerente).pack(pady=20)
        ttk.Button(frame_agregar, text="Regresar", command=self.admin_gerentes).pack(pady=10)

    def crear_formulario_gerente(self, frame):
        self.campos = {}
        campos_texto = [
            "ID Gerente", "PIN", "Nombres", "Apellido Paterno",
            "Apellido Materno", "RFC", "Salario", "Puesto"
        ]
        
        # Crear un frame para el formulario de 4 columnas
        frame_formulario = tk.Frame(frame, bg="#404B69")
        frame_formulario.pack(padx=10, pady=10)
        
        for i, campo in enumerate(campos_texto):
            row, col = divmod(i, 2)  # Organiza en 2 columnas
            tk.Label(frame_formulario, text=f"{campo}:",
                    font=("Arial", 18), bg="#404B69", fg="#DBEDF3").grid(row=row, column=col*2, padx=10, pady=10, sticky="w")
            self.campos[campo] = tk.Entry(frame_formulario, font=("Arial", 18), width=25)
            self.campos[campo].grid(row=row, column=col*2 + 1, padx=10, pady=10, sticky="w")



    def guardar_gerente(self):
        datos_gerente = {campo: self.campos[campo].get() for campo in self.campos}
        gerente = Adminsitradores(
            int(datos_gerente["ID Gerente"]), datos_gerente["Nombres"], datos_gerente["Apellido Paterno"],
            datos_gerente["Apellido Materno"], datos_gerente["RFC"], datos_gerente["PIN"], 
            float(datos_gerente["Salario"]), datos_gerente["Puesto"]
        )
        resultado = gerente.crearAdministrador()
        if resultado:
            messagebox.showinfo("Éxito", "Gerente agregado correctamente")
        else:
            messagebox.showerror("Error", "No se pudo agregar el gerente")
        self.admin_gerentes()

    def mostrar_gerentes(self):
        self.limpiar_ventana()
        frame_mostrar = tk.Frame(self, bg="#404B69")
        frame_mostrar.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_mostrar, text="Mostrar Gerentes", font=("Arial", 24, "bold"), bg="#404B69", fg="#DBEDF3").grid(row=0, column=0, columnspan=7, pady=20)

        headers = ["ID_Gerente", "Nombres", "Apellido Paterno", "Apellido Materno", "RFC", "Salario", "Puesto"]
        for col, header in enumerate(headers):
            tk.Label(frame_mostrar, text=header, font=("Arial", 14, "bold"), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=1, column=col, sticky="nsew")

        gerentes = Adminsitradores.mostrarAdministrador()

        if len(gerentes) > 0:
            for index, i in enumerate(gerentes):
                tk.Label(frame_mostrar, text=i[0], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=0, sticky="nsew")
                tk.Label(frame_mostrar, text=i[1], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=1, sticky="nsew")
                tk.Label(frame_mostrar, text=i[2], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=2, sticky="nsew")
                tk.Label(frame_mostrar, text=i[3], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=3, sticky="nsew")
                tk.Label(frame_mostrar, text=i[4], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=4, sticky="nsew")
                tk.Label(frame_mostrar, text=i[6], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=5, sticky="nsew")
                tk.Label(frame_mostrar, text=i[7], font=("Arial", 14), bg="#404B69", fg="#DBEDF3", padx=10, pady=5).grid(row=index+2, column=6, sticky="nsew")
        else:
            tk.Label(frame_mostrar, text="No existen gerentes registrados...", font=("Arial", 14), bg="#404B69", fg="#DBEDF3").grid(row=2, column=0, columnspan=7)

        ttk.Button(frame_mostrar, text="Regresar", command=self.admin_gerentes).grid(row=index+3, column=0, columnspan=7, pady=20)


    def actualizar_gerente(self):
        self.limpiar_ventana()
        frame_actualizar = tk.Frame(self, bg="#404B69")
        frame_actualizar.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_actualizar, text="Actualizar Gerente", font=("Arial", 24, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        self.crear_formulario_gerente(frame_actualizar)
        ttk.Button(frame_actualizar, text="Actualizar", command=self.guardar_actualizacion_gerente).pack(pady=20)
        ttk.Button(frame_actualizar, text="Regresar", command=self.admin_gerentes).pack(pady=10)

    def guardar_actualizacion_gerente(self):
        datos_gerente = {campo: self.campos[campo].get() for campo in self.campos}
        resultado = Adminsitradores.actualizarAdministrador(
            int(datos_gerente["ID Gerente"]), datos_gerente["Nombres"], datos_gerente["Apellido Paterno"],
            datos_gerente["Apellido Materno"], datos_gerente["RFC"], datos_gerente["PIN"], 
            float(datos_gerente["Salario"]), datos_gerente["Puesto"]
        )
        if resultado:
            messagebox.showinfo("Éxito", f"El gerente con N_cuenta {datos_gerente['ID Gerente']} se actualizó correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo actualizar el gerente")
        self.admin_gerentes()

    def eliminar_gerente(self):
        self.limpiar_ventana()
        frame_eliminar = tk.Frame(self, bg="#404B69")
        frame_eliminar.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        tk.Label(frame_eliminar, text="Eliminar Gerente", font=("Arial", 28, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=30)

        # Etiqueta y campo de entrada con mejoras
        tk.Label(frame_eliminar, text="ID del gerente a eliminar:", font=("Arial", 20), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        self.entrada_id_eliminar = tk.Entry(frame_eliminar, font=("Arial", 18), width=30, bd=5, relief="solid")  # Cambios aquí
        self.entrada_id_eliminar.pack(pady=15, ipadx=10, ipady=5)  # Padding adicional

        # Botones
        ttk.Button(frame_eliminar, text="Eliminar", command=self.confirmar_eliminar_gerente).pack(pady=20)
        ttk.Button(frame_eliminar, text="Regresar", command=self.admin_gerentes).pack(pady=10)


    def confirmar_eliminar_gerente(self):
        id_gerente = int(self.entrada_id_eliminar.get())
        resultado = Adminsitradores.eliminarAdministrador(id_gerente)
        if resultado:
            messagebox.showinfo("Éxito", f"El gerente con N_cuenta {id_gerente} se eliminó correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo eliminar el gerente")
        self.admin_gerentes()

    def crear_menu_clientes(self):
        self.limpiar_ventana()
        
        frame_clientes = tk.Frame(self, bg="#404B69", width=600, height=400)
        frame_clientes.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(frame_clientes, text="...:: MENÚ CLIENTES ::...", font=("Arial", 32, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=40)
        
        ttk.Button(frame_clientes, text="CUENTA DE DÉBITO", command=self.menu_debito, style="TButton").pack(pady=20, ipadx=50, ipady=10)
        ttk.Button(frame_clientes, text="CUENTA DE CRÉDITO", command=self.menu_credito, style="TButton").pack(pady=20, ipadx=50, ipady=10)
        ttk.Button(frame_clientes, text="SALIR", command=self.crear_menu_principal, style="TButton").pack(pady=20, ipadx=50, ipady=10)

    
    def menu_debito(self):
        self.limpiar_ventana()
        frame_debito = tk.Frame(self, bg="#404B69")
        frame_debito.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(frame_debito, text="..:: CUENTA DÉBITO ::..", font=("Arial", 24, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        ttk.Button(frame_debito, text="Consultar saldo", command=self.consultar_saldo_debito).pack(pady=10)
        ttk.Button(frame_debito, text="Depositar", command=self.depositar).pack(pady=10)
        ttk.Button(frame_debito, text="Retirar", command=self.retirar_debito).pack(pady=10)
        ttk.Button(frame_debito, text="Transferir", command=self.transferir).pack(pady=10)
        ttk.Button(frame_debito, text="Estados de cuenta", command=self.estados_cuenta_debito).pack(pady=10)
        ttk.Button(frame_debito, text="Regresar", command=self.crear_menu_clientes).pack(pady=10)

    def consultar_saldo_debito(self):
        self.limpiar_ventana()
        frame_saldo = tk.Frame(self, bg="#404B69")
        frame_saldo.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_saldo, text="...:: CONSULTAR SALDO ::...", font=("Arial", 36, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=40)
        consulta = Cuenta_Debito.consultar_saldo(self.numero_cuenta)
        
        tk.Label(frame_saldo, text=f"Saldo actual: ${consulta[0]}", font=("Arial", 30), bg="#404B69", fg="#DBEDF3").pack(pady=30)
        ttk.Button(frame_saldo, text="Regresar", command=self.menu_debito).pack(pady=40)

    def depositar(self):
        self.limpiar_ventana()
        frame_deposito = tk.Frame(self, bg="#404B69")
        frame_deposito.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_deposito, text="..:: DEPOSITAR ::..", font=("Arial", 38, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        tk.Label(frame_deposito, text="Cantidad a depositar:", font=("Arial", 30), bg="#404B69", fg="#DBEDF3").pack(pady=10)
        self.entrada_deposito = tk.Entry(frame_deposito, font=("Arial", 30), width=20)
        self.entrada_deposito.pack(pady=10)
        ttk.Button(frame_deposito, text="Depositar", command=self.realizar_deposito).pack(pady=20)
        ttk.Button(frame_deposito, text="Regresar", command=self.menu_debito).pack(pady=10)

    def realizar_deposito(self):
        deposito = float(self.entrada_deposito.get())
        id_movimiento_debito = "DEP" + datetime.now().strftime("%Y%m%d%H%M%S")
        n_movimiento = datetime.now().strftime("%Y%m%d%H%M%S")
        fecha = datetime.now().strftime("%Y-%m-%d")
        tipo = "deposito"
        descripcion = "Deposito realizado"
        id_debito = self.numero_cuenta

        consulta = Cuenta_Debito.consultar_saldo(self.numero_cuenta)
        nuevo_saldo = consulta[0] + deposito
        resultado = Cuenta_Debito.depositar(self.numero_cuenta, nuevo_saldo)
        if resultado:
            registro = Movimiento_debito(id_movimiento_debito, n_movimiento, fecha, tipo, deposito, descripcion, nuevo_saldo, id_debito)
            registro.agregarMovimiento()
            messagebox.showinfo("Éxito", f"Depósito realizado. Nuevo saldo: {nuevo_saldo}")
        else:
            messagebox.showerror("Error", "No se pudo realizar el depósito")
        self.menu_debito()

    def retirar_debito(self):
        self.limpiar_ventana()
        frame_retiro = tk.Frame(self, bg="#404B69")
        frame_retiro.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_retiro, text="..:: RETIRAR ::..", font=("Arial", 24, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        tk.Label(frame_retiro, text="Cantidad a retirar:", font=("Arial", 18), bg="#404B69", fg="#DBEDF3").pack(pady=10)
        self.entrada_retiro = tk.Entry(frame_retiro, font=("Arial", 18), width=20)
        self.entrada_retiro.pack(pady=10)
        ttk.Button(frame_retiro, text="Retirar", command=self.realizar_retiro).pack(pady=20)
        ttk.Button(frame_retiro, text="Regresar", command=self.menu_debito).pack(pady=10)

    def realizar_retiro(self):
        retiro = float(self.entrada_retiro.get())
        id_movimiento_debito = "RET" + datetime.now().strftime("%Y%m%d%H%M%S")
        n_movimiento = datetime.now().strftime("%Y%m%d%H%M%S")
        fecha = datetime.now().strftime("%Y-%m-%d")
        tipo = "retiro"
        descripcion = "Retiro realizado"
        id_debito = self.numero_cuenta

        consulta = Cuenta_Debito.consultar_saldo(self.numero_cuenta)
        nuevo_saldo = consulta[0] - retiro
        if nuevo_saldo >= 0:
            resultado = Cuenta_Debito.retirar(self.numero_cuenta, nuevo_saldo)
            if resultado:
                registro = Movimiento_debito(id_movimiento_debito, n_movimiento, fecha, tipo, retiro, descripcion, nuevo_saldo, id_debito)
                registro.agregarMovimiento()
                messagebox.showinfo("Éxito", f"Retiro realizado. Nuevo saldo: {nuevo_saldo}")
            else:
                messagebox.showerror("Error", "No se pudo realizar el retiro")
        else:
            messagebox.showerror("Error", "Saldo insuficiente")
        self.menu_debito()

    def transferir(self):
        self.limpiar_ventana()
        frame_transferir = tk.Frame(self, bg="#404B69")
        frame_transferir.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_transferir, text="::: TRANSFERIR :::", font=("Arial", 28, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=30)
        
        tk.Label(frame_transferir, text="Número de cuenta destino:", font=("Arial", 20), bg="#404B69", fg="#DBEDF3").pack(pady=15)
        self.entrada_destino = tk.Entry(frame_transferir, font=("Arial", 20), width=35, relief="solid", bd=2)
        self.entrada_destino.pack(pady=15)
        
        tk.Label(frame_transferir, text="Monto a transferir:", font=("Arial", 20), bg="#404B69", fg="#DBEDF3").pack(pady=15)
        self.entrada_transferir = tk.Entry(frame_transferir, font=("Arial", 20), width=35, relief="solid", bd=2)
        self.entrada_transferir.pack(pady=15)
        
        ttk.Button(frame_transferir, text="Transferir", command=self.realizar_transferencia).pack(pady=25)
        ttk.Button(frame_transferir, text="Regresar", command=self.menu_debito).pack(pady=15)



    def realizar_transferencia(self):
        cuenta_destino = self.entrada_destino.get()
        monto = float(self.entrada_transferir.get())
        id_movimiento_debito = "TRA" + datetime.now().strftime("%Y%m%d%H%M%S")
        n_movimiento = datetime.now().strftime("%Y%m%d%H%M%S")
        fecha = datetime.now().strftime("%Y-%m-%d")
        tipo = "transferencia"
        descripcion = "Transferencia realizada"
        id_debito = self.numero_cuenta

        saldo_origen = Cuenta_Debito.consultar_saldo(self.numero_cuenta)
        saldo_destino = Cuenta_Debito.consultar_saldo(cuenta_destino)

        nuevo_saldo_origen = saldo_origen[0] - monto
        nuevo_saldo_destino = saldo_destino[0] + monto

        if nuevo_saldo_origen >= 0:
            resultado = Cuenta_Debito.transferir(self.numero_cuenta, nuevo_saldo_origen, cuenta_destino, nuevo_saldo_destino)
            if resultado:
                registro_origen = Movimiento_debito(id_movimiento_debito, n_movimiento, fecha, tipo, monto, descripcion, nuevo_saldo_origen, id_debito)
                registro_destino = Movimiento_debito(id_movimiento_debito, n_movimiento, fecha, tipo, monto, descripcion, nuevo_saldo_destino, cuenta_destino)
                registro_origen.agregarMovimiento()
                registro_destino.agregarMovimiento()
                messagebox.showinfo("Éxito", f"Transferencia realizada. Nuevo saldo: {nuevo_saldo_origen}")
            else:
                messagebox.showerror("Error", "No se pudo realizar la transferencia")
        else:
            messagebox.showerror("Error", "Saldo insuficiente")
        self.menu_debito()

    def estados_cuenta_debito(self):
        self.limpiar_ventana()
        frame_estado = tk.Frame(self, bg="#404B69", width=1200, height=500)
        frame_estado.place(relx=0.5, rely=0.45, anchor="center")

        tk.Label(frame_estado, text="...:: ESTADOS DE CUENTA DÉBITO ::...", 
                font=("Arial", 26, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)

        movimientos = Movimiento_debito.mostrarMovimientos(self.id_debito)

        if len(movimientos) > 0:
            frame_movimientos = tk.Frame(frame_estado, bg="#404B69")
            frame_movimientos.pack(padx=20, pady=20)

            headers = ["N° Movimiento", "Fecha", "Tipo", "Monto", "Descripción", "Saldo Final"]
            for col, header in enumerate(headers):
                tk.Label(frame_movimientos, text=header, font=("Arial", 24, "bold"),
                        bg="#404B69", fg="#DBEDF3", width=18).grid(row=0, column=col, padx=10, pady=5)

            for index, movimiento in enumerate(movimientos, start=1):
                tk.Label(frame_movimientos, text=str(movimiento[1]), font=("Arial", 24),
                        bg="#404B69", fg="#DBEDF3", width=18).grid(row=index, column=0, padx=10, pady=5)
                tk.Label(frame_movimientos, text=str(movimiento[2]), font=("Arial", 24),
                        bg="#404B69", fg="#DBEDF3", width=18).grid(row=index, column=1, padx=10, pady=5)
                tk.Label(frame_movimientos, text=str(movimiento[3]), font=("Arial", 24),
                        bg="#404B69", fg="#DBEDF3", width=18).grid(row=index, column=2, padx=10, pady=5)
                tk.Label(frame_movimientos, text=str(movimiento[4]), font=("Arial", 24),
                        bg="#404B69", fg="#DBEDF3", width=18).grid(row=index, column=3, padx=10, pady=5)
                tk.Label(frame_movimientos, text=str(movimiento[5]), font=("Arial", 24),
                        bg="#404B69", fg="#DBEDF3", width=18).grid(row=index, column=4, padx=10, pady=5)
                tk.Label(frame_movimientos, text=str(movimiento[6]), font=("Arial", 24),
                        bg="#404B69", fg="#DBEDF3", width=18).grid(row=index, column=5, padx=10, pady=5)
        else:
            tk.Label(frame_estado, text="No hay movimientos todavía", font=("Arial", 24), 
                    bg="#404B69", fg="#DBEDF3").pack(pady=10)

        ttk.Button(frame_estado, text="Regresar", command=self.menu_debito).pack(pady=20)


    def menu_credito(self):
        self.limpiar_ventana()
        frame_credito = tk.Frame(self, bg="#404B69")
        frame_credito.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(frame_credito, text="..:: CUENTA DE CRÉDITO ::..", font=("Arial", 24, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        ttk.Button(frame_credito, text="Consultar saldo", command=self.consultar_saldo_credito).pack(pady=10)
        ttk.Button(frame_credito, text="Pagar tarjeta", command=self.pagar_tarjeta).pack(pady=10)
        ttk.Button(frame_credito, text="Retirar", command=self.retirar_credito).pack(pady=10)
        ttk.Button(frame_credito, text="Estados de cuenta", command=self.estados_cuenta_credito).pack(pady=10)
        ttk.Button(frame_credito, text="Regresar", command=self.crear_menu_clientes).pack(pady=10)

    def consultar_saldo_credito(self):
        self.limpiar_ventana()
        frame_saldo = tk.Frame(self, bg="#404B69")
        frame_saldo.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(frame_saldo, text="..:: CONSULTAR SALDO DE CRÉDITO ::..", font=("Arial", 36, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        consulta = Cuenta_Credito.consultar_saldo(self.numero_cuenta)
        for i in consulta:
            tk.Label(frame_saldo, text=f"Saldo disponible: {i[1] - i[2]}", font=("Arial", 36), bg="#404B69", fg="#DBEDF3").pack()
            tk.Label(frame_saldo, text=f"Saldo pendiente: {i[2]}", font=("Arial", 36), bg="#404B69", fg="#DBEDF3").pack()
        ttk.Button(frame_saldo, text="Regresar", command=self.menu_credito).pack(pady=10)

    def pagar_tarjeta(self):
        self.limpiar_ventana()
        frame_pago = tk.Frame(self, bg="#404B69")
        frame_pago.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_pago, text="..:: PAGAR TARJETA DE CRÉDITO ::..", font=("Arial", 24, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        tk.Label(frame_pago, text="Cantidad a pagar:", font=("Arial", 18), bg="#404B69", fg="#DBEDF3").pack(pady=10)
        self.entrada_pago = tk.Entry(frame_pago, font=("Arial", 18), width=20)
        self.entrada_pago.pack(pady=10)
        ttk.Button(frame_pago, text="Pagar", command=self.realizar_pago).pack(pady=20)
        ttk.Button(frame_pago, text="Regresar", command=self.menu_credito).pack(pady=10)

    def realizar_pago(self):
        pago = float(self.entrada_pago.get())
        id_movimiento_credito = "PAG" + datetime.now().strftime("%Y%m%d%H%M%S")
        n_movimiento = datetime.now().strftime("%Y%m%d%H%M%S")
        fecha = datetime.now().strftime("%Y-%m-%d")
        tipo = "pago tarjeta"
        descripcion = "Pago de tarjeta"
        id_credito = self.numero_cuenta

        consulta = Cuenta_Credito.consultar_saldo(self.numero_cuenta)
        saldo_pendiente = consulta[0][2]
        nuevo_saldo = saldo_pendiente - pago

        resultado = Cuenta_Credito.pagarTarjeta(self.numero_cuenta, nuevo_saldo)
        if resultado:
            registro = Movimiento_credito(id_movimiento_credito, n_movimiento, fecha, tipo, pago, descripcion, nuevo_saldo, id_credito)
            registro.agregarMovimiento()
            messagebox.showinfo("Éxito", "Pago realizado con éxito")
        else:
            messagebox.showerror("Error", "No se pudo realizar el pago")
        self.menu_credito()

    def retirar_credito(self):
        self.limpiar_ventana()
        frame_retiro = tk.Frame(self, bg="#404B69")
        frame_retiro.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_retiro, text="..:: RETIRAR DE CUENTA DE CRÉDITO ::..", font=("Arial", 24, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)
        tk.Label(frame_retiro, text="Cantidad a retirar:", font=("Arial", 18), bg="#404B69", fg="#DBEDF3").pack(pady=10)
        self.entrada_retiro_credito = tk.Entry(frame_retiro, font=("Arial", 18), width=20)
        self.entrada_retiro_credito.pack(pady=10)
        ttk.Button(frame_retiro, text="Retirar", command=self.realizar_retiro_credito).pack(pady=20)
        ttk.Button(frame_retiro, text="Regresar", command=self.menu_credito).pack(pady=10)

    def realizar_retiro_credito(self):
        retiro = float(self.entrada_retiro_credito.get())
        id_movimiento_credito = "RET" + datetime.now().strftime("%Y%m%d%H%M%S")
        n_movimiento = datetime.now().strftime("%Y%m%d%H%M%S")
        fecha = datetime.now().strftime("%Y-%m-%d")
        tipo = "retiro crédito"
        descripcion = "Retiro de crédito"
        id_credito = self.numero_cuenta

        consulta = Cuenta_Credito.consultar_saldo(self.numero_cuenta)
        saldo_pendiente = consulta[0][2]
        nuevo_saldo = saldo_pendiente + retiro

        resultado = Cuenta_Credito.retirar(self.numero_cuenta, nuevo_saldo)
        if resultado:
            registro = Movimiento_credito(id_movimiento_credito, n_movimiento, fecha, tipo, retiro, descripcion, nuevo_saldo, id_credito)
            registro.agregarMovimiento()
            messagebox.showinfo("Éxito", "Retiro realizado con éxito")
        else:
            messagebox.showerror("Error", "No se pudo realizar el retiro")
        self.menu_credito()

    def estados_cuenta_credito(self):
    
        self.limpiar_ventana()
        # Ampliar el tamaño del frame para que ocupe más espacio
        frame_estado = tk.Frame(self, bg="#404B69", width=1200, height=500)
        frame_estado.place(relx=0.5, rely=0.45, anchor="center")

        tk.Label(frame_estado, text="...:: ESTADOS DE CUENTA CRÉDITO ::...", 
                font=("Arial", 26, "bold"), bg="#404B69", fg="#DBEDF3").pack(pady=20)

        movimientos = Movimiento_credito.mostrarMovimientos(self.id_credito)
        
        if len(movimientos) > 0:
            frame_movimientos = tk.Frame(frame_estado, bg="#404B69")
            frame_movimientos.pack(padx=20, pady=20)

            headers = ["N° Movimiento", "Fecha", "Tipo", "Monto", "Descripción", "Saldo Final"]
            for col, header in enumerate(headers):
                tk.Label(frame_movimientos, text=header, font=("Arial", 24, "bold"), 
                        bg="#404B69", fg="#DBEDF3", width=18).grid(row=0, column=col, padx=10, pady=5)

            for index, movimiento in enumerate(movimientos, start=1):
                tk.Label(frame_movimientos, text=str(movimiento[1]), font=("Arial", 24), 
                        bg="#404B69", fg="#DBEDF3", width=18).grid(row=index, column=0, padx=10, pady=5)
                tk.Label(frame_movimientos, text=str(movimiento[2]), font=("Arial", 24), 
                        bg="#404B69", fg="#DBEDF3", width=18).grid(row=index, column=1, padx=10, pady=5)
                tk.Label(frame_movimientos, text=str(movimiento[3]), font=("Arial", 24), 
                        bg="#404B69", fg="#DBEDF3", width=18).grid(row=index, column=2, padx=10, pady=5)
                tk.Label(frame_movimientos, text=str(movimiento[4]), font=("Arial", 24), 
                        bg="#404B69", fg="#DBEDF3", width=18).grid(row=index, column=3, padx=10, pady=5)
                tk.Label(frame_movimientos, text=str(movimiento[5]), font=("Arial", 24), 
                        bg="#404B69", fg="#DBEDF3", width=18).grid(row=index, column=4, padx=10, pady=5)
                tk.Label(frame_movimientos, text=str(movimiento[6]), font=("Arial", 24), 
                        bg="#404B69", fg="#DBEDF3", width=18).grid(row=index, column=5, padx=10, pady=5)
        else:
            tk.Label(frame_estado, text="No hay movimientos todavía", font=("Arial", 24), 
                    bg="#404B69", fg="#DBEDF3").pack(pady=10)

        ttk.Button(frame_estado, text="Regresar", command=self.menu_credito).pack(pady=20)




    def limpiar_ventana(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = BanfuturoApp()
    app.mainloop()
