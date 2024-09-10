#importaciones de la clase
from hashlib import *
from transaccion import Transaccion
import random

#funcion que cacula el hash de un dato
def hash_Sha256(data):
    return sha256(data.encode('utf-8')).hexdigest()

#clase Bloque que tiene como Inputs: Hash previo, las transacciones se van adicionando despues.
class Bloque:  
    def __init__(self, hash_previo):
        self.hash_bloque = ""
        self.hash_previo = hash_previo
        self.nonce = ""
        self.hash_raiz = ""
        self.transacciones = []
        self.data_tx = []
    
    #adicionar transacciones, depende de la aprobacion de las mismas: se validan que las entradas sean UTXO y que dentro de la transaccion sus entradas sean iguales a sus salidas
    def adicionar_transacciones(self, tx):
        for t in tx:
            transaccion = Transaccion()
            transaccion = t
            transaccion.validar_transaccion()
            if(transaccion.valida):
                if self.aprobar_transaccion(transaccion):
                    self.data_tx.append(transaccion.retornar_info())
                    self.transacciones.append(transaccion)
    
    #Aprobacion de transacciones
    def aprobar_transaccion(self, t):
        verificadas,utxo_entradas = 0,0
        transaccion = Transaccion()
        transaccion = t
        for e in transaccion.entradas:
            for tx in self.transacciones:
                transaccion2 = Transaccion
                transaccion2 = tx
                for s in transaccion2.salidas:
                    if(e == s):
                        verificadas += 1
            utxo_entradas += 1
        if(verificadas == utxo_entradas):
            t.aprobar_transaccion()
            return True
        else:
            return False
        
    #se retorna la informacion del bloque    
    def retornar_bloque(self):
        return f'Hash del bloque: {self.hash_bloque}.\nHash Previo: {self.hash_previo}.\nNonce: {self.nonce}.\nHash Raiz: {self.hash_raiz}.\nTransacciones: {self.data_tx}.'
    
    #se retorna solo la data del bloque    
    def data_bloque(self):
        return f'{self.hash_bloque}{self.hash_previo}{self.nonce}{self.hash_raiz}{self.transacciones}'
    
    #creando el arbol de merkle
    def crear_arbol(self):
        nivel = 1
        hojas = []
        for tx in self.data_tx:
            hojas.append(hash_Sha256(tx))
        while(len(hojas)>1):
            hojas_up = []
            if (len(hojas) % 2 != 0):
                hojas.append(hojas[-1])
            for i in range(0, len(hojas) - 1, 2):
                hojas_up.append(hash_Sha256(str(hojas[i] + hojas[i+1])))
            hojas = hojas_up
            nivel += 1
        self.hash_raiz = hojas
    
    #creando el bloque una vez se tiene el arbol, su hash y el nonce    
    def crear_bloque(self, numero_de_ceros):
        self.crear_arbol()
        self.proof_of_work(numero_de_ceros)
        
    #proof of work
    def proof_of_work(self, numero_ceros):
        validador = True
        cadena_ceros = ""
        for i in range(0,numero_ceros):
            cadena_ceros = cadena_ceros + "0"
        while(validador):
            self.nonce = random.randint(1000000,2000000)
            self.hash_bloque = hash_Sha256(self.data_bloque())
            if(str(self.hash_bloque).startswith(cadena_ceros)):
                validador = False
        

#probando la clase bloque
weimar = ["Weimar",100]
pedro = ["Pedro",100]
manuel = ["Manuel",100]
andres = ["Andres",100]
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
 
bloque1 = Bloque("hashPrevio001")
t0 = Transaccion()
t0.adicionar_entrada(["Weimar",100])
t0.adicionar_salida(["Weimar",100])
t1 = Transaccion()
t1.adicionar_entrada(["Manuel",100])
t1.adicionar_salida(["Manuel",100])
bloque1.data_tx.append(t0.retornar_info())
bloque1.transacciones.append(t0)  
bloque1.data_tx.append(t1.retornar_info())
bloque1.transacciones.append(t1)
bloque1.adicionar_transacciones([transaccion1,transaccion2])
bloque1.crear_bloque(2)
print(bloque1.retornar_bloque())


    
    
    