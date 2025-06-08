
from entities.pieza import Pieza
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
    
    def registrar_pieza(self,desc_pieza,costo_pieza,cantidad_pieza,lote_pieza):

        pieza0=Pieza(desc_pieza,costo_pieza,cantidad_pieza,lote_pieza)
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
                print (f"{n}. Cliente: {cliente.nombre}, ID: {cliente.id}, Tipo: particular, Cédula: {cliente.cédula}, Teléfono: {cliente.telefono}, Correo: {cliente.correo_electrónico}")
            elif cliente in self.lista_empresas:
                print (f"{n}. Cliente: {cliente.nombre}, ID: {cliente.id}, Tipo: empresa, RUT: {cliente.rut}, Página web: {cliente.página_web}, Teléfono: {cliente.telefono}, Correo: {cliente.correo_electrónico}")

    ####CLIENTE####

    ####REPOSICION####
    def registrar_reposicion(self,pieza,cantidad):
        nueva_reposicion=Reposicion(pieza,cantidad)
        pieza.reposicion.append(nueva_reposicion)
        for pieza_navegar in self.lista_piezas:
            if pieza_navegar.codigo==pieza.codigo:
                pieza_navegar.cantidad+=cantidad
                print(f"Reposición registrada. Pieza: {pieza_navegar.desc}, Cantidad: {cantidad}")

        
    ####REPOSICION####
    def registrar_requerimiento(self,maquina,pieza,cantidad):
        requerimiento=Requerimiento(maquina,pieza,cantidad)
        return requerimiento
    
    ####PEDIDOS####
    def registrar_pedido(self,cliente_pedido,maquina_pedido):
        if maquina_pedido.disponibilidad()==False:
            estado="pendiente"
            fecha_entregado=None
        elif maquina_pedido.disponibilidad()==True:
            estado="entregado"
            fecha_entregado=datetime.now()
        fecha_recibido=datetime.now()
        nuevo_pedido = Pedido(cliente_pedido, maquina_pedido, fecha_recibido, fecha_entregado, estado)
        if nuevo_pedido.estado=="pendiente":
            self.lista_pedidos_pendientes.append(nuevo_pedido)
            print("Pedido registrado. Estado: PENDIENTE")
        elif nuevo_pedido.estado=="entregado":
            for navegar_requerimientos in nuevo_pedido.maquina.requerimiento:
                for navegar_pieza in self.lista_piezas:
                    if navegar_requerimientos.pieza.codigo==navegar_pieza.codigo:
                        navegar_pieza.cantidad-=navegar_requerimientos.cantidad
            print("Pedido registrado. Estado: ENTREGADO ")
        self.lista_pedidos.append(nuevo_pedido)
        print(f"Pedido registrado con éxito!")

    def completar_pedido(self):
        for pedido_pendiente in self.lista_pedidos_pendientes:
            if pedido_pendiente.maquina.disponibilidad()==True:
                pedido_pendiente.fecha_entregado=datetime.now()
                pedido_pendiente.estado="entregado"
                for navegar_requerimientos in pedido_pendiente.maquina.requerimiento:
                    for navegar_pieza in self.lista_piezas:
                        if navegar_requerimientos.pieza==navegar_pieza:
                            navegar_pieza.cantidad-=navegar_requerimientos.cantidad
                self.lista_pedidos_pendientes.remove(pedido_pendiente)
                print(f"Pedido de la maquina {pedido_pendiente.maquina.desc} recibido en la fecha {pedido_pendiente.fecha_recibido} ha sido completado y eliminado de la lista de pendientes.")

    def listar_pedidos(self):
        n=0
        for pedido in self.lista_pedidos:
                n+=1
                print(f"{n}. Pedido. Cliente: {pedido.cliente.nombre}, Maquina: {pedido.maquina.desc}, Fecha Recibido: {pedido.fecha_recibido}, Fecha Entregado: {pedido.fecha_entregado}, Estado: {pedido.estado}, Precio: {pedido.get_precio()}")
    def listar_pedidos_filtrados(self, opcion_estado):
        n=0
        if opcion_estado ==1:
            for pedido in self.lista_pedidos_pendientes:
                n+=1
                print(f"{n}. Pedido. Cliente: {pedido.cliente.nombre}, Maquina: {pedido.maquina.desc}, Fecha Recibido: {pedido.fecha_recibido}, Estado: {pedido.estado}, Precio: {pedido.get_precio()}")
        elif opcion_estado ==2:
            n=0
            for pedido in self.lista_pedidos:
                if pedido.estado=="entregado":
                    n+=1
                    print(f"{n}. Pedido. Cliente: {pedido.cliente.nombre}, Maquina: {pedido.maquina.desc}, Fecha Recibido: {pedido.fecha_recibido}, Fecha Entregado: {pedido.fecha_entregado}, Estado: {pedido.estado}, Precio: {pedido.get_precio()}")
    def contabilidad(self):
        costo_total=0
        ingreso_total=0
        for pedido in self.lista_pedidos:
            if pedido.estado=="entregado":
                costo_total+=pedido.maquina.costo_produccion()
                ingreso_total+=pedido.get_precio()
        ganancia_total=ingreso_total-costo_total
        print(f"1. Costo total de producción: {costo_total} USD \n 2. Ingreso total de ventas: {ingreso_total} USD \n 3. Ganancia total: {ganancia_total}USD \n 4. Impuesto a la ganancia: {ganancia_total*0.25}USD \n 5. Ganancia total tras impuestos: {ganancia_total*0.75}USD")


