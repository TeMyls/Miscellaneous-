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
		
		


def get_faux2D(array, row, col, rows, cols):
	#indexing a 1D array as if it were a 2D array
	return array[(row % rows) * cols + (col % cols)]
	
def set_faux2D(array, row, col, rows, cols, value):
	#indexing a 1D array as if it were a 2D array
	array[(row % rows) * cols + (col % cols)] = value
	return array
	
def show_faux(array, rows, cols):
	s = ""
	for y in range(rows):
		
		for x in range(cols):
			s += str(get_faux2D(array, y, x, rows, cols)) + " "
		s += "\n"
	return s
	
	
def get_sudoku_board():
	"""
	# in lua add 1 to all
	_____________________________
	|0  1  2  |3  4  5  |6  7  8 |
	|9  10 11 |12 13 14 |15 16 17|                     
	|18 19 20 |21 22 23 |24 25 26|
	|_________|_________|________|     
	|27 28 29 |30 31 32 |33 34 35|
	|36 37 38 |39 40 41 |42 43 44|
	|45 46 47 |48 49 50 |51 52 53|
	|_________|_________|________|
	|54 55 56 |57 58 59 |60 61 62|
	|63 64 65 |66 67 68 |69 70 71|
	|72 73 74 |75 76 77 |78 79 80|
	|_________|_________|________|
	"""
	# the nine 3x3 quadrants a sudoku board is made of
	w = 9
	h = 9
	
	region_test = [
		j for j in range(w * h) 
	]
	
	board = [
		0 for j in range(w * h) 
	]
	#print(show_faux(region_test, w, h))
	#print(len(region_test))
	quads = [
		0, 3, 6,
		27, 30, 33,
		54, 57, 60,
	]
	
	
	
	
	
	grid = empty_map(9, 9, 0)
	
	# in lua the minus 1 would be unnecessary
	w = len(grid[0])
	h = len(grid)
	row = random.randint(0, h - 1)
	col = random.randint(0, w - 1)
	#print(row, col, sep = " ")
	
			
	for y in range(h):
		for x in range(w):
			choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
			# Note: in other languages the double slash is equivalent to math.floor(x/n)
			# sudoku has 3x3 quadrants 
			# in this case I alternate between indexing the array as a 2D arry and a 1D array
			# below considers 3x3 quadrants
			qx = x//3
			qy = y//3
			
			idx = qx * 3 + qy * 27
			
			ox = qx * 3
			oy = qy * 3
			
			
			#print(qx * 3, qy * 3)
			s_1 = ""
			s_2 = "" #f"OX:{ox} OY:{oy} "
			
			a = 0
			while a < 9:
				# offset by itself only outputs the
				# first 3x3 quadrant
				# 0  1  2
				# 9  10 11
				# 18 19 20
				# using idx it gets the correct position of indexing in a 1D array
				offset = ((a//3) * 9) + a % 3
				
				s_2 += str(get_faux2D(board, oy, ox, h, w)) + " "
				
				#if board[idx + offset] in choices:
					#choices.remove(board[idx + offset])
				
				if get_faux2D(board, oy, ox, h, w) in choices:
					#choices.remove(get_faux2D(board, oy, ox, h, w))
					choices.remove(grid[oy][ox])
				
				#grid[oy][ox] = 8
				# for 2D arrays
				ox += 1
				if (a + 1) % 3 == 0:
					oy += 1
					ox = qx * 3
				
				#print(f"OX:{ox} OY:{oy} ")
				
				
				
				
					
				s_1 += str(idx + offset) + " "
				
				if (a + 1) % 3 == 0:
					s_1 += "\n"
					s_2 += "\n"
				#print(offset)
				a += 1
			#print(s_1)
			#print(s_2)
			
		
			
			
			#print(x, y, qx, qy, offset)
			
			
			
			
			
			
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
				#get_faux2D(board, i, x, h, w)
				bottom = grid[j][x]
				#get_faux2D(board, j, x, h, w)
				left = grid[y][k]
				#get_faux2D(board, y, k, h, w)
				right = grid[y][l]
				get_faux2D(board, y, l, h, w)
				
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
				
			#print(choices, y, x)
			if choices:
				#set_faux2D(board, y, x, h, w, random.choice(choices))
				grid[y][x] = random.choice(choices)
			#break
		#break

		
	display_true(grid)
	#print(show_faux(board, w, h))
	#BFS flood fill
	#queue
	
	#display_true(grid)
	return grid


def game_loop(chances, shown_cells):
	#if in_bounds(x, y, len(grid[0]), len(grid):
	
	revealed_cells = shown_cells
	
	visible_grid = empty_map(9, 9, -1)
	hidden_grid = get_sudoku_board()
	
	#display_board(hidden_grid)
	#display_board(visible_grid)


	uncovered_all = revealed_cells == 9 * 9 
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
				revealed_cells += 1
			else:
				chance_missed = True
				chances -= 1
				
			
			
				
			
			
			uncovered_all = revealed_cells == mine_neighbors 
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
		if not type(chances) == type("chance"):
			print("Invalid Chances")
			return
		
		chances = abs(int(chances))
		game_loop(chances, 80)

game_loop(5, 80)
#get_sudoku_board()
