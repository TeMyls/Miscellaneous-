import random
import time 
#for pythonista
#import console
#outside of pythonista
import os
#0 any
#it is a blamk cell that can be anything
#1 water
#only boarders sand and itself
#2 sand
#only boarders water,grass and itself
#3 trees
#only boarders grass and itself
#4 dirt
#only boarders trees, sand and itself

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
				
		

colors = {

	blank_cell:'⬜️',
	water_cell:'🟦',
	sand_cell:'🟧',
	tree_cell:'🟩',
	dirt_cell:'🟫'
	
	
	
}
					



def empty_map(rows,columns,color):
	return [[color]*columns for i in range(rows)]
			
def in_bounds(x, y,grid_w,grid_h):
		return 0 <= x < grid_w and 0 <= y < grid_h
				
				


def set_seed_tile(arr):
	#position of starting tileoit
	row,col = random.randint(0,len(arr)-1), random.randint(0,len(arr[0])-1)
	#giving an initial value a random integer within our dictionary to represent a starting tile
	val = random.randint(1, len(options))
	#print(val,'\n',row,col
	arr[row][col] = val
	return row, col



def display(arr):
	h=''
	for i in arr:
		for j in i:
				h = h +  colors[j]
		h = h + '\n'
	print(h)
	

	
def flood_fill_collapse(arr, row, col):
	w = len(arr[0])
	h = len(arr)
	#direction vectors in array
	#[up,right,down,left]
	x_vectors = [0,-1,0,1]
	y_vectors = [-1,0,1,0]
	#queue
	t = 0
	visited = []
	kyu = []
	kyu.append([row,col])
	
	while kyu:
		cur = kyu.pop(0)
		
		if in_bounds(cur[1],cur[0],w,h) and  [cur[0],cur[1]] not in visited:
			cur_value = arr[cur[0]][cur[1]]
			
			visited.append([cur[0],cur[1]])
			t += 1
			
			
			
			#possible future values of X and Y depening on position
			possibilities = []
			
			
			for i in range(len(x_vectors)):
				y = cur[0] + y_vectors[i]
				x = cur[1] + x_vectors[i]
				
				
				if in_bounds(x,y,w,h):
					neighbor = arr[y][x]
					if neighbor != blank_cell:
						possibilities.append(options[arr[y][x]])
					
				
			
			
			
			choice = 0
			#print(possibilities)
			
			if len(possibilities) > 1:
				
				
				#using set
				shared = set(possibilities[0])
				#print(shared)
				for arrays in possibilities:
					#set intersection
					#only keeps the shared elements 
					shared = shared & set(arrays)
				possibilities = list(shared)
				'''
				#using dictionary
				shared = {}
				common = []
				for arrays in possibilities:
					for ele in arrays:
						if shared.get(ele):
							shared[ele] += 1
						else:
							shared.update({ele:1})
				for key in shared:
					if shared[key] == len(possibilities):
						common.append(key)
						
				print(common)
				possibilities = common
				'''
						
				
				
				
				choice = random.randint(0,len(possibilities) - 1)
				print("yep")
				
				
				arr[cur[0]][cur[1]] = possibilities[choice]
				
					
				
				
			elif len(possibilities) == 1:
				#options[arr[cur[0]][cur[1]]]
				
				choice = random.randint(0,len(possibilities) - 1)
				
				possibilities = possibilities[choice]
				
				choice = random.randint(0,len(possibilities) - 1)
					
				print("neo")
				arr[cur[0]][cur[1]] = possibilities[choice]
			
			
			kyu.append([cur[0] + 1, cur[1]])
			kyu.append([cur[0] - 1, cur[1]])
			kyu.append([cur[0], cur[1] + 1])
			kyu.append([cur[0], cur[1] - 1])
		#console.clear()
		os.system('cls')
		
		display(arr)
		time.sleep(.15)
	#console.clear()
	os.system('cls')
	
	display(arr)

			
			
def wave_function_collapse(rows,cols):
	arena = empty_map(rows,cols,blank_cell)
	x,y = set_seed_tile(arena)
	flood_fill_collapse(arena,x,y)
	
	#display(arena)
	
wave_function_collapse(18,18)
