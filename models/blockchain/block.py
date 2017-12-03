""" Modelo de datos de Bloque """
from db import DB

class Block(object):
    """ Constructor """
    def __init__(self, index, timestamp, current_transactions, proof, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = current_transactions
        self.proof = proof
        self.previous_hash = previous_hash

    def find_block_by_index(self, index):
        """ Find a block by given index """
        return DB.child('chain').child('blocks').child(index).get()
