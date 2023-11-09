import random
import time 
#for pythonista
#import console
#outside of pythonista
import os

def empty_map(rows,columns,empty_arr):
	for i in range(rows):
		empty_arr.append([0]*columns)
			
	return  empty_arr
	
	
def symbol_display(arr):
	h=''
	for i in arr:
		for j in i:
			
			if j == 0:
				h = h + '⬜️'
			if j == 1:
				h = h +  '🟥'
			
		h = h + '\n'
	print(h)



def random_direction(arr,y,x,visited):
	w = len(arr[0])
	h = len(arr)
	#direction vectors in array
	#[up,right,down,left]
	#x_vectors = [0,1,0,-1]
	#y_vectors = [-1,0,1,0]
	#by editing  you can bias the generation
	x_vectors = [0,0,0,1,1,0,-1,-1,-1]
	y_vectors = [-1,-1,-1,0,0,1,0,0,0]
	
	#possible future values of X and Y depening on position
	possible_Xs = []
	possible_Ys = []
	#original X and Y
	og_x = x
	og_y = y
	for i in range(len(x_vectors)):
		y = og_y + y_vectors[i]
		x = og_x + x_vectors[i]
		if x >= w or x < 0 or y >= h or y < 0:
			continue
		else:
			#0 is the blank tile
			#Adding it to the Possble Array means it will be filled
			if arr[y][x] == 0:
				
				possible_Xs.append(x)
				possible_Ys.append(y)
	#C
	choice = 0
	if len(possible_Xs) > 0:
		choice = random.randint(0,len(possible_Xs) - 1)
	else:
		if len(visited) != 0:
			coords = visited.pop(0)
			return random_direction(arr,coords[0],coords[1],visited)
		
		
		 
	return possible_Ys[choice],possible_Xs[choice]
def random_walk(arr,y,x,steps):
	visited = []
	arr[y][x] = 1
	symbol_display(arr)
	while steps != 0:
		
		y,x = random_direction(arr,y,x,visited)
		visited.append([y,x])
		steps = steps - 1
		arr[y][x] = 1
		
		#console.clear()
		os.system('cls')
		symbol_display(arr)
		time.sleep(.015)
		#symbol_display(arr)
	#symbol_display(arr)	
		
		
	
	
	
	


			
			
			
arr = empty_map(40,40,[])	
random_walk(arr,27,33,500)
