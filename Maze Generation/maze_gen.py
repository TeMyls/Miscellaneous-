import random
import math
import time
#import console
import os
#from array_raycast import *


filled_color = 1
blank_color = 0


colors = {
	#wall
	filled_color:'. ',
	#floor
	blank_color:'# ',
}


		

def display(arr):
	#displays map in readable format
	h=''
	for row in arr:
		for col in row:
			h += colors[col] 
		h = h + '\n'
	print(h)

def empty_map(rows,cols, color):		
	return [[color]*cols for i in range(rows)]


def coord_to_str(x,y):
	return str(x) + "-" + str(y)
	
def str_to_coord(string):
	return list(map(int,string.split('-')))
	
def is_invalid(arr2d,x,y,visited):
	return x > len(arr2d[0]) - 1 or x < 0 or y > len(arr2d) - 1 or y < 0 or [x, y] in visited
	
def fill_walls(array_2d,color):
	w = len(array_2d[0])
	h = len(array_2d)
	array_2d[0] = [color] * w 
	array_2d[h - 1] = [color] * w 
	for i in range(w):
		array_2d[i][0] = color
		array_2d[i][w - 1] = color
	
def double(x):
	return x * 2

def animate(arr):
    #console.clear()
	os.system('cls')
	display(arr)
	time.sleep(.07)


def random_walker_maze_gen(array_2d,array_2d2):
	w = len(array_2d[0])
	h = len(array_2d)
	og_x = 0
	og_y = 0
	
	#tree = {coord_to_str(og_x,og_y):[None]}
	
	x_vectors = [0,-1,0,1]
	y_vectors = [-1,0,1,0]
	
	og_x_vectors = x_vectors.copy()
	og_y_vectors = y_vectors.copy()
	
	cur_dir_x = 0
	cur_dir_y = 0
	
	visited = [[og_x,og_y]]
	walls = []
	directions = []
	array_2d[og_y][og_x] = filled_color
	display(array_2d)
	
	choice = 0
	coords = []
	#walls
	'''
	
	'''
	
	#smaller first
	while len(visited) != w * h :
		
		backtracking = False
		
		#possible future values of X and Y depening on position
		possible_Xs = []
		possible_Ys = []
		#original X and Y
		
		
			
		
		for i in range(len(x_vectors)):
			y = og_y + y_vectors[i]
			x = og_x + x_vectors[i]
			if is_invalid(array_2d,x,y,visited):
				continue
			else:
				#0 is the blank tile
				#Adding it to the Possble Array means it can filled
				#if x%2 != 0 and y%2 != 0:
					
				possible_Xs.append(x)
				possible_Ys.append(y)
			
		#by making the choice zero or the array lenght its possible to make the walker stick to walls
		
		if len(possible_Xs) > 0:
			choice = random.randint(0,len(possible_Xs) - 1)
			#choice = 0
		else:
			if len(visited) != 0:
				coords = visited.pop(0)
					
		nu_x = 0
		nu_y = 0
		if coords:
			nu_x = coords[0]
			nu_y = coords[1]
		else:
			nu_x = possible_Xs[choice]	
			nu_y = possible_Ys[choice]
			
		
		cur_dir_x = nu_x - og_x 
		cur_dir_y = nu_y - og_y 
				
		og_x = nu_x
		og_y = nu_y
			
		array_2d[nu_y][nu_x] = filled_color
		directions.append([cur_dir_x,cur_dir_y])
		directions.append([cur_dir_x,cur_dir_y])
		
		
		if [nu_x,nu_y] not in visited:
			visited.append([nu_x,nu_y])
			
			
		animate(array_2d)
		possible_Xs.clear()
		possible_Ys.clear()
		coords.clear()
		choice = 0
		
	cur_x = 1
	cur_y = 1
	while directions:
		dir = directions.pop(0)
		array_2d2[cur_y][cur_x] = filled_color
		
		cur_x += dir[0]
		cur_y += dir[1]

		animate(array_2d2)
	
	#print(walls)
	display(array_2d2)
	
	
	return array_2d2
	

def make_maze(maze_w,maze_h):

	arr = empty_map(maze_h//2,maze_w//2,blank_color)
	big_arr = empty_map(maze_h + 1,maze_w + 1,blank_color)

	random_walker_maze_gen(arr,big_arr)
	

	
	
	 
	
	
	
#random_walker_gen_maze(10, 10)	
make_maze(16,16)


