import math

floor = lambda x: round(x)

floor_color = 1

wall_color = 0
player_color = 7
other_color = 9

colors = {
	#wall
	wall_color:'.',
	#floor
	floor_color:'#',
	#player
	player_color:'@',
	other_color:'X'

	
	
}

def empty_map(rows,columns,color):
	return [[color]*columns for i in range(rows)]

def symbol_display(arr):
	#displays map in readable format
	h=''
	for row in arr:
		for col in row:
			h += colors[col]
		h = h + '\n'
	print(h)

def in_bounds(x, y,grid_w,grid_h):
    return 0 <= x < grid_w and 0 <= y < grid_h 

def clamp(x, lower, upper):
	if x < lower:
		return lower
	elif x > upper:
		return upper
		
	else:
		return x

def lerp(a, b, percentage):
	return a + (b - a) * clamp(percentage, 0, 1)
	

def r_bez(point_ls: list[float], points: [int], point: int) -> list[float]:
	# the way bezier curves work is by linear interpolating(lerp)
		# the value from one coordinate to another, getting a percentage between the two
		# these points are lerp-ed until the path of a single line is deduced
	# 4 X-Y coordinate pairs have 3 lines between them
	# when a value is connected inbetween these 3 lines sequentially you get 2 lines, then 1 line fron where each point on the found
	# this recurcise and iterative versions do exactly that, once the amount of points is reduced to 4 numbers, 2 X-Y pairs, a line
			# the curve's coordinate at that percentage is found
			
	ln = len(point_ls)
	#print(point_ls)
	if ln == 4:
		x1 = point_ls[0]
		y1 = point_ls[1]
		
		x2 = point_ls[2]
		y2 = point_ls[3]
	
		#print(x1, y1, x2, y2)
		
		x = lerp(x1, x2, point/points)
		y = lerp(y1, y2, point/points)
			
		return [x , y]
				
	if ln < 6:
		return

	ls_point = []
	for i in range(3, ln, 2):
		
		x1 = point_ls[i - 3]
		y1 = point_ls[i - 2]
		
		x2 = point_ls[i - 1]
		y2 = point_ls[i]
	
		#print(x1, y1, x2, y2)
		ls_point.append(
			lerp(x1, x2, point/points)
			)
		ls_point.append(
			lerp(y1, y2, point/points)
			)

	return r_bez(ls_point, points, point)
	
def i_bez(point_ls: list[float], points: [int], point: int) -> list[float]:
	
	ln = len(point_ls)
	
	if ln < 6:
		return
	
	ls_point = [coord for coord in point_ls]
	while len(ls_point) != 4:
		ln = len(ls_point)
		i = 3 
		while i < ln:
		#for i in range(3, ln, 2):
		
			x1 = ls_point[i - 3]
			y1 = ls_point[i - 2]
			
			x2 = ls_point[i - 1]
			y2 = ls_point[i]
		
			#print(x1, y1, x2, y2)
			ls_point.append(
				lerp(x1, x2, point/points)
				)
			ls_point.append(
				lerp(y1, y2, point/points)
				)
			i += 2
			
		ls_point = ls_point[ln:ln + i]
		#print(len(ls_point))
		#if len(ls_point) == 4:
			#return ls_point
	x1 = ls_point[0]
	y1 = ls_point[1]
	
	x2 = ls_point[2]
	y2 = ls_point[3]

	#print(x1, y1, x2, y2)
	
	x = lerp(x1, x2, point/points)
	y = lerp(y1, y2, point/points)
	return [x , y]

		
		
grid = empty_map(22, 22, wall_color)
w = len(grid[0]) - 1
h = len(grid) - 1
points = 10
coords = [
			#X 									Y
			0									, 0, 
			floor(w  * 0.20)	,floor(h * .80), 
			floor(w  * 0.65)	,floor(h * .20), 
			floor(w  * 0.90)	,floor(h * .75)
		]
#curve = n_curve_bezier(points, 8)

for i in range(points):
	curve = r_bez(coords, points, i)
	
	x = floor(curve[0])
	y = floor(curve[1])
	
	grid[y][x] = floor_color
	print(curve)

#symbol_display(grid)

for i in range(0, len(coords), 2):
		x = floor(coords[i])
		y = floor(coords[i + 1])
		
		grid[y][x] = player_color

symbol_display(grid)
print(len(curve))

