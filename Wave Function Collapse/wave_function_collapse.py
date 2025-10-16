import random
import time 
#for windows
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

options = {
	water_cell:[water_cell,sand_cell],
	sand_cell:[water_cell,sand_cell,dirt_cell],
	tree_cell:[tree_cell,dirt_cell],
	dirt_cell:[sand_cell,tree_cell,dirt_cell]
				}

uncollapsed = [water_cell, sand_cell, tree_cell, dirt_cell]
		


colors = {

	blank_cell:'✨ ',
	water_cell:'💧 ',
	sand_cell:'🏝️ ',
	tree_cell:'🌲 ',
	dirt_cell:'🌱 '
	
	
	
}
					



def empty_map(rows,columns, filler):
	return [[filler.copy() for j in range(columns)] for j in range(rows)]
			

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

	
def flood_fill_collapse(array_2d, row, col):
	w = len(array_2d[0])
	h = len(array_2d)
	#direction vectors in array
	#[up,right,down,left]
	x_vectors = [0,-1,0,1]
	y_vectors = [-1,0,1,0]
	
	#queue
	visited = []
	queue = []
	queue.append([row,col])
	#print(array_2d[row][col])
	#The first cell is initially an array pf choices
	#it is collapsed to an integer
	array_2d[row][col] = random.choice(array_2d[row][col])
	for i in range(len(x_vectors)):
		y = row + y_vectors[i]
		x = col + x_vectors[i]
		if in_bounds(x,y,w,h):
			#
			array_2d[y][x] = options[array_2d[row][col]]
	
	while queue:
		cur = queue.pop(0)
		
		if in_bounds(cur[1],cur[0],w,h) and  [cur[0],cur[1]] not in visited:
			
			
			#print(visited)
			# collapsing cell to a number
			if type(array_2d[cur[0]][cur[1]]) == type([]):
				#if its an array
				array_2d[cur[0]][cur[1]] = random.choice( array_2d[cur[0]][cur[1]])
			'''
			else:
				print('ye')
				y, x = visited[-1]
				array_2d[cur[0]][cur[1]] = array_2d[y][x]
			'''
				
			
			if visited:
				#possible future values of X and Y depending on position
				
				
				for i in range(len(x_vectors)):
					y = cur[0] + y_vectors[i]
					x = cur[1] + x_vectors[i]
					
					if in_bounds(x,y,w,h):
						# neighbors should be the uncollapsed array 
						# this array is edited by it's collapsed neighbor
						# works because python allows multiple types in arrays in other launguages two 2D arrays would have to be managed
						neighbor = array_2d[y][x]
						if type(neighbor) == type(
							[]):
							#if the 
							idx_to_pop = []
							#print('e')
							for j in range(len(neighbor)):
								
								if neighbor[j] not in options[array_2d[cur[0]][cur[1]]]:
									idx_to_pop.append(j)
							
							
							while idx_to_pop:
								
								idx = idx_to_pop.pop()
								#if len(neighbor) > 1:
								neighbor.pop(idx)
							

			visited.append([cur[0],cur[1]])
			
			display_true(array_2d)
			#display(array_2d)
			time.sleep(.015)
			queue.append([cur[0] + 1, cur[1]])
			queue.append([cur[0] - 1, cur[1]])
			queue.append([cur[0], cur[1] + 1])
			queue.append([cur[0], cur[1] - 1])
			
			
			
			
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
	arena = empty_map(rows,cols,uncollapsed)
	x,y = set_seed_tile(arena)
	flood_fill_collapse(arena,x,y)
	print("1 is water","2 is sand","3 is tree","4 is dirt", sep = "\n")
	print(options)
	print(msg)
	display(arena)
	
wave_function_collapse(3, 3)
