class Scene(object):

	def enter(self):
		pass

#Death inherits scene since it's a type of scene
class Death(Scene):

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