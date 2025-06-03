
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

    
    ####PIEZA####
    
    def registrar_pieza(self,desc_pieza,costo_pieza,cantidad_pieza,lote_pieza):

        pieza0=Pieza(desc_pieza,costo_pieza,cantidad_pieza,lote_pieza)
        self.lista_piezas.append(pieza0)
    
    @classmethod
    def listar_piezas(cls):
        print("Piezas: ")
        faltante=0
        for piece in cls.lista_piezas:
            for pedido in cls.lista_pedidos_pendientes:
                for requerimiento in pedido.maquina.requerimiento:
                    if requerimiento.pieza==piece:
                        faltante=requerimiento.cantidad-piece.cantidad
                        if faltante<0:
                            faltante=0
            print(f"\n Codigo: {piece.codigo}\n Descripcion: {piece.desc}\n Costo: {piece.costo}\n Cantidad: {piece.cantidad}\n Lote: {piece.lote}\nCantidad faltante:{faltante}\nCantidad recomendada a reponer:{round(faltante/piece.lote)}")

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
    lista_pedidos=[]
    lista_pedidos_pendientes=[]
    def registrar_pedido(self):
        print("seleccione el cliente que desea registrar un pedido: ")
        for i in range(len(self.lista_clientes)):
            print(f"{i+1}. {self.lista_clientes[i].nombre}")
        seleccion_cliente = int(input("Ingrese el número del cliente: ")) - 1

        print("seleccione la máquina que desea registrar un pedido: ")
        for i in range(len(self.lista_maquinas)):
            print(f"{i+1}. {self.lista_maquinas[i].desc}")
        seleccion_maquina = int(input("Ingrese el número de maquina: ")) - 1
        num_estado=0
        for pieza_pedido in self.lista_maquinas[seleccion_maquina].requerimientos:
            for pieza in self.lista_piezas:
                if pieza.codigo_pieza==pieza_pedido.codigo_pieza and pieza.cantidad<pieza_pedido.cantidad:
                    num_estado+=1
        if num_estado>0:
            estado="pendiente"
            fecha_entregado=None
        else:
            estado="entregado"
            fecha_entregado=datetime.now()
        
        cliente_pedido= self.lista_clientes[seleccion_cliente]
        if cliente_pedido in self.lista_particulares:
            precio=(self.lista_maquinas[seleccion_maquina].costo)*1.50
        elif cliente_pedido in self.lista_empresas:
            precio=((self.lista_maquinas[seleccion_maquina].costo)*1.50)*0.80
        fecha_recibido=datetime.now()
        nuevo_pedido = Pedido(self.lista_clientes[seleccion_cliente], self.lista_maquinas[seleccion_maquina], fecha_recibido, fecha_entregado, estado, precio)
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
                for pieza in self.lista_piezas:
                    if pieza.codigo_pieza==pieza_registrada.pieza.codigo_pieza and pieza.cantidad<pieza_registrada.cantidad:
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
        print("LISTAR PEDIDOS \n ¿Desea filtrar por estado? \n 1. Si \n 2. No")
        filtrar = int(input("Ingrese su opción: "))
        if filtrar == 1:
            opcion_estado=int(input("Seleccione el estado del pedido: \n 1. Pendiente \n 2. Entregado"))
            n=0
            if opcion_estado ==1:
                for pedido in self.lista_pedidos_pendientes:
                    n+=1
                    print(f"{n}. Pedido. Cliente: {pedido.cliente.nombre}, Maquina: {pedido.maquina.descripcion}, Fecha Recibido: {pedido.fecha_recibido}, Estado: {pedido.estado}, Precio: {pedido.precio}")
            elif opcion_estado ==2:
                for pedido in self.lista_pedidos:
                    if pedido.estado=="entregado":
                        n+=1
                        print(f"{n}. Pedido. Cliente: {pedido.cliente.nombre}, Maquina: {pedido.maquina.descripcion}, Fecha Recibido: {pedido.fecha_recibido}, Fecha Entregado: {pedido.fecha_entregado}, Estado: {pedido.estado}, Precio: {pedido.precio}")
        elif filtrar == 2:
            for pedido in self.lista_pedidos:
                n+=1
                print(f"{n}. Pedido. Cliente: {pedido.cliente.nombre}, Maquina: {pedido.maquina.descripcion}, Fecha Recibido: {pedido.fecha_recibido}, Fecha Entregado: {pedido.fecha_entregado}, Estado: {pedido.estado}, Precio: {pedido.precio}")


    def listar_contabilidad(self):
        costo_total=0
        ingreso_total=0
        for pedido in self.lista_pedidos and pedido not in self.lista_pedidos_pendientes:
            costo_total+=pedido.maquina.costo_produccion()
            ingreso_total+=pedido.precio
            ganancia_total=ingreso_total-costo_total
        print(f"1. Costo total de producción: {costo_total} USD \n 2. Ingreso total de ventas: {ingreso_total} USD \n 3. Ganancia total: {ingreso_total-costo_total} \n 4. Impuesto a la ganancia: {ganancia_total*0.25} \n 5. Ganancia total tras impuestos: {ganancia_total*0.75}")

