import random
import math
import console
import os

def clear_console():
		# clearing the console
		#on windows
		os.system('cls')
		#on pythonista
		#console.clear()

def rand_choice(arr, weight_ls, k):
	return random.choices(arr,weights = weight_ls,k = k)

def get_ready(units: list):
	# Fill initiative bars
	
	ready = []
	while True:
		for unit in units:
			unit["time"] += unit["speed"]
			
		ready = [u for u in units if u["time"] >= 100]
		if ready:
			break
	return  ready
	
def start_ready(ready: list, units: list):
	if ready:
		# decide who moves
		print("ready", ready)
		actor = ready[0]
		for unit in ready:
			if unit["time"] > actor["time"]:
				actor = unit
				
		print("{} acts".format( actor["name"] ))
	
		# Spend initiative
		actor["time"] -= actor["time"]
		print([(u["name"], u["time"]) for u in units])
		print()
		
def make_unit(name : str, speed: int):
	return {
		"name" : name,
		"speed": speed,
		"time" : 0,
		
	}


def run_turn_test():
	units = [
	
		make_unit("Hero", 15),
		make_unit("Goblin", 25),
		make_unit("Mage", 10),
		make_unit("Thief", 30)
		
	]
		
	for turn in range(50):
		print(f"Turn {turn + 1}")
		ready = get_ready(units)
		start_ready(ready, units)
	
	

def culm_hp(units):
	total_hp = 0
	for unit in units:
			total_hp += unit["hp"]
	return  total_hp
	
def run_turn_game():
	units = [
		
		{
			"name" : "Knight",
			"speed": 10,
			"time" : 0,
			# above is the basics
			"hp"   : 25,
			"dmg"  : 15,
			"dfn"  : 20,
			"eva" : 8,
			"state": ""
		},
		{
			"name" : "Mage",
			"speed": 7,
			"time" : 0,
			# above is the basics
			"hp"   : 15,
			"dmg"  : 25,
			"dfn"  : 15,
			"eva" : 14,
			"state": ""
		},
		{
			"name" : "Thief",
			"speed": 18,
			"time" : 0,
			# above is the basics
			"hp"   : 12,
			"dmg"  : 8,
			"dfn"  : 11,
			"eva" : 20,
			"state": ""
		},
		{
		
			"name" : "Troll",
			"speed": 9,
			"time" : 0,
			# above is the basics
			"hp"   : 110,
			"dmg"  : 6,
			"dfn"  : 20,
			"eva" : 2,
			"state": ""
		},
	]
	#print(units[:3], units[3:])
	
	hero_hp = culm_hp(units[:3]) 
	enemy_hp = units[3]["hp"]
	msg = ""
	while hero_hp > 0  and enemy_hp > 0:
		print("The {} is waiting. \n\tHP: {}".format(units[3]["name"], units[3]["hp"]))
		s = "Your Team:"
		for unit in units[:3]:
			s += "\n\tName:" + unit["name"] + "\n\t\tHp:" + str(unit["hp"])
		print(s)
		print(msg)
		ready = []
		while True:
			# incrementing progress
			for unit in units:
				unit["time"] += unit["speed"]
				
			
			# finding who is above the threshold
			ready = [u for u in units if u["time"] >= 100]
			if ready:
				break
				
		#print("ready", ready)
		actor = ready[0]
		for unit in ready:
			if unit["time"] > actor["time"]:
				actor = unit
		
		if actor in units[:3]:
			acted = False
			while not acted:
				action = input("What will {} do?\n (A)ttack or (D)efend?".format(actor["name"]))
				dmg = actor["dmg"]
				#def = actor["dfn"]
				if action.upper() == "A":
					
					admg = random.randint(
						math.floor(dmg - dmg *.10), 
						dmg
					)
					
					if (units[3]["dfn"] - admg) > 0:
						units[3]["hp"] -= (units[3]["dfn"] - admg)
						msg = "{} attacks, {} takes {} damage".format(actor["name"], units[3]["name"], (units[3]["dfn"] - admg))
					else:
						units[3]["hp"] -= math.floor(admg/1.5)
						msg = "{} attacks, {} takes {} damage".format(actor["name"], units[3]["name"], math.floor(admg/1.5))
					
					
					
					actor["state"] = "A"
					acted = True
				elif action.upper() == "D":
					actor["state"] = "D"
					msg = "{} defends".format(actor["name"])
					acted = True
				else:
					print("Invalid Action, enter again.")
					
			#print("{} acts".format( actor["name"] ))
		else:
			#print("{} acts".format( actor["name"] ))
			rdm = math.floor(random.random() * 3)
			options = ["A", "D", "H"]
			action = rand_choice(options, [4, 2, 2], 1)[0]
			target = rand_choice(units[:3], [2, 1, 1], 1)[0]
			dmg = units[3]["dmg"]
			
			admg = random.randint(
						math.floor(dmg - dmg *.10), 
						dmg
					)
			heal = random.randint(
						math.floor(10 - 10 *.10), 
						10
					)
			if action == "A":
				msg = "{} attacks, {} takes {} damage".format(units[3]["name"], target["name"], (target["dfn"] - admg))
				target["hp"] -= (target["dfn"] - admg)
			elif action == "D":
				units[3]["state"] = "D"
				msg = "{} defends".format(units[3]["name"])
			elif action == "H":
				units[3]["hp"] += heal
				msg = "{} heals for {} health".format(units[3]["name"], heal)
			
			
			
			
	
		# Spend initiative
		actor["time"] -= actor["time"]
		hero_hp = culm_hp(units[:3]) 
		enemy_hp = units[3]["hp"]
		#clear_console()
		
		print([(u["name"], u["time"]) for u in units])
		#print()
		#break
				
	if culm_hp(units[:3]) > 0:
		print("You won")
		
	else:
		print("The Troll won...")

run_turn_test()

#run_turn_game()


		
		
	
		
