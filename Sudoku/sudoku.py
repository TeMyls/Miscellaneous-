import math
import time
import console
import random
import os


floor_color = 0
wall_color = -1
bomb_color = 9
boom_color = 10

colors = {
	
	# wall
	wall_color:'# '
	# floor and ceiling
	#floor_color:'. ',
	#player
	#bomb_color:'ő ',
	
	#boom_color:'X '
	
}

#direction vectors in array
#[up,right,down,left]
#x_vectors = [0,-1,0,1]
#y_vectors = [-1,0,1,0]
# n, ne, e, se, s, sw, w, nw
x_vectors = [0, 1, 1, 1, 0, -1, -1, -1]
y_vectors = [-1, -1, 0, 1, 1, 1, 0, -1]

def empty_map(rows,columns,color):
	return [[color]*columns for i in range(rows)]

def in_bounds(x, y, w, h):
	return -1 < x < w and -1 < y < h
	
def display_board(grid):
	#displays map as numbers
	
	g = "  "
	for row in range(len(grid[0])):
		
		g += str(row%10) + "|"
		
			
		
	print(g)
	
	h=''
	for y in range(len(grid)):
		h += str(y) + "|"
		
		for x in range(len(grid[y])):
			if colors.get(grid[y][x]):
				h += colors[grid[y][x]] 
			else:
				h += str(grid[y][x]) + " "
				
		h = h + '\n'
	print(h + "Y")	
	
	
def display_true(arr):
	h=''
	for i in arr:
		for j in i:
				h = h + str(j) + " "
		h = h + '\n'
	print(h)

		
def clear_console():
		# clearing the console
		
		#on windows
		os.system('cls')
		#on pythonista
		#console.clear()

def animate(wait, grid):
		if wait:
			time.sleep(.05)
		#os.system('cls')
		console.clear()
		display_true(grid)
		
			
			
def quadrant_sweep(grid, x, y, choices):
# Note: in other languages the double slash is equivalent to math.floor(x/n)
	# this chunk sweeps through the 3x3 box of one of the quadrants checking quadrant neighbors
	# sudoku has 3x3 quadrants 
	# below considers 3x3 quadrants
	qx = (x//3) 
	qy = (y//3) 
			
	ox = qx * 3
	oy = qy * 3
	#print(f"X: {x}, Y: {y}, QX: {qx} QY: {qy} ")
	s = ""
	
	a = 0
	while a < 9:
		s = s + " OX: " + str(ox) + " OY: " + str(oy) + " G: " + str(grid[oy][ox])
		s = s + "\n"
		
	
		
		#grid[oy][ox] = x + y
		if grid[oy][ox] in choices:
			choices.remove(grid[oy][ox])
			
		
		
		if (a + 1) % 3 == 0:
			oy += 1
			ox = ox - 3
		
		ox += 1
		a += 1
		
	#print(s)
			
			
			
			
	return choices
	
def cross_sweep(grid, x, y, choices):
	w = 9
	h = 9
	# considers individual rows and columns
	i, j, k, l = y, y, x, x
	# treats the 1D array as a 2D array
	# in lua this would be 1 to 9
	cond = (

			i != 0 or 
			j != h - 1 or
			k != 0 or
			l != w - 1
			
		)
		
	while cond:
		if i != 0:
			i = i - 1
			
		if j != w - 1:
			j = j + 1
			
		if k != 0:
			k = k - 1
			
		if l != h - 1:
			l = l + 1
			
		
		#grid[i][x] = 2
		#grid[j][x] = 4
		
		#grid[y][k] = 1
		#grid[y][l] = 3
			
		# can be replace with indexing a 2D array
		top = grid[i][x]
		
		bottom = grid[j][x]
		
		left = grid[y][k]
		
		right = grid[y][l]
	
		
		if top in choices:
			choices.remove(top)
			
		if bottom in choices:
			choices.remove(bottom)
			
		if left in choices:
			choices.remove(left)
			
		if right in choices:
			choices.remove(right)
		
		#print("x y top bottom left right")
		#print(x, y, top, bottom, left, right)
		#print(i, j, k, l)
		cond = (
			i != 0 or 
			j != h - 1 or
			k != 0 or
			l != w - 1
		)
		
			
	return  choices

def get_sudoku_board():
	"""
					0          1        2		  QX
			 0  1  2    3  4  5   6  7  8	X
			_____________________________
		0	|         |         |        |
	0 1	|         |         |        |                     
		2	|         |         |        |
			|_________|_________|________|     
		3	|         |         |        |
	1 4	|         |         |        |                     
		5	|         |         |        |
			|_________|_________|________|
		6	|         |         |        |
	2 7	|         |         |        |                     
		8	|         |         |        |
			|_________|_________|________|
 QY Y
	"""
	# the nine 3x3 quadrants a sudoku board is made of
	w = 9
	h = 9
	
	
	grid = empty_map(9, 9, 0)
	
	# in lua the minus 1 would be unnecessary
	w = len(grid[0])
	h = len(grid)
	row = random.randint(0, h - 1)
	col = random.randint(0, w - 1)
	#print(row, col, sep = " ")
	
	#iteration tracker
	q = 0
	
	y = 0
	while y < 9:
		x = 0
		restarts = 0
		while x < 9:
			q += 1
			choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
			
			if grid[y][x] in choices:
				choices.remove(grid[y][x])
			
			choices = cross_sweep(grid, x, y, choices)
			
			choices = quadrant_sweep(grid, x, y, choices)
			
			if choices:
				
				grid[y][x] = random.choice(choices)
				x += 1
			else:
				# grid[y][x] is 0, no choice was made
				# erase entire row back to zero
				# mn = x - 2
				while x != 0:
					x -= 1
					grid[y][x] = 0
					
				restarts += 1
				if restarts > 15:
					grid = empty_map(9, 9, 0)
					restarts = 0
					y = 0
			#animate(True, grid)
			#display_true(grid)
		
		y += 1
	

		
		
	display_true(grid)
	print(f"iterations: {q}")
	return grid



def game_loop(chances, shown_cells):
	#if in_bounds(x, y, len(grid[0]), len(grid):
	
	visible_grid = empty_map(9, 9, -1)
	hidden_grid = get_sudoku_board()
	
	#display_board(hidden_grid)
	#display_board(visible_grid)


	uncovered_all = 81 - shown_cells == 0
	mine_neighbors = 0
	
	has_moved = False
	chance_missed = False
	
	all_cells = [
		[y, x] for y in range(len(visible_grid)) for x in range(len(visible_grid[0]))
	]
	
	for i in range(shown_cells):
		rc = random.choice(all_cells)
		visible_grid[rc[0]][rc[1]] = hidden_grid[rc[0]][rc[1]]
		all_cells.remove(rc)
		
	
	while not uncovered_all and chances > 0:
		
		clear_console()
		
		print("hidden grid")
		display_board(hidden_grid)
		
		print("game grid")
		display_board(visible_grid)
		try:
			#print(len(revealed_cells), mine_neighbors)
			
			#x = int(input("Enter an X value: "))
			#y = int(input("Enter an Y value: "))
			if chance_missed:
				print("Incorrect Number")
				chance_missed = False
				
			print(f"Chances Left: {chances}")
			XnYnN = input("Enter an X-Y-N value seperated by a space:")
			x, y, n = list(map(int, XnYnN.split(" ")))
			
			w = len(hidden_grid[0])
			h = len(hidden_grid)
			
			cur_x = math.floor(abs(x % 9))
			cur_y = math.floor(abs(y % 9))
			
			
			if hidden_grid[cur_y][cur_x] == n:
				#clear_console()
				#hidden_grid[cur_y][cur_x] = n
				visible_grid[cur_y][cur_x] = n
				#display_board(visible_grid)
				#display_board(hidden_grid)
				shown_cells += 1
			else:
				chance_missed = True
				chances -= 1
				
			
			
				
			
			
			uncovered_all = 81 - shown_cells == 0
			if uncovered_all:
				clear_console()
				display_board(visible_grid)
				print("You Won")
				
			if chance_missed == chances:
				print("You lost")
				break 
				
		except Exception as e:
			print(e)
			break
		
	if input("Play Again? Y/N?").upper() == "Y":
		
		chances = int(input("Enter a chance count: "))
		if not type(chances) == type(3):
			print("Invalid Chances")
			return
		
		
		game_loop(chances, 8)

game_loop(5, 8)
#get_sudoku_board()
