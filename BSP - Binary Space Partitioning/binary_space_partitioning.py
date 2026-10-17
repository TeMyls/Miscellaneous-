import math 
import random

floor_color = 1
unknown_color = 2
wall_color = 0
player_color = 7
enemy_color = 9
up_stairs_color = 8
down_stairs_color = 6


#these can be anything but the wall color
visited_color = 1


colors = {

	wall_color:'#',
	floor_color:'.',
	#player_color:'@',
	#unknown_color:'?',
	#up_stairs_color:'>',
	#enemy_color: 'V',
	#down_stairs_color:'<'
	
	
	
}

def clamp(value, upper, lower):
	return math.max(lower, math.min(value, upper))
	
def lerp(a, b, percentage):
	return a + (b - a) * percentage
	
def distance_to(x1, y1, x2, y2):
	return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
	
def angle_to(x1, y1, x2, y2):
	return math.atan2(y2 - y1, x2 - x1)
	
def degrees_to_radians(degrees):
	return (degrees * math.pi)/180		
		
def radians_to_degrees(radians):
	return  radians * 180/math.pi
	
def create_2D_array(rows,columns,color):
	return [[color]*columns for i in range(rows)]

def rand_choice(arr, weight_ls, k):
	return random.choices(arr,weights = weight_ls,k = k)

def flatten(list_of_lists):
	return [ele for ls in list_of_lists for ele in ls]

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



def BSP(grid, splits):
	#This fuction splits a two dimensional array into a bunch of small squares
	#x0,y1,w2,h3
	#arr is the map size represented by x, y, w,h
	
	#width is the with of the map size
	#height is the height of th map soze

	#splits is how many box exists
	
	gx1 = 0
	gy1 = 0
	gx2 = len(grid[0])
	gy2 = len(grid)
	areas = [
		[
			gx1,
			gy1,
			gx2,
			gy2
		]
	]
	
	
	while len(areas) != splits:
		#print(areas)
		#print()
		
		
		
		rand = int(random.random() * 2)
		
		area = areas.pop(0)
		gx1 = area[0]
		gy1 = area[1]
		gx2 = area[2]		
		gy2 = area[3]
		ratio_wh = (gx2 - gx1)/(gy2 - gy1)
		
		if ratio_wh > 1:
			new_x = math.floor(
				lerp(
					gx1,
					gx2,
					random.randint(35, 75)/100
				)
			)
			
			
			
			child_1 = [
				new_x,
				gy1,
				gx2,
				gy2
			]
			
			child_2 = [
				gx1,
				gy1,
				new_x,
				gy2
			]
			
			if rand > 0.5:
				areas.append(child_2)
				areas.append(child_1)
			else:
				
				areas.append(child_1)
				areas.append(child_2)
			
		else:
			new_y = math.floor(
				lerp(
					gy1,
					gy2,
					random.randint(35, 75)/100
				)
			)
			
			
			
			child_1 = [
				gx1,
				new_y,
				gx2,
				gy2
			]
			
			child_2 = [
				gx1,
				gy1,
				gx2,
				new_y 
			]
			
			if rand > 0.5:
				areas.append(child_2)
				areas.append(child_1)
			else:
				
				areas.append(child_1)
				areas.append(child_2)
				
	for area in areas:
		x1 = area[0]
		y1 = area[1]
		x2 = area[2]
		y2 = area[3]
		print(area)
		#print(x,y,w,h,sep='_')
		for row in range(y1, y2):
			for col in range(x1, x2):
				#arr[row][col] = 1
				
				if col == x1 or col == x2:
					grid[row][col] = wall_color
				elif row == y1 or row == y2:
					grid[row][col] = wall_color
				else:
					grid[row][col] = floor_color
					
	return grid

grid = create_2D_array(20, 40, wall_color)				
BSP(grid, 8)
display(grid)
			
	
				
				