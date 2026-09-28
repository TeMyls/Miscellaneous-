import math
import random
import console
import os
import time


floor_color = 1
unknown_color = 2
wall_color = 0
player_color = 7
enemy_color = 9
up_stairs_color = 8
down_stairs_color = 6


#these can be anything but the wall color
visited_color = 1

'''
if col == wall_color:
				h = h + '#'
			elif col == floor_color:
				h = h + '.'
			elif col == unknown_color:
				h = h + '?'
			elif col == player_color:
				h = h + '@'
			elif col == up_stairs_color:
				h = h + 'u'
			elif col == down_stairs_color:
				h = h + 'd'
			else:
				h = h + '.'
				
'''
colors = {

	#wall_color:'#',
	floor_color:'.',
	player_color:'@',
	#unknown_color:'?',
	#up_stairs_color:'>',
	enemy_color: 'V',
	#down_stairs_color:'<'
	
	
	
}


def create_1D_array(rows,columns,color):
	return [[color]*columns for i in range(rows)]

def in_bounds(x, y, w, h):
	return -1 < x < w and -1 < y < h
	
def display(arr):
	h=''
	for i in arr:
		for j in i:
				if colors.get(j):
					h = h + colors[j]
				else:
					h = h + str(j)
		h = h + '\n'
	print(h)

def display_true(arr):
	h=''
	for i in arr:
		for j in i:
				h = h + str(j) + " "
		h = h + '\n'
	print(h)




def get_tile_type(grid, tile_int):
	tiles = []
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] == tile_int:
				tiles.append([x, y])
			else:
				continue
	return tiles

def create_execution_stack(units: list, threshold: int):
	# Fill initiative bars
	
	ready = []
	while True:
		for unit in units:
			unit["time"] += unit["speed"]
			
		ready = [u for u in units if u["time"] >= threshold]
		if ready:
			break
			
	ready = sorted(ready, key=lambda x: x["time"])
	
	# Spend initiative
	for unit in ready:
		if unit["time"] >= threshold:
			unit["time"] -= unit["time"]
	# decide who moves
	'''
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
	'''
	return  ready



def make_unit(name : str, speed: int, hp: int, tile: int):
	return {
		"name" : name,
		"speed": speed,
		"time" : 0,
		"hp"	 : hp,
		"x"		 :-1,
		"y"		 :-1,
		"atk"  :-1,
		"visited": [],
		# entity tile
		"etile": tile,
		# ground tile
		"gtile": tile,
		
	}
		
	
def add_unit(grid, units, tiles_floor, name, speed, health, color):
	idx = random.randint(0, len(tiles_floor) - 1)
	px, py = tiles_floor.pop(idx)
	
	units.append(make_unit(name, speed, health, color))
	ulen = len(units) - 1
	units[ulen]["x"] = px
	units[ulen]["y"] = py
	units[ulen]["etile"] = color
	units[ulen]["gtile"] = floor_color
	grid[py][px] = color
	
def game_loop():
	ROWS = 10
	COLS = 20
	room_num = 2
	#grid, rooms = floor_maker(ROWS,COLS,room_num)
	grid = create_1D_array(ROWS, COLS, floor_color)
	
	#[N,NE,E,SE,S,SW,W]
	#possible directions
	#8 direction
	#x_vectors = []
	#y_vectors = []
	xf_vectors = [0,1,-1,1,0,-1,1,-1]
	yf_vectors = [-1,-1,0,1,1,1,0,-1]
	#[N,E,S,W]
	#4 direction
	x_vectors = [0,-1,0,1]
	y_vectors = [-1,0,1,0]
	directions = {
		#y, x
		#north
		"w":[-1, 0],
		#east
		"a":[0, -1],
		#south
		"s":[1, 0],
		#west
		"d":[0, 1],
	}
	
	threshold = 8
	
	tiles_floor = get_tile_type(grid, floor_color)
	
	
	
	
	
	
	
	
	units = []
	# add_unit(grid, units, tiles_floor, name, speed, health, color):
	add_unit(grid, units, tiles_floor, "player", 9, 10, player_color)
	
	for i in range(15):
		add_unit(grid, units, tiles_floor, "enemy", 8, 10, enemy_color)
	
	
	display(grid)
	# display_true(grid)
	dir = ""
	msg = []
	
	#print("Commands: \n \'W\':North \n \'A\':East \n \'S\':South \n \'D\':West")
	while True:
		
		
		
		
		
		if msg:
			for sentence in msg:
				print(sentence)
		
	
		msg.clear()
		end_loop = False
		
		
		
		console.clear()
		display(grid)
		cnt = 0
		for i in grid:
			for j in i:
				if j == enemy_color:
					cnt += 1
					
				
				
		print("Enemy Count:", cnt)
		#print(execution_stack)
		#print(units)
		dir = input(f"Move? WASD: ")
		for letter in dir:
			execution_stack = create_execution_stack(units, threshold)
			while execution_stack:
				
				
				unit = execution_stack.pop()
				if unit["name"] == "player":
					# moving the player
					# processing player input
					
						
						
						
					if directions.get(letter):
						
						temp_x = unit['x'] + directions[letter][1]
						temp_y = unit['y'] + directions[letter][0]
					
						within_bounds = in_bounds(temp_x,temp_y,len(grid[0]),len(grid))
					
						if not within_bounds:
							continue
							
						is_wall = grid[temp_y][temp_x] == wall_color
						
						is_unit = grid[temp_y][temp_x] == enemy_color
						
						if is_wall:
							continue
							
						if is_unit:
							continue
						#setting previous tile back to what it was
						grid[unit['y']][unit['x']] = floor_color
						#setting the new groud tile to whatever is beneath
						unit['gtile'] = floor_color
						#setiing and updating the player  position
						unit['x'] = temp_x
						unit['y'] = temp_y
						grid[unit['y']][unit['x']] = player_color
							
				else:
					
					possible_tiles = []
					temp_x = -1
					temp_y = -1
					for i in range(len(xf_vectors)):
						
						temp_x = unit['x'] + xf_vectors[i]
						temp_y = unit['y'] + yf_vectors[i]
						
						
						
						
						
						within_bounds = in_bounds(temp_x,temp_y,len(grid[0]),len(grid))
						
						if not within_bounds:
							continue
							
						is_wall = grid[temp_y][temp_x] == wall_color
						
						is_player = grid[temp_y][temp_x] == player_color 
						
						is_unit = grid[temp_y][temp_x] == enemy_color
							
						if is_wall:
							continue
							
						if is_player:
							continue
							
						if is_unit:
							continue
						
						
						
						
						if [temp_x, temp_y] in unit['visited']:
							continue
						else:
							if len(unit['visited']) < 11:
								
								unit['visited'].append([temp_x, temp_y])
							else:
								unit['visited'].pop(0)
								unit['visited'].append([temp_x, temp_y])
								
						possible_tiles.append([temp_x, temp_y])
								
							
						
					
					if possible_tiles:
						#print(possible_tiles)
						temp_x, temp_y = random.choice(possible_tiles)
						
					else:
						if unit["visited"]:
							temp_x, temp_y = unit["visited"].pop()
							#setting previous tile back to what it was
							
					grid[unit['y']][unit['x']] = floor_color
					#setting the new groud tile to whatever is beneath
					unit['gtile'] = floor_color				
					#setiing and updating the player  position
					unit['x'] = temp_x
					unit['y'] = temp_y
					grid[unit['y']][unit['x']] = enemy_color
				
			
				
			
				#display(grid)
				
				#for pythonista
				#console.clear()
                #for windows
                os.system('cls')
				display(grid)
				time.sleep(0.01)
		# display_true(grid)
		#os.system('cls')
		



	
	


game_loop()

	
	