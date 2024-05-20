from time import time
import hashlib
import json

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