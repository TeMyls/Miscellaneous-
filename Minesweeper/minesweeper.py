import math
import time
import console
import random
#import os


floor_color = 0
wall_color = -1
bomb_color = 9
boom_color = 10

colors = {
	
	# wall
	wall_color:'# ',
	# floor and ceiling
	floor_color:'. ',
	#player
	bomb_color:'ő ',
	
	boom_color:'X '
	
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
	
	

		
def clear_console():
		# clearing the console
		
		#on windows
		#os.system('cls')
		#on pythonista
		console.clear()
		
		
def flood_fill_bfs(grid, row, col):
	w = len(grid[0])
	h = len(grid)
	#BFS flood fill
	#queue
	
	visited = []
	queue = []
	queue.append((row,col))
	while queue:
		#print(kyu)
	
		cur = queue.pop(0)
		
		if not in_bounds(cur[1], cur[0], w, h) or	grid[cur[0]][cur[1]] != wall_color:
			continue
		else:
			visited.append((cur[0], cur[1]))
			grid[cur[0]][cur[1]] = floor_color
			queue.append((cur[0] + 1, cur[1]))
			queue.append((cur[0] - 1, cur[1]))
			queue.append((cur[0], cur[1] + 1))
			queue.append((cur[0], cur[1] - 1))
	return visited
	
def get_valid_cells(grid):
	cells_valid = []
	w = len(grid[0])
	h = len(grid)
	for row in range(h):
		for col in range(w):
			if grid[row][col] == wall_color:
				cells_valid.append([row, col])
	return cells_valid
	
def place_mines(grid, valid_cells, mine_count):
	# placing mines everywhere but the start coordinates
	#print(valid_cells)
	
	while mine_count > 0:
		mine_loc = random.choice(valid_cells)
		valid_cells.remove(mine_loc)
		#print(mine_loc)
		grid[mine_loc[0]][mine_loc[1]] = bomb_color
		
		mine_count = mine_count - 1 
		
def place_numbers(grid, valid_cells):
	
	
	w = len(grid[0])
	h = len(grid)
	
	while valid_cells:
		
		cy, cx = valid_cells.pop()
		if grid[cy][cx] == bomb_color:
			continue
		
		for i in range(len(x_vectors)):
			
			nx = cx + x_vectors[i]
			ny = cy + y_vectors[i]
			if not in_bounds(nx, ny, w, h):
				continue
				
			if grid[ny][nx] == bomb_color:
				
				
				
				# all valid cells start off as the wall color
				if grid[cy][cx] == wall_color:
					
					grid[cy][cx] = 1
					
				else:
					
					grid[cy][cx] += 1

def neighbor_color(cx, cy, color, grid):
	w = len(grid[0])
	h = len(grid)
	grid[cy][cx] = color
	
	for i in range(len(x_vectors)):

		nx = cx + x_vectors[i]
		ny = cy + y_vectors[i]
		if not in_bounds(nx, ny, w, h):
			continue
		
		grid[ny][nx] = color
					
	

def game_loop(board_width, board_height, mine_count):
	#if in_bounds(x, y, len(grid[0]), len(grid):
	
	revealed_cells = set()
	
	visible_grid = empty_map(board_height, board_width, wall_color)
	hidden_grid = empty_map(board_height, board_width, wall_color)
	
	#display_board(hidden_grid)
	#display_board(visible_grid)


	uncovered_all = revealed_cells == board_width * board_height - mine_count
	mine_neighbors = 0
	
	has_moved = False
	
	while not uncovered_all:
		
		clear_console()
		
		#print("hidden grid")
		display_board(hidden_grid)
		
		print("game grid")
		display_board(visible_grid)
		try:
			#print(len(revealed_cells), mine_neighbors)
			
			#x = int(input("Enter an X value: "))
			#y = int(input("Enter an Y value: "))
			XnY = input("Enter an X-Y value seperated by a space:")
			x, y = list(map(int, XnY.split(" ")))
			
			w = len(hidden_grid[0])
			h = len(hidden_grid)
			
			cur_x = math.floor(abs(x % board_width))
			cur_y = math.floor(abs(y % board_height))
			
			if not has_moved:
				
				
				
				neighbor_color(cur_x, cur_y, floor_color, hidden_grid)
				#hidden_grid[cur_y][cur_x] = floor_color
				
				wall_cells = get_valid_cells(hidden_grid)
				place_mines(hidden_grid, wall_cells, mine_count)
				place_numbers(hidden_grid, wall_cells)
				
				#print(valid_cells)
				#valid_cells.append([y, x])
				
				neighbor_color(cur_x, cur_y, wall_color, hidden_grid)
				place_numbers(hidden_grid, wall_cells)
				#hidden_grid[cur_y][cur_x] = wall_color
				
				has_moved = True
			
				for y in range(len(hidden_grid)):
					for x in range(len(hidden_grid[y])):
						if not colors.get(hidden_grid[y][x]):
							mine_neighbors += 1
				
			if hidden_grid[cur_y][cur_x] == bomb_color:
				clear_console()
				hidden_grid[cur_y][cur_x] = boom_color
				
				display_board(hidden_grid)
				#display_board(hidden_grid)
				print("touched mine")
				break
			
			if hidden_grid[cur_y][cur_x] == wall_color:
				changed_cells = flood_fill_bfs(hidden_grid, cur_y, cur_x)
				while changed_cells:
					_y, _x = changed_cells.pop()
					visible_grid[_y][_x] = hidden_grid[_y][_x]
					
			else:
				visible_grid[cur_y][cur_x] =  hidden_grid[cur_y][cur_x]
				
				if not colors.get(hidden_grid[cur_y][cur_x]):
					coord_xy = str(cur_x) + "-" + str(cur_y)
					revealed_cells.add(coord_xy)
				
			
			
			uncovered_all = len(revealed_cells) == mine_neighbors 
			if uncovered_all:
				clear_console()
				display_board(visible_grid)
				print("You Won")
		
		except:
			print("Error")
			break
		
	if input("Play Again? Y/N?").upper() == "Y":
		board_custom = input("Customize Board Size? Y/N? ").upper()
		if board_custom == "Y":
			WnH = input("Enter a Width-Height value seperated by a space: ")
			w, h = WnH.split(" ")
			if not w.isnumeric() or not h.isnumeric():
				print("Invalid Number")
				return
			
			
			board_width, board_height = abs(int(w)), abs(int(h))
				
		mine_custom = input("Customize Mine Count\n(Can't be more than a 1/5th of the the area?)\n Y/N? ").upper()
		if mine_count == "Y":
			count_mines = input("Enter a mine count: ")
			if not count_mines.isnumeric():
				print("Invalid Number")
				return
			
			mine_count = abs(int(count_mines))
		game_loop(board_width, board_height, mine_count)

game_loop(16, 10, 16)

