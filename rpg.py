from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()"
		exit(1)

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
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew."
		print "You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an escape pod."
		print "You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth," 
		print "and evil clown costume flowing around his hate filled body. He's blocking the door to the Armory and about to pull a weapon to blast you."

		action = raw_input("What do you want to do? (shoot, dodge, run) > " )
		if action == "shoot":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws off your aim."
			print "Your laser hits his costume but misses him entirely. This completely ruins his brand new costume"
			print "his mother bought him, which makes him fly into an insane rage and blast you repeatedly in the face until you are dead.",  
			print "Then he eats you."
			return 'death'

		elif action == "dodge":
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you" 
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return 'death'

		elif action =="run":
			print "Lucky for you, the Gothon has not been hitting the gym much. You curse the Gothon in its language:"
			print "Lbhe zbgure vf fb sng!! jura fur fvgf nebhaq gur ubhfr! fur fvgf nebhaq gur ubhfr!"
			print "The Gothon stops, tries not to laugh, then busts out laughing and can't move because of your poor pronunciation."
			print "You take the opportunity and shoot him square in the head putting him down, then jump through the Weapon Armory door."
			return 'laser_weapon_armory'
		else:
			print "Please enter a valid action: shoot, dodge or run"
			return 'central_corridor'

class LaserWeaponArmory(Scene):

	def enter(self):
		print "You do a crazy wheelcart into the Weapon Armoury, crounch and scan the room"
		print "for more Gothons that might be hiding. It's dead quiet..too quiet...."
		print "You stand up and run to the far side of the room and find the"
		print "neutron bomb in its container. There's a keypad lock on the box"
		print "and you need the code to get the bomb out. If you get the code wrong 10 times"
		print "then the lock closes forever and you can't get the bomb. The code is 3 digits."

		code = "{0} {1} {2}".format(randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[KEYPAD]> ")
		guesses = 0

		while guess != code and guesses < 10:
			print "BZZZZZZZZZZZZZ!!!"
			guesses += 1
			guess = raw_input("[KEYPAD]> ")

		if guess == code:
			print "The container clicks open and the seal breaks, letting gas out."
			print "You grab the neutron bomb and run as fast as you can to the"
			print "bridge where you must place the bomb in the right spot."
			return 'bridge'
		else:
			print "The lock buzzes one last time and then you hear a loud melting sound"
			print "as the mechanism is fused together. You decide to sit there, and finally"
			print "the Gothons blow up the ship from their ship and you die...."
			return 'death'

class theBridge(Scene):
	
	def enter(self):
		pass

class EscapePod(Scene):

	def enter(self):
		pass

class Engine(object):

	def __init__(self, scene_map):
		print "Engine __init__ has scene_map", scene_map
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		print "Play's first scene", current_scene

		while True:
			print "\n-----------"
			next_scene_name = current_scene.enter()
			print "next_scene", next_scene_name
			current_scene = self.scene_map.next_scene(next_scene_name)
			print "map returns new scene", current_scene

class Map(object):

	scenes = { 'central_corridor': CentralCorridor(),
		       'death': Death(),
		       'escape_pod': EscapePod(),
		       'laser_weapon_armory': LaserWeaponArmory(),
		       'the_bridge': theBridge()
		       }

	def __init__(self, start_scene):
		self.start_scene = start_scene
		print "start_scene in __init__", self.start_scene

	def next_scene(self, scene_name):
		print "start_scene in next_scene"
		val = Map.scenes.get(scene_name)
		print "next_scene returns", val
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()