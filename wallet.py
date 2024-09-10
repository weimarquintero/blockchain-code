#import para trabajar con hash
from hashlib import *

#funcion que cacula el hash de un dato
def hash_Sha256(data):
    return sha256(data.encode('utf-8')).hexdigest()

#clase que crea un ID con un balance o saldo
class Wallet:
    def __init__(self, id, balance):
        self.clave_publica = hash_Sha256(id)
        self.balance = balance

    def retornar_wallet(self):
        return (self.clave_publica,self.balance)