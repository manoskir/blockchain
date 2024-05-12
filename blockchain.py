

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

	def new_block(self):
		# Creates a new Block and adds it to the chain
		pass

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
		# Hashes a block
		pass

	@property
	def last_block(self):
		#returns the last block in the chain
		pass


		