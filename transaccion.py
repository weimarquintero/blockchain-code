#importaciones de la clase
from hashlib import *

#funcion que cacula el hash de un dato
def hash_Sha256(data):
    return sha256(data.encode('utf-8')).hexdigest()

#clase transaccion
class Transaccion:
    def __init__(self):
        self.id = ""
        self.valida = False
        self.aprobada = False
        self.entradas = []
        self.salidas = []
        
    def adicionar_entrada(self, entrada):
        self.entradas.append(entrada)
        
    def adicionar_salida(self, salida):
        self.salidas.append(salida)
        
    def validar_transaccion(self):
        suma_entradas = 0
        suma_salidas = 0
        for i in self.entradas:
            suma_entradas = suma_entradas + i[1]
        for j in self.salidas:
            suma_salidas = suma_salidas + j[1]
        if (suma_entradas==suma_salidas):
            self.valida = True
        return self.valida
    
    def retornar_data(self):
        return f'{self.valida}{self.aprobada}{self.entradas}{self.salidas}'
    
    #se retorna la informacion del bloque    
    def retornar_info(self):
        return f'ID: {self.id}. Validada: {self.valida}. Aprobada: {self.aprobada}. Entradas: {self.entradas}. Salidas: {self.salidas}.'
    
    def crear_id(self):
        self.id = hash_Sha256(self.retornar_data())