import unittest
import random
from rpg import Scene, Death

class RPGTest(unittest.TestCase):

	def setUp(self):
		self.randTest = random.Random()
		rng = self.randTest
		rng.seed(42)

	def test_room(self):
		gold = Scene("GoldRoom",
			"""This room has gold in it you can grab. There's a door to the north""")
		self.assertEqual(gold.name, "GoldRoom")
		self.assertEqual(gold.paths, {})

	def test_room_paths(self):
		center = Scene("Center", "Test room in the center.")
		north  = Scene("North", "Test room in the north.")
		south  = Scene("South", "Test room in the south.")

		center.add_paths({'north': north, 'south':south})
		self.assertEqual(center.go('north'), north)
		self.assertEqual(center.go('south'), south)

	def test_death_scene(self):
		death = Death("Death Scene", 
			"""You kinda suck at this""")
		assert self.death.quips(rng.randint(0,4)) == "My grandma can play better than you."
		assert self.death.quips(rng.randint(0,3)) == "You should retire..and get go to gaming school"
		assert self.death.quips(rng.randint(0,2)) == "I have a small puppy that's better than you"