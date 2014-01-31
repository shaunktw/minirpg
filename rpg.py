class Scene(object):

	def enter(self):
		pass

	def __init__(self,name,description):
		self.name = name
		self.description = description
		self.paths = {}
	
	def add_paths(self, paths):
		self.paths.update(paths)

	def go(self, direction):
		return self.paths.get(direction, None)

#Death inherits scene since it's a type of scene
class Death(Scene):

	quips = ["You died. You suck bad.",
			 "Your mom would be proud..if she were smarter.",
			 "My grandma can play better than you.",
			 "You should retire..and get go to gaming school",
			 "I have a small puppy that's better than you"]

	def enter(self):
		print Death.quips[randint(0,len(self.quips)-1)]
		exit(1)
#Central Corridor is a scene since it's a type of scene
class CentralCorridor(Scene):

	def enter(self):
		print """ The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew.
		You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory,
		put it in the bridge, and blow the ship up after getting into an escape pod. \n
        You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, 
        and evil clown costume flowing around his hate filled body. He's blocking the door to the Armory and about to pull a weapon to blast you. """

class LaserWeaponArmory(Scene):

	def enter(self):
		pass

class theBridge(Scene):

	def enter(self):
		pass

class EscapePod(Scene):

	def enter(self):
		pass

class Engine(object):

	def __init__(self, scene_map):
		pass

	def play(self):
		pass

class Map(object):

	def __init__(self, start_scene):
		pass

	def next_scene(self):
		pass

	def opening_scene(self):
		pass