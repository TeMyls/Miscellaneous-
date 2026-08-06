import random
import math
import time
import console
#import os

filled_color = 1
blank_color = 0


colors = {
	#path
	filled_color:".",
	#floor
	blank_color:"#",
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


def in_bounds(x, y, w, h):
	return -1 < x < w and -1 < y < h

	
def animate(arr):
	#console.clear()
	os.system('cls')
	display(arr)
	time.sleep(.1)

def backtrack_maze(mw, mh):
	maze = empty_map(mh, mw, blank_color)
	# S, W, N, E
	Xs = [0,-1,0,1]
	Ys = [-1,0,1,0]
	
	a = 0
	step = 2
	px = 1
	py = 1
	visited = [[px, py]]
	queue = [[px, py]]
	maze[py][px] = filled_color
	
	while a != mw * mh:
		
		#px, py = queue.pop(0)
		dir_XYs = []
		for i in range(len(Xs)):
			
			nx = px + Xs[i] * step
			ny = py + Ys[i] * step
			
			if not in_bounds(nx, ny, mw, mh):
				continue
				
			if maze[ny][nx] == filled_color:
				continue
				
			dir_XYs.append([Xs[i], Ys[i]])
			if [nx, ny] in visited:
				continue
		

		mx1, my1 = 0, 0
		mx2, my2 = 0, 0
		
		if dir_XYs:
			ex, ey = random.choice(dir_XYs)
			
			
			mx1, my1 = px + ex, py + ey
			mx2, my2 = mx1 + ex, my1 + ey
			
			if maze[my2][mx2] != filled_color:
				
				maze[my1][mx1] = filled_color
				maze[my2][mx2] = filled_color
				
				px, py = mx2, my2
				
				visited.append([mx2, my2])
				#break
			else: 
				if not visited:
					break
				
				px, py = visited.pop()
			
		else: 
			if not visited:
				break
			
			px, py = visited.pop()
		
		
		a += 1
		
		animate(maze)
	display(maze)
	print(a, mw * mh, (mw * mh)/2)
		
	
backtrack_maze(41, 15)