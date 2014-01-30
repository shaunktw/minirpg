import unittest
from rpg import Room

class RPGTest(unittest.TestCase):

	def test_room(self):
		gold = Room("GoldRoom",
			"""This room has gold in it you can grab. There's a door to the north""")
		self.assertEqual(gold.name, "GoldRoom")
		self.assertEqual(gold.paths, {})

	def test_room_paths(self):
		center = Room("Center", "Test room in the center.")
		north  = Room("North", "Test room in the north.")
		south  = Room("South", "Test room in the south.")