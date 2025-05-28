
from Pieza import Pieza
from exceptions.Errores import FueraDeRango
from Requerimiento import Requerimiento
from Maquina import Maquina
from Cliente import Persona, Empresa

###REGISTROS###

codigos_generados = 0

def generar_codigo():
    codigo= codigos_generados+1
    codigos_generados=codigo
    return codigo



class Sistema():
    
    lista_piezas=[]
    lista_maquinas=[]
    lista_pedidos=[]
    lista_clientes=[]


    
    ####PIEZA####
    
    def registrar_pieza(self,codigo,desc_pieza,costo_pieza,cantidad_pieza,lote_pieza):

        pieza0=Pieza(codigo,desc_pieza,costo_pieza,cantidad_pieza,lote_pieza)
        self.lista_piezas.append(pieza0)
    
    def listar_piezas():
        pass
    ####PIEZAS####
    
    ####MAQUINAS###
    def registrar_maquina(lista_maquinas,lista_piezas):
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
    def listar_maquinas():
        pass
    ####MAQUINAS####
                




    ####CLIENTE####
    def registrar_cliente():
        pass

    def listar_cliente():
        pass
    ####CLIENTE####

    ####REPOSICION####
    def registrar_reposicion():
        pass
    ####REPOSICION####
    
    
    #PEDIDOS#
    def registrar_pedido():
        pass

    def listar_pedido():
        pass
   
    #CONTABILIDAD#