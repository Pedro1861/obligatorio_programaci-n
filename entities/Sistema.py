
from entities.Pieza import Pieza
from exceptions.Errores import FueraDeRango
from entities.Requerimiento import Requerimiento
from entities.Maquina import Maquina
from entities.Cliente import ClienteParticular, Empresa
from Reposicion import Reposición
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
    
    @classmethod
    def listar_piezas(cls):
        print("Piezas: ")
        for i in cls.lista_piezas:
            print(f"\n Codigo: {i.codigo}\n Descripcion: {i.desc}\n Costo: {i.costo}\n Cantidad: {i.cantidad}\n Lote: {i.lote}\n Reposiciones: {i.reposicion}\n")

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
    def registrar_reposicion(self,pieza,cantidad_lotes):
        reposicion0=Reposición(pieza,cantidad_lotes)
        pieza.reposicion.append(reposicion0)
        pieza.cantidad+=cantidad_lotes*pieza.lote
        print(f"Costo de reposicion: {reposicion0.get_costo()}\nCantidad disponible de Pieza({reposicion0.pieza}): {pieza.cantidad }")
    ####REPOSICION####
    
    
    ####PEDIDOS####
    def registrar_pedido():
        pass

    def listar_pedido():
        pass
