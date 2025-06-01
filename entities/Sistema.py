
from entities.Pieza import Pieza
from exceptions.Errores import FueraDeRango
from entities.Requerimiento import Requerimiento
from entities.Maquina import Maquina
from entities.Cliente import ClienteParticular, Empresa

###REGISTROS###




class Sistema():
    
    lista_piezas=[]
    lista_maquinas=[]
    lista_pedidos=[]
    lista_clientes=[]
    lista_requerimientos=[]

    
    ####PIEZA####
    
    def registrar_pieza(self,codigo,desc_pieza,costo_pieza,cantidad_pieza,lote_pieza):

        pieza0=Pieza(codigo,desc_pieza,costo_pieza,cantidad_pieza,lote_pieza)
        self.lista_piezas.append(pieza0)
    
    def listar_piezas():
        pass
    ####PIEZAS####
    
    ####MAQUINAS###
    def registrar_maquina(self,descripcion):
        maquina0=Maquina(descripcion)
        self.lista_maquinas.append(maquina0)
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
    
    
    ####PEDIDOS####
    def registrar_pedido():
        pass

    def listar_pedido():
        pass
