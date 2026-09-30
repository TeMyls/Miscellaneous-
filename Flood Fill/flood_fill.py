import math
import random
import os
import console
import time

floor_color = 1
fill_color = 3

colors = {

	floor_color:'⬜️',
	fill_color: '🟥'
	
}
	
def create_2D_array(rows,columns,color):
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
	


def flood_fill(grid: list[list[int]], x: int, y: int, is_bfs: bool):
	
	deque = [[x, y]]
	visited = []
	w = len(grid[0])
	h = len(grid)
	#direction vectors in array
	#[up,right,down,left]
	x_vectors = [0,-1,0,1]
	y_vectors = [-1,0,1,0]
	
	while deque:
		# dfs is scanline fill
		# bfs is flood fill
		cell = deque.pop(0) if is_bfs else deque.pop()
		if not in_bounds(cell[0], cell[1], w, h):
			continue
		
		if cell in visited:
			continue
			
		grid[cell[1]][cell[0]] = fill_color
		visited.append(cell)
			
		for i in range(len(x_vectors)):
			nx = cell[0] + x_vectors[i]
			ny = cell[1] + y_vectors[i]
			
			if not in_bounds(nx, ny, w, h):
				continue
				
			
			deque.append([nx, ny])
			
		# for pythonista
		console.clear()
		
		# for windows
		#os.system('cls')
		
		display(grid)
		time.sleep(.05)
			
		
	
grid = create_2D_array(12, 12, floor_color)
w = len(grid[0])
h = len(grid)
rx = random.randint(0, w - 1)
ry = random.randint(0, h - 1)
flood_fill(grid, rx, ry, True)


