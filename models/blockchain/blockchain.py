""" hashlib para hashear con sha256, json y time """
import json

from time import time
from db import DB
from models.blockchain.block import Block

class Blockchain(object):
    """ Constructor """
    def __init__(self):
        # Obtiene cadena desde Firebase
        self.chain = DB.child('chain').get().val()
        # Si no existe, creamos una nueva y un bloque génesis
        if self.chain is None:
            self.chain = []
            self.current_transactions = []
            self.new_block(previous_hash=1, proof=100)
            self.nodes = set()

    def new_block(self, proof, previous_hash=None):
        """
        Crea un nuevo bloque y lo agrega a la cadena

        :param proof: <int> La prueba dada por el algoritmo de Prueba de Trabajo
        :param previous_hash: (Optional) <str> Hash del bloque anterior
        :return: <dict> Nuevo Bloque
        """
        index = len(self.chain) + 1
        block = Block(index, time(), self.current_transactions, proof, previous_hash)

        # Restauramos la lista de transacciones actuales
        self.current_transactions = []

        
        # Agregamos el nuevo bloque a la cadena directamente si es el bloque génesis
        DB.child("chain").child("blocks").push(block.__dict__)

        return block
