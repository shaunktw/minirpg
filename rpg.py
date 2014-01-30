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
			 "I have a small puppy that's better than this.."]

	def enter(self):
		pass
#Central Corridor is a scene since it's a type of scene
class CentralCorridor(Scene):

	def enter(self):
		pass

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