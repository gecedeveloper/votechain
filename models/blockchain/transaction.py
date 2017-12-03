""" Modelo de datos de Transacción """

class Transaction(object):
    """ Constructor """
    def __init__(self, index, timestamp, current_transactions, proof, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = current_transactions
        self.proof = proof
        self.previous_hash = previous_hash
