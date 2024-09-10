#Importaciones de la clase
from bloque_bit import Bloque
from transaccion import Transaccion

#clase blockchain
class BlockChain:
    def __init__(self, numero_bloques):
        self.numero_bloques = numero_bloques
        self.bloques = []
        
    #creando la block_chain
    def concatenar_bloque(self, actual, siguiente):
        hash = 0
        bloque_actual = Bloque(hash)
        bloque_actual = actual
        bloque_siguiente = Bloque(hash)
        bloque_siguiente = siguiente
        bloque_siguiente.concatenar(bloque_actual.retornar_hash())
        self.bloques.append(bloque_actual,bloque_siguiente)
        
#Creando algunas transacciones iniciales
weimar = ["Weimar",100]
manuel = ["Manuel",100]
andres = ["Andres",100]
t0 = Transaccion()
t0.adicionar_entrada(["Weimar",100])
t0.adicionar_salida(["Weimar",100])
t1 = Transaccion()
t1.adicionar_entrada(["Manuel",100])
t1.adicionar_salida(["Manuel",100])
transaccion1 = Transaccion()
transaccion1.adicionar_entrada(weimar)
transaccion1.adicionar_salida(["Pedro",20])
transaccion1.adicionar_salida(["Weimar",80])
transaccion1.crear_id()
transaccion2 = Transaccion()
transaccion2.adicionar_entrada(manuel)
transaccion2.adicionar_salida(["Andres",50])
transaccion2.adicionar_salida(["Manuel",50])
transaccion2.crear_id()

#Creando el bloque genesis
bloque_genesis = Bloque("hashPrevio001")
bloque_genesis.data_tx.append(t0.retornar_info())
bloque_genesis.transacciones.append(t0)  
bloque_genesis.data_tx.append(t1.retornar_info())
bloque_genesis.transacciones.append(t1)
bloque_genesis.adicionar_transacciones([transaccion1,transaccion2])
bloque_genesis.crear_bloque(2)
print(bloque_genesis.retornar_bloque())

#Creando el segundo bloque
bloque_1 = Bloque(bloque_genesis.retornar_hash())
bloque_1.data_tx.append(t0.retornar_info())
bloque_1.transacciones.append(t0)  
bloque_1.data_tx.append(t1.retornar_info())
bloque_1.transacciones.append(t1)

#creando una transaccion para adicionar al nuevo bloque
transaccion3 = Transaccion()
transaccion3.adicionar_entrada(["Manuel",50])
transaccion3.adicionar_salida(["Pedro",20])
transaccion3.adicionar_salida(["Manuel",30])
transaccion3.crear_id()

#adicionando la transaccion al nuevo bloque
bloque_1.adicionar_transacciones([transaccion1,transaccion2,transaccion3])
bloque_1.crear_bloque(3)

#Creando la blockchain
blockchain = BlockChain(3)
print(bloque_1.retornar_bloque())




