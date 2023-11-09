import random
import time 
#for pythonista
#import console
#outside of pythonista
import os

#0 any: Its the starting 
#it is a blamk cell that can be anything
#1 water
#only boarders sand and itself
#2 sand
#only boarders water,grass and itself
#3 trees
#only boarders grass and itself
#4 dirt
#only boarders trees, sand and itself


options = {1:[1,2],2:[1,2,4],3:[3,4],4:[2,3,4]}



def empty_map(rows,columns,empty_arr):
	for i in range(rows):
		empty_arr.append([0]*columns)
			
	return  empty_arr
			
def cleaner(arr):
   
	for r in range(len(arr)):
		for c in range(len(arr[r])):
			#cardinal directions
			n, nw, w, sw, s, se, e, ne = 0,0,0,0,0,0,0,0
			current = arr[r][c]
			if c > 0:
				w = arr[r][c - 1] 
					
			if c < len(arr[r]) - 1:
				e = arr[r][c + 1] 
			if r > 0:
				n = arr[r - 1][c]
				if c > 0:
					nw = arr[r - 1][c - 1] 
				if c < len(arr[r]) - 1:
					ne = arr[r - 1][c + 1] 
				
			if r < len(arr) - 1:
				s = arr[r + 1][c]
				if c > 0:
					sw = arr[r + 1][c - 1] 
				if c < len(arr[r]) - 1:
					se = arr[r + 1][c + 1] 
			quick_arr = [n, nw, w, sw, s, se, e, ne]	
			if quick_arr.count(1) >= 6:
				arr[r][c] = 1
			if quick_arr.count(4) + quick_arr.count(3) > 5 and current == 2:
				arr[r][c] = 4
				

def set_seed_tile(arr):
	
	#position of starting tileoit
	row,col = random.randint(0,len(arr)-1), random.randint(0,len(arr[0])-1)
	#giving an initial value a random integer within our dictionary to represent a starting tile
	val = random.randint(1, len(options))
	#print(val,'\n',row,col)
	
	arr[row][col] = val
	return row, col

			

def display(arr):
	
	for i in arr:
		print(i)
		

		
	
		
def symbol_display(arr):
	h=''
	for i in arr:
		for j in i:
			
			
			if j == 0:
				h = h + '⬜️'
			if j == 1:
				h = h + '🟦'
			if j == 2:
				h = h +  '🟧'
			if j == 3:
				h = h +  '🟩'
			if j == 4:
				h = h +  '🟫'
			
		h = h + '\n'
	print(h)


def shared(ls1,ls2,ls3 = None,ls4 = None):
	#returns the shared elements of two list
	#for three elemnents
	#why so many loops? 
	#the loops make the weighs matter
	#[1,2,2,2,3] and [2,3] will return
	#[2,2,2,3] instead of [2,3]
	repeats_1 = ls1.count(1) + ls1.count(2) + ls1.count(3) + + ls1.count(4)
	repeats_2 = ls2.count(1) + ls2.count(2) + ls2.count(3) + + ls2.count(4)
	#for two elemnents
	if repeats_1 > repeats_2:
		return [x for x in ls1 if x in ls2]
	elif repeats_1 < repeats_2: 
		return [x for x in ls2 if x in ls1]
	else:
		return [x for x in ls1 if x in ls2]


def restrict(cell_val1, cell_val2 = None):
	#collapse the options based on cell adjency
	#returns a random element from the new list to add to the array
	shared_vals = []
	
	if cell_val2:
		#for two values
		shared_vals = shared(options[cell_val1],options[cell_val2])
		choice = random.randint(0, len(shared_vals) - 1)
		return shared_vals[choice]
	else:
		#for one value
		#just makes a random choice based on the cell value
		#returns random choice
		neighbors = options[cell_val1]
		#print(neighbors)
		choice = random.randint(0,len(neighbors) - 1)
		return options[cell_val1][choice]
		
	
	

	
def flood_fill_collapse(arr, row, col):
	w = len(arr)
	h = len(arr[0])
	#queue
	t = 0
	visited = []
	kyu = []
	kyu.append((row,col))
	while kyu:
		cur = kyu.pop(0)
		if cur[0] >= w or cur[0] < 0 or cur[1] >= h or cur[1] < 0:
			continue
		elif (cur[0],cur[1]) not in visited:
			visited.append((cur[0],cur[1]))
			t += 1
			
			right, left, top, bottom = 0,0,0,0
			if cur[1] > 0:
				right = arr[cur[0]][cur[1] - 1] 
			
			if cur[1] < h - 1:
				left = arr[cur[0]][cur[1] + 1] 
			if cur[0] > 0:
				top = arr[cur[0]  - 1][cur[1]]			
			if cur[0] < w - 1:
			  bottom = arr[cur[0] + 1][cur[1]]
			#print()
						
			#two cells are filled and neighbor is affected
			if right != 0 and bottom == 0 and left == 0 and top != 0:
				arr[cur[0]][cur[1]] = restrict(right,top)
				
			if right != 0 and bottom != 0 and left == 0 and top == 0:
				arr[cur[0]][cur[1]] = restrict(right,bottom)
				
			if right == 0 and bottom == 0 and left != 0 and top != 0:
				arr[cur[0]][cur[1]] = restrict(left,top)
				
			if right == 0 and bottom != 0 and left != 0 and top == 0:
				arr[cur[0]][cur[1]]= restrict(left,bottom)
			#one cell is filled and neighbor is affected
			if right != 0 and bottom == 0 and left == 0 and top == 0:
				arr[cur[0]][cur[1]] = restrict(right)
				
			if right == 0 and bottom != 0 and left == 0 and top == 0:
				arr[cur[0]][cur[1]] = restrict(bottom)
				
			if right == 0 and bottom == 0 and left == 0 and top != 0:
				arr[cur[0]][cur[1]] = restrict(top)
				
			if right == 0 and bottom == 0 and left != 0 and top == 0:
				arr[cur[0]][cur[1]] = restrict(left)
				
			kyu.append((cur[0] + 1, cur[1]))
			kyu.append((cur[0] - 1, cur[1]))
			kyu.append((cur[0], cur[1] + 1))
			kyu.append((cur[0], cur[1] - 1))
			#console.clear()

      
			os.system('cls')
			symbol_display(arr)
			time.sleep(.001)
	#console.clear()
	os.system('cls')
	cleaner(arr)
	symbol_display(arr)
	#print(t)
			
			
def wave_function_collapse(rows,cols):
	arena = empty_map(rows,cols,[])
	x,y = set_seed_tile(arena)
	
	flood_fill_collapse(arena,x,y)
	display(arena)
	#print(arena)
	
wave_function_collapse(20,20)
print("1 is water","2 is sand","3 is tree","4 is dirt", sep = "\n")
