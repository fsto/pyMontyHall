import random

class MontyHall(object):
	""" Monty Hall implementation.
	"""
	def __init__(self, num_doors):
		self.num_doors = num_doors
		self.doors     = self._generate_doors()
		
	def _generate_doors(self):
		""" Generate doors and place True behind one of them.
		"""
		true_index = random.randint(0, self.num_doors - 1)
		return [d == true_index for d in range(self.num_doors)]

	def make_choice(self, keep_initial_choice=True):
		""" Make a choice by either keeping initial choice or changing to
			another than the opened.
		"""
		# Choose a random doors
		initial_choice = random.randint(0, self.num_doors - 1)

		# Open a not chosen False door
		next_door = (initial_choice + 1) % self.num_doors
		prev_door = (initial_choice - 1) % self.num_doors
		new_alterative = prev_door if self.doors[next_door] == False else next_door

		return self.doors[new_alterative] if not keep_initial_choice else self.doors[initial_choice]
		