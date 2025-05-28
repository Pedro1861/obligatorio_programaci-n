import random
from Pieza import Pieza
from exceptions.Errores import FueraDeRango
from Requerimiento import Requerimiento
from cliente import ClienteParticular, Empresa

###REGISTROS###

codigos_generados = set()

def generar_codigo(longitud=6):
    while True:
        codigo = ''.join(random.choices('0123456789', k=longitud))
        if codigo not in codigos_generados:
            codigos_generados.add(codigo)
            return codigo




#PIEZA#
lista_piezas=[]
def registrar_pieza(lista_piezas):
    desc_pieza=input("Brinda una descripcion de la pieza: ")
    for i in lista_piezas:
        if i.desc==desc_pieza:
            nueva_desc=int(input("ERROR:La pieza ya existe.\n Si desea poner otra descripcion, ingrese 1\n Si desea abortar la operacion ingrese 2"))
            if nueva_desc!=1 and nueva_desc!=2:
                raise FueraDeRango

            if nueva_desc==1:
                desc_pieza=input("Ingrese una descripcion valida: ")
                if desc_pieza==i.desc:
                    print("ERROR: La descrpcion sigue siendo igual, operacion terminada")
                    break

            elif nueva_desc==2:
                break

    costo_pieza=int(input("Brinda costo por unidad de la pieza: "))
    lote_pieza=int(input("Brinda el tamanio del lote de reposicion: "))
    cantidad_pieza=int(input("Brinda un cantidad inicial de piezas: "))
    pieza0=Pieza(generar_codigo(),desc_pieza,costo_pieza,cantidad_pieza,lote_pieza)
    lista_piezas.append(pieza0)
    


#MAQUINA#
lista_maquinas=[]
def registrar_maquina(lista_maquinas):
    lista_requerimientos=[]
    print("Comenzemos con sus requerimientos...\n")
    print(lista_piezas)
    code=int(input("ingrese el codigo de la pieza requerida: "))
    nuevo_requerimiento=1
    while nuevo_requerimiento==1:
        nueva_pieza=0
        for i in lista_piezas:
            if i.codigo==code:
                nueva_pieza=i
        while nueva_pieza==0:
            print("El codigo no pertenece a ninguna pieza")
            code=int(input("ingrese el codigo de la pieza requerida: "))
            for i in lista_piezas:
                if i.codigo==code:
                    nueva_pieza=i
        cantidad_piezas=int(input("Ingrese la cantidad de piezas necesarias: "))      
        nuevo_requerimiento=int(input("Desea agregar un nuevo requerimiento?\n 1.SI\n 2.NO"))
        if nuevo_requerimiento!=1 and nuevo_requerimiento!=0:
            raise FueraDeRango
            
            
#CLIENTE#
    def __init__(self):
        self.clientes=[]
        self.ID_cliente=1
    def registrar_cliente(self):
        print("Tipo cliente: \n 1. Cliente Particular \n 2. Empresea")
        tipo=int(input("Seleccione tipo de cliente: "))
        if tipo==1:
            cédula= int(input("ingrese la cédula del cliente: "))
            nombre=input("ingrese nombre completo del cliente: ")
            teléfono=int(input("ingrese el teléfono del cliente: "))
            correo_electrónico= input("ingrese el correo electrónico del cliente: ")
            cliente=ClienteParticular(self.ID_cliente,cédula,nombre,teléfono,correo_electrónico)
            self.clientes.append(cliente)
        if tipo==2:
            rut=int(input("Ingrese número de RUT: "))
            nombre=input("Ingrese nombre: ")
            página_web=input("Ingrese página web: ")
            teléfono=input("Ingrese teléfono de contacto: ")
            correo_electrónico= input("ingrese el correo electrónico del cliente: ")
            cliente=Empresa(self.ID_cliente,rut,nombre,página_web,teléfono,correo_electrónico)
            self.clientes.append(cliente)
        else:
            raise ValueError
        self.ID_cliente+=1

        
#REPOSICION#
###LISTADOS###
#CLIENTES#
#PEDIDOS#
#MAQUINAS#
#PIEZAS#
#CONTABILIDAD#
