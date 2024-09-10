#se importa la clase bloque
from bloque_bit import Bloque

#clase blockchain
class BlockChain:
    def __init__(self, numero_bloques):
        self.numero_bloques = numero_bloques
        self.bloque_genesis = Bloque()