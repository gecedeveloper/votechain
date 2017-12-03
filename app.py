""" hashlib para hashear con sha256, json y time """
from uuid import uuid4
from models.blockchain import Blockchain

from flask import Flask

# Instantiate our Node
APP = Flask(__name__)

# Generate a globally unique address for this node
NODE_IDENTIFIER = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
BLOCKCHAIN = Blockchain()
