import math
import random

floor_color = 1
unknown_color = 2
wall_color = 0
player_color = 7
up_stairs_color = 8
down_stairs_color = 6


#these can be anything but the wall color
visited_color = 1
traceback_color = 5
goal_color = 10
start_color = 3

def empty_map(rows,columns,empty_arr):
	for i in range(rows):
		empty_arr.append([wall_color]*columns)
			
	return  empty_arr

def symbol_display(arr):
	#displays map in readable format
	h=''
	for row in arr:
		for col in row:
			if col == wall_color:
				h = h + '# '
			elif col == floor_color:
				h = h + '. '
			elif col == unknown_color:
				h = h + '? '
			elif col == player_color:
				h = h + '@ '
			elif col == up_stairs_color:
				h = h + 'u '
			elif col == down_stairs_color:
				h = h + 'd '
			else:
				h = h + '.'
			
		h = h + '\n'
	print(h)



def DDA(x0, y0, x1, y1): 

	# find absolute differences 
	dx = x1 - x0
	dy = y1 - y0
	# find maximum difference 
	
	
	steps = 0
	
	if abs(dx) >= abs(dy):
		steps = abs(dx)
	else:
		steps = abs(dy)
		
	
	# calculate the increment in x and y 
	xinc = dx/steps 
	yinc = dy/steps 

	# start with 1st point 
	x = x0
	y = y0
	# make a list for coordinates 
	coorinates = [] 

	coorinates.append([x, y]) 
	for i in range(steps): 
		
		
		
		# increment the values 
		x = x + xinc 
		y = y + yinc 
		
		# append the x,y coordinates in respective list 
		coorinates.append([math.floor(x), math.floor(y)]) 
		
	return coorinates
	
def DDA_raycast(grid, x0, y0, x1, y1, max_dist): 

	# find absolute differences 
	dx = abs(x0 - x1) 
	dy = abs(y0 - y1) 
	# find maximum difference 
	steps = max(dx, dy) 

	# calculate the increment in x and y 
	x_inc = dx/steps 
	y_inc = dy/steps 

	# start with 1st point 
	x = float(x0) 
	y = float(y0) 
	# make a list for coordinates 
	coorinates = [] 
	
	og_tile = grid[math.floor(y)][math.floor(x)]
	cur_tile = og_tile
	valid_tile = floor_color 
	while cur_tile == og_tile or cur_tile == valid_tile:
		
		
		
		x = x + x_inc 
		y = y + y_inc 
		total_dist = math.sqrt(math.pow((x0 - x),2) +  math.pow((y0 - y),2))
		cur_tile = grid[math.floor(y)][math.floor(x)]
		
		if total_dist >= max_dist:
			break
		
	
	
		# append the x,y coordinates in respective list 
		#coorinates.append([x, y]) 
		# increment the values 
		
	#return coorinates

def bresenham_circle(x0, y0, radius):
	x = radius
	y = 0
	err = 3 - 2 * radius
	#5 / 4 - radius
	#3 - 2 * radius

	points = []

	while x >= y:
		points.append((x0 + x, y0 + y))
		points.append((x0 + y, y0 + x))
		points.append((x0 - y, y0 + x))
		points.append((x0 - x, y0 + y))
		points.append((x0 - x, y0 - y))
		points.append((x0 - y, y0 - x))
		points.append((x0 + y, y0 - x))
		points.append((x0 + x, y0 - y))

		y += 1
		err += 1 + 2 * y
		if 2*(err-x) + 1 > 0:
			x -= 1
			err += 1 - 2 * x

	return points

				
		
			
def bresenham_line(start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
	"""Return a list of coordinates from `start` to `end` including both endpoints.

	This implementation is symmetrical. It uses the same set of coordinates in either direction.

	>>> bresenham_line((0, 0), (3, 4))
	[(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
	>>> bresenham_line((3, 4), (0, 0))
	[(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
	"""
	# Setup initial conditions
	x1, y1 = start
	x2, y2 = end
	dx = x2 - x1
	dy = y2 - y1

	# Determine how steep the line is
	is_steep = abs(dy) > abs(dx)

	# Rotate line
	if is_steep:
		x1, y1 = y1, x1
		x2, y2 = y2, x2

	# Swap start and end points if necessary and store swap state
	swapped = False
	if x1 > x2:
		x1, x2 = x2, x1
		y1, y2 = y2, y1
		swapped = True

	# Recalculate differentials
	dx = x2 - x1
	dy = y2 - y1

	# Calculate error
	error = dx // 2
	ystep = 1 if y1 < y2 else -1

	# Iterate over bounding box generating points between start and end
	y = y1
	points = []
	for x in range(x1, x2 + 1):
		coord = (y, x) if is_steep else (x, y)
		points.append(coord)
		error -= abs(dy)
		if error < 0:
			y += ystep
			error += dx

	# Reverse the list if the coordinates were swapped
	if swapped:
		points.reverse()
	return points
	
blank = empty_map(10,10,[])
possible_tiles = []
for y in range(len(blank) - 1):
	for x in range(len(blank[y])):
		possible_tiles.append([x,y])

pair = random.choice(possible_tiles)
possible_tiles.remove(pair)
rx1, ry1 = pair[0], pair[1]

pair = random.choice(possible_tiles) 
possible_tiles.remove(pair)
rx2, ry2 = pair[0], pair[1]

blank[ry1][rx1] = floor_color
blank[ry2][rx2] = floor_color

symbol_display(blank)
between = DDA(rx1,ry1,rx2,ry2)
print(rx1," ",ry1,"\n",rx2," ", ry2)
for coords in between: 
	print(coords)
	blank[coords[1]][coords[0]] = floor_color
	
symbol_display(blank)

#rx, ry = pair1[0], pair1[1]
#print(rx," ",ry)
#print(possible_tiles)
#rx1, ry1 = blank
