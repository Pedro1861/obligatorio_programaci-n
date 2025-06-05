
from pieza import Pieza
from entities.errores import FueraDeRango, YaExiste
from entities.requerimiento import Requerimiento
from entities.maquina import Maquina
from entities.cliente import ClienteParticular, Empresa
from entities.reposicion import Reposicion
from entities.pedido import Pedido
import datetime
###REGISTROS###




class Sistema():
    
    lista_piezas=[]
    lista_maquinas=[]
    lista_pedidos=[]
    lista_clientes=[]
    lista_requerimientos=[]
    lista_empresas=[]
    lista_particulares=[]
    lista_pedidos=[]
    lista_pedidos_pendientes=[]

    
    ####PIEZA####
    
    def registrar_pieza(self,codigo,desc_pieza,costo_pieza,cantidad_pieza,lote_pieza):

        pieza0=Pieza(codigo,desc_pieza,costo_pieza,cantidad_pieza,lote_pieza)
        self.lista_piezas.append(pieza0)
    
    @classmethod
    def listar_piezas(cls):
        if cls.lista_piezas==[]:
            print("\nError! No hay Piezas para listar\n")
        print("Piezas: ")
        faltante=0
        for piece in cls.lista_piezas:
            for pedido in cls.lista_pedidos_pendientes:
                for requerimiento in pedido.maquina.requerimiento:
                    if requerimiento.pieza==piece:
                        faltante+=requerimiento.cantidad-piece.cantidad
                        if faltante<0:
                            faltante=0
            print(f"\n Codigo: {piece.codigo}\n Descripcion: {piece.desc}\n Costo: {piece.costo}\n Cantidad: {piece.cantidad}\n Lote: {piece.lote}")
            if faltante!=0:
                print(f"Cantidad faltante:{faltante}\nLotes recomendados reponer:{round(faltante/piece.lote)}")
    ####PIEZAS####
    
    ####MAQUINAS###
    def registrar_maquina(self,descripcion):
        maquina0=Maquina(descripcion)
        self.lista_maquinas.append(maquina0)
        return maquina0
    
    def listar_maquinas(self):
        if self.lista_maquinas==[]:
            print("\nError! No hay Maquinas para listar\n")
            pass
        print("Maquinas: \n")
        for i in self.lista_maquinas:
            print(f"\nCodigo:{i.codigo}\n\nDescripcion:{i.desc}\n\nRequerimientos:")
            for j in i.requerimiento:
                print(f" Codigo Pieza:{j.pieza.codigo}\n Cantidad Pieza: {j.cantidad}\n")
            print(f"Costo: {i.costo_produccion()}\n")
            print("---------------------------")
        
    ####MAQUINAS####
                




    ####CLIENTE####
    def registrar_cliente_Particular(self,cédula,nombre,teléfono,correo_electrónico):
        cliente=ClienteParticular(cédula,nombre,teléfono,correo_electrónico)
        self.lista_clientes.append(cliente)
        self.lista_particulares.append(cliente)

    def registrar_cliente_Empresa(self,rut,nombre,pagina_web,teléfono,correo_electrónico):
        cliente=Empresa(rut,nombre,teléfono,correo_electrónico,pagina_web)
        self.lista_clientes.append(cliente)
        self.lista_empresas.append(cliente)

    def listar_clientes(self):
        n=0
        for cliente in self.lista_clientes:
            n+=1
            if cliente in self.lista_particulares:
                print (f"{n}. Cliente: {cliente.nombre}, ID: {cliente.ID_cliente}, Tipo: particular, Cédula: {cliente.cédula}, Teléfono: {cliente.telefono}, Correo: {cliente.correo_electrónico}")
            elif cliente in self.lista_empresas:
                print (f"{n}. Cliente: {cliente.nombre}, ID: {cliente.ID_cliente}, Tipo: empresa, RUT: {cliente.rut}, Página web: {cliente.página_web}, Teléfono: {cliente.telefono}, Correo: {cliente.correo_electrónico}")

    ####CLIENTE####

    ####REPOSICION####
    def registrar_reposicion():
        pass
    ####REPOSICION####
    def registrar_requerimiento(self,maquina,pieza,cantidad):
        requerimiento=Requerimiento(maquina,pieza,cantidad)
        return requerimiento
    
    ####PEDIDOS####
    def registrar_pedido(self,cliente_pedido,maquina_pedido):
        num_estado=0
        for pieza_pedido in maquina_pedido.requerimientos:
            for pieza in self.lista_piezas:
                if pieza.codigo_pieza==pieza_pedido.codigo_pieza and pieza.cantidad<pieza_pedido.cantidad:
                    num_estado+=1
        if num_estado>0:
            estado="pendiente"
            fecha_entregado=None
        else:
            estado="entregado"
            fecha_entregado=datetime.now()
        if cliente_pedido in self.lista_particulares:
            precio=(maquina_pedido.costo)*1.50
        elif cliente_pedido in self.lista_empresas:
            precio=((maquina_pedido.costo)*1.50)*0.80
        fecha_recibido=datetime.now()
        nuevo_pedido = Pedido(cliente_pedido, maquina_pedido, fecha_recibido, fecha_entregado, estado, precio)
        if nuevo_pedido.estado=="pendiente":
            self.lista_pedidos_pendientes.append(nuevo_pedido)
            print("Pedido registrado. Estado: PENDIENTE")
        elif nuevo_pedido.estado=="entregado":
            for navegar_requerimientos in nuevo_pedido.maquina.requerimientos:
                for navegar_pieza in self.lista_piezas:
                    if navegar_requerimientos.codigo_pieza==navegar_pieza.codigo_pieza:
                        navegar_pieza.cantidad-=navegar_requerimientos.cantidad
        self.lista_pedidos.append(nuevo_pedido)
        print(f"Pedido registrado con éxito: {nuevo_pedido}")

    def completar_pedido(self):
        for pedido_pendiente in self.lista_pedidos_pendientes:
            num_estado=0
            for pieza_registrada in pedido_pendiente.maquina.requerimientos:
                if pieza_registrada.pieza.cantidad<pieza_registrada.cantidad:
                    num_estado+=1
            if num_estado>0:
                estado="pendiente"
                fecha_entregado=None
                pedido_pendiente.estado="pendiente"
            else:
                pedido_pendiente.fecha_entregado=datetime.now()
                pedido_pendiente.estado="entregado"
                for navegar_requerimientos in pedido_pendiente.maquina.requerimientos:
                    for navegar_pieza in self.lista_piezas:
                        if navegar_requerimientos.pieza==navegar_pieza:
                            navegar_pieza.cantidad-=navegar_requerimientos.cantidad

            if pedido_pendiente.estado == "entregado":
                self.lista_pedidos_pendientes.remove(pedido_pendiente)
                print(f"Pedido {pedido_pendiente} completado y eliminado de la lista de pendientes.")

    def listar_pedidos(self):
        n=0
        for pedido in self.lista_pedidos:
                n+=1
                print(f"{n}. Pedido. Cliente: {pedido.cliente.nombre}, Maquina: {pedido.maquina.descripcion}, Fecha Recibido: {pedido.fecha_recibido}, Fecha Entregado: {pedido.fecha_entregado}, Estado: {pedido.estado}, Precio: {pedido.precio}")
    def listar_pedidos_filtrados(self, opcion_estado):
        n=0
        if opcion_estado ==1:
            for pedido in self.lista_pedidos_pendientes:
                n+=1
                print(f"{n}. Pedido. Cliente: {pedido.cliente.nombre}, Maquina: {pedido.maquina.descripcion}, Fecha Recibido: {pedido.fecha_recibido}, Estado: {pedido.estado}, Precio: {pedido.precio}")
        elif opcion_estado ==2:
            n=0
            for pedido in self.lista_pedidos:
                if pedido.estado=="entregado":
                    n+=1
                    print(f"{n}. Pedido. Cliente: {pedido.cliente.nombre}, Maquina: {pedido.maquina.descripcion}, Fecha Recibido: {pedido.fecha_recibido}, Fecha Entregado: {pedido.fecha_entregado}, Estado: {pedido.estado}, Precio: {pedido.precio}")
