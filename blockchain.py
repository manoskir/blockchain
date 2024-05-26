import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

	def new_block(self, proof, pevious_hash=None):
		'''
		Creates a new Block and adds it to the chain
		:param proof: <int> The proof given by the proof of work algo
		:param previous_hash: (Optional) <str> Hash of previous block
		:return: <dict> new block
		'''

		block = {
			'index': len(self.chain) + 1,
			'timestamp': time(),
			'transactions': self.current_transactions,
			'proof': proof,
			'previous_hash': previous_hash or self.hash(self.chain[-1])
		}

		#resets the list of current transactions
		self.current_transactions = []

		self.chain.append(block)
		return block


	def new_transaction(self, sender, recipent, amount):
		# Adds a new transaction to the list of transactions
		self.current_transactions.append({
			'sender': sender,
			'recipent': recipent
			'amount': amount
			})

		return self.last_block['index'] + 1

	def proof_of_work(self, last_proof):
		'''
		utilizes valid proof and adds 1 in the proof number until it finds the solution
		'''
		proof = 0
		while valid_proof(last_proof, proof) is False:

			proof += 1

		return proof 


	@staticmethod
	def valid_proof(last_proof, proof):

		'''
		takes last proof and puts it together with current proof
		hashes it and returns True if solution has 4 leading zeros, false if not
		'''

		guess = f'{last_proof}{proof}'.encode()
		guess_hash = hashlib.sha256(guess).hexdigest()

		return guess_hash[:4] == "0000"

	@staticmethod
	def hash(block):
		# Creates a sha-256 hash of a block
		# The dictionary must be orderd, or we'll have inconsistencies and this is why we use the json dumps
		block_string = json.dumps(block, sort_keys=True).encode()

		return hashlib.sha256(block_string).hexdigest()

	@property
	def last_block(self):
		#returns the last block in the chain
		return self.chain[-1]


#initiate our Node
app = Flask(__name__)

#Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

#initiate the blockchain
blockchain = Blockchain()

#creates /mine endpoint (get request)
@app.route('/mine', methods=['GET'])
def mine():
	return "We'll mine a new Block"

#creates the /transactions/new endpoint (post request since we're sending data)
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
	return "We'll add a new transaction"

#creates the /chain endpoint that returns the full blockchain
@app.route('/chain', methods=['GET'])
def full_chain():

	response = {

		'chain': blockchain.chain,
		'length': len(blockchain.chain),

	}

	return jsonify(response), 200

#runs the server on port 5000
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)