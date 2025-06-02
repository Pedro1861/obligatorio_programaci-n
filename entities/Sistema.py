
from entities.pieza import Pieza
from exceptions.errores import FueraDeRango, YaExiste
from entities.requerimiento import Requerimiento
from entities.maquina import Maquina
from entities.cliente import ClienteParticular, Empresa
from entities.reposicion import Reposicion
###REGISTROS###




class Sistema():
    
    lista_piezas=[]
    lista_maquinas=[]
    lista_pedidos=[]
    lista_clientes=[]
    lista_requerimientos=[]
    lista_empresas=[]
    lista_particulares=[]

    
    ####PIEZA####
    
    def registrar_pieza(self,desc_pieza,costo_pieza,cantidad_pieza,lote_pieza):

        pieza0=Pieza(desc_pieza,costo_pieza,cantidad_pieza,lote_pieza)
        self.lista_piezas.append(pieza0)
    
    @classmethod
    def listar_piezas(cls):
        print("Piezas: ")
        for i in cls.lista_piezas:
            print(f"\n Codigo: {i.codigo}\n Descripcion: {i.desc}\n Costo: {i.costo}\n Cantidad: {i.cantidad}\n Lote: {i.lote}\n")

    ####PIEZAS####
    
    ####MAQUINAS###
    def registrar_maquina(self,descripcion):
        maquina0=Maquina(descripcion)
        self.lista_maquinas.append(maquina0)
        return maquina0
    @classmethod
    def listar_maquinas(cls):
        print("Maquinas: \n")
        for i in cls.lista_maquinas:
            print(f"\nCodigo:{i.codigo}\nDescripcion:{i.desc}\nRequerimientos:")
            for j in i.requerimiento:
                if i==j.maquina:
                    print(f" \nCodigo Pieza:{j.pieza.codigo}\n Cantidad: {j.cantidad}\n")
            print(f"Costo: {i.costo_produccion()}")
        
    ####MAQUINAS####
                




    ####CLIENTE####
    def registrar_cliente(self):
        print("Tipo cliente: \n 1. Cliente Particular \n 2. Empresa")
        while True:
            try:
                tipo=int(input("Seleccione tipo de cliente: "))
                if tipo!=1 or tipo!=2:
                    raise FueraDeRango
                break
            except ValueError:
                print("\nError! Ingrese un valor valido\n")
            except FueraDeRango:
                print("\nError! Ingrese indice dentro del rango\n")
        if tipo==1:
            while True:
                try:
                    cédula= int(input("ingrese la cédula del cliente: "))
                    for particular in self.lista_particulares:
                        if particular.cédula == cédula:
                            raise YaExiste
                    break
                except ValueError:
                    print("\nError! Ingrese un valor valido\n")
                except YaExiste:
                    print("\nEsa cedula ya existe, ingrese una nueva\n")
            for particular in self.lista_particulares:
                if particular.cédula == cédula:
                    cédula=int(input("ERROR: la cédula ya está regitrada. \n Ingrese una nueva cédula: "))
                    return
            nombre=input("ingrese nombre completo del cliente: ")
            while True:
                try:
                    teléfono=int(input("ingrese el teléfono del cliente: "))
                    break
                except ValueError:
                    print("\nError! Ingrese un valor valido\n")
            correo_electrónico= input("ingrese el correo electrónico del cliente: ")
            cliente=ClienteParticular(self.ID_cliente,cédula,nombre,teléfono,correo_electrónico)
            self.lista_clientes.append(cliente)
            self.lista_particulares.append(cliente)
        elif tipo==2:
            while True:
                try:
                    rut=int(input("Ingrese número de RUT: "))
                    break
                except ValueError:
                    print("\nError! Ingrese un valor valido\n")
            for empresa in self.lista_empresas:
                if empresa.rut == rut:
                    rut=int(input("ERROR: el RUT ya está regitrado. \n Ingrese un nuevo número de RUT: "))
            nombre=input("Ingrese nombre: ")
            página_web=input("Ingrese página web: ")
            while True:
                try:
                    teléfono=int(input("Ingrese teléfono de contacto: "))
                    break
                except ValueError:
                    print("\nError! Ingrese un valor valido\n")
            correo_electrónico= input("ingrese el correo electrónico del cliente: ")
            cliente=Empresa(self.ID_cliente,rut,nombre,página_web,teléfono,correo_electrónico)
            self.lista_clientes.append(cliente)
            self.lista_empresas.append(cliente)
        else:
            raise ValueError
        self.ID_cliente+=1

    def listar_clientes(self):
        for i in range (len(self.lista_clientes)):
            print (self.lista_clientesclientes[i])
    ####CLIENTE####

    ####REPOSICION####
    def registrar_reposicion(self,pieza,cantidad_lotes):
        reposicion0=Reposicion(pieza,cantidad_lotes)
        pieza.reposicion.append(reposicion0)
        pieza.cantidad+=cantidad_lotes*pieza.lote
        print(f"Costo de reposicion: {reposicion0.get_costo()}\nCantidad disponible de Pieza({reposicion0.pieza}): {pieza.cantidad }")
    ####REPOSICION####
    def registrar_requerimiento(self,maquina,pieza,cantidad):
        requerimiento=Requerimiento(maquina,pieza,cantidad)
        return requerimiento
    
    ####PEDIDOS####
    def registrar_pedido():
        pass

    def listar_pedido():
        pass
