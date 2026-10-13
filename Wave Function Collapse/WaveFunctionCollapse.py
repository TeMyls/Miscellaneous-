import random
import time 
# for windows
import os
#for pythonista
#import console

#1 water
#only borders sand and itself
#2 sand
#only borders water,grass and itself
#3 trees
#only borders grass and itself
#4 dirt
#only borders trees, sand and itself

print("1 is water","2 is sand","3 is tree","4 is dirt", sep = "\n")

#left,down,right,up

blank_cell = 0
water_cell = 1
sand_cell = 2
tree_cell = 3
dirt_cell = 4


X = [0,1,0,-1]
Y = [-1,0,1,0]

_options = {
	water_cell:[water_cell,sand_cell],
	sand_cell:[water_cell,sand_cell,dirt_cell],
	tree_cell:[tree_cell,dirt_cell],
	dirt_cell:[sand_cell,tree_cell,dirt_cell]
				}

options = {
	water_cell:{
		water_cell: True,
		sand_cell: True,
		tree_cell: False,
		dirt_cell: False
	},
	sand_cell:{
		water_cell: True,
		sand_cell: True,
		tree_cell: False,
		dirt_cell: True
	},
	tree_cell:{
		water_cell: False,
		sand_cell: False,
		tree_cell: True,
		dirt_cell: True
	},
	dirt_cell:{
		water_cell: False,
		sand_cell: True,
		tree_cell: True,
		dirt_cell: True
	}
}


is_possible = {
		water_cell: True,
		sand_cell: True,
		tree_cell: True,
		dirt_cell: True
}

colors = {

	blank_cell:'✨ ',
	water_cell:'💧 ',
	sand_cell:'🏝️ ',
	tree_cell:'🌲 ',
	dirt_cell:'🌱 '
	
	
	
}
					



def empty_map(rows,columns, color):
	return [[color]*columns for i in range(rows)]
			

def in_bounds(x, y,grid_w,grid_h):
		return -1 < x < grid_w and -1 < y < grid_h
				
				


def set_seed_tile(array_2d):
	#position of starting tileoit
	row,col = random.randint(0,len(array_2d)-1), random.randint(0,len(array_2d[0])-1)
	return row, col



def display(arr):
	h=''
	for i in arr:
		for j in i:
				if type(j) != type([]):
					h = h +  colors[j]
				else:
					h = h +  "🎬 "
		h = h + '\n'
	print(h)

def display_true(arr):
	h=''
	for i in arr:
		for j in i:
				h = h + str(j) + " "
		h = h + '\n'
	print(h)

	
def flood_fill_collapse(array_2d, row, col, is_bfs = True):
	w = len(array_2d[0])
	h = len(array_2d)
	#direction vectors in array
	#[up,right,down,left]
	#x_vectors = [0,-1,0,1]
	#y_vectors = [-1,0,1,0]
	
	x_vectors = [0 , -1,-1,-1, 0, 1, 1]
	y_vectors = [-1, -1, 0, 1, 1, 1, 0]
	
	#queue
	visited = []
	deque = []
	deque.append([row,col])
	#print(array_2d[row][col])
	#The first cell is initially an array pf choices
	#it is collapsed to an integer
	#array_2d[row][col] = random.choice(array_2d[row][col])
	
	while deque:
		cur = deque.pop(0) if is_bfs else deque.pop()
		
		if in_bounds(cur[1],cur[0],w,h) and  [cur[0],cur[1]] not in visited:
			
				
			final_options = {
					water_cell: True,
					sand_cell: True,
					tree_cell: True,
					dirt_cell: True
			}
			
			neighbor_options = []
			
			for i in range(len(x_vectors)):
				y = cur[0] + y_vectors[i]
				x = cur[1] + x_vectors[i]
				
				if in_bounds(x,y,w,h):
					# essentially s
					neighbor = array_2d[y][x]
					if neighbor in list(is_possible.keys()):
						for key in options[neighbor]:
							#the very first is a copy
							if i == 0:
								final_options[key] = options[neighbor][key]
							else:
								final_options[key] = final_options[key] and options[neighbor][key]
								
				
			for key, value in final_options.items():
				if value:
					neighbor_options.append(key)

			choice = -1
			if len(neighbor_options) == 1:
				choice = neighbor_options[0]
			else:
				choice = random.choice(neighbor_options)
				
			array_2d[cur[0]][cur[1]] = choice
			visited.append([cur[0],cur[1]])
			
			#prints everythin
			#console.clear()
            os.system('cls')
			display_true(array_2d)
			#display(array_2d)
			time.sleep(.014)
			deque.append([cur[0] + 1, cur[1]])
			deque.append([cur[0] - 1, cur[1]])
			deque.append([cur[0], cur[1] + 1])
			deque.append([cur[0], cur[1] - 1])
			
			
			
			
		#console.clear()
		#os.system('cls')
		
	
	#console.clear()
	#os.system('cls')
	display_true(array_2d)
	#display(array_2d)
	
			
			
def wave_function_collapse(rows,cols):
	msg = '''1 water: only borders sand and itself\n2 sand: only borders water,grass and itself\n3 trees: only borders grass and itself\n4 dirt: only borders trees, sand and itself\n
	'''
	print(options)
	print(msg)
	
	arena = empty_map(rows,cols, 0)
	display_true(arena)
	x,y = set_seed_tile(arena)
	flood_fill_collapse(arena,x,y, True)
	print("1 is water","2 is sand","3 is tree","4 is dirt", sep = "\n")
	print(options)
	print(msg)
	display(arena)
	
wave_function_collapse(10, 10)