import random
import math
import time
import typing
#import console
#from procgenmap import *
import os




known_tiles = []

floor_color = 1

wall_color = 0
player_color = 7
d_stair_color = 2

#ASCII_brightness = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
ASCII_brightness = "WM#*zcvu-_+^'"
#ASCII_brightness = "WMzc+:'"
print(ASCII_brightness)


colors = {
	#wall
	wall_color:'#',
	#floor
	floor_color:'.',
	#player
	player_color:'@'
	
	
}



#the can be anything but the wall color
visited_color = 1
traceback_color = 5
goal_color = 10
start_color = 3



def empty_map(rows,columns,color):
	
	
			
	return [[color]*columns for i in range(rows)]


def in_bounds(x, y,grid_w,grid_h):
		return 0 <= x < grid_w and 0 <= y < grid_h 


			
		
		

def symbol_display(arr):
	#displays map in readable format
	h=''
	for row in arr:
		for col in row:
			h += colors[col] 
			
			
		h = h + '\n'
	print(h)
	
def dual_map_display(display_grid, map_grid, list_hits,show_display,show_map):
	#the only reason this function works is because both maps are the same height
	display_string = ""
	for i in range(len(display_grid)):
		if show_display:	
			for j in range(len(display_grid[i])):
				if colors.get(display_grid[i][j]):
					
					display_string += colors[display_grid[i][j]]
				else:
					
					
					display_string += str(display_grid[i][j])
		if show_map:
			for j in range(len(map_grid[i])):
				if [i , j] in list_hits:
					display_string += "o"
				elif colors.get(map_grid[i][j]):
					display_string += colors[map_grid[i][j]]
				else:
					display_string += str(map_grid[i][j])
					
		display_string += "\n" 
	print(display_string)

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
	
	


	
def DDA_raycast(grid, x0, y0,step_x,step_y): 

	
	# calculate the increment in x and y 
	xinc = step_x
	yinc = step_y

	# start with 1st point 
	x = x0
	y = y0
	# make a list for coordinates 
	coorinates = [] 

	coorinates.append([x, y]) 
	
	og_tile = grid[math.floor(y)][math.floor(x)]
	cur_tile = og_tile
	valid_tiles = [floor_color, d_stair_color]
	total_dist = 0
	while cur_tile == og_tile or cur_tile in valid_tiles:
		
		
		
		x = x + xinc 
		y = y + yinc 
		if in_bounds(x,y,len(grid[0]),len(grid)):
			cur_tile = grid[math.floor(y)][math.floor(x)]
		else:
			total_dist = math.sqrt(math.pow((x0 - x),2) +  math.pow((y0 - y),2))
			return [total_dist,[math.floor(y), math.floor(x)]]
		
		if cur_tile == wall_color:
			total_dist = math.sqrt(math.pow((x0 - x),2) +  math.pow((y0 - y),2))
			return [total_dist,[math.floor(y), math.floor(x)]]
		
			
		
	
	
		# append the x,y coordinates in respective list 
		#coorinates.append([x, y]) 
		# increment the values 
		
	#return coorinates
	
def degrees_to_radians(deg):
	return (deg * math.pi)/180
	
def ray_angles(ray_count,fov,x0,y0):
	space_per_ray = degrees_to_radians(fov/ray_count)
	ray_angle = -degrees_to_radians(fov/2)
	fov_angles = []
	fov_angles.append(ray_angle)
	for i in range(ray_count):
		
		ray_angle = ray_angle + space_per_ray
		fov_angles.append(ray_angle)
	return fov_angles
	
def draw_vertical_line(grid,x,color,size):
	y = 0
	if in_bounds(x,y,len(grid[0]),len(grid)):
		#start y
		y = round((len(grid) - size)/2)
		end_y = len(grid) - y
		while y < end_y:
			grid[y][x] = color
			y = y + 1	
	
def render_floors(x,display_grid,map_grid,wall_height,angle_ray,cos,sin,player):
	display_height = len(display_grid)
	display_width = len(display_grid[0])
	half_display_height = display_height//2
	begin = half_display_height + wall_height
	for y in range(begin,display_height):
		dist = display_height/(2*y-display_height)
		#fisheye correction
		dist = dist/math.cos(angle_ray)
		
		tileX = dist * cos
		tileY = dist * sin
		tileX = math.floor(tileX + player["tx"])
		tileY = math.floor(tileY + player["ty"])
		if map_grid[tileY][tileX] == d_stair_color:
			mfy = math.floor(y)
			mfx = math.floor(x)
			if in_bounds(mfx,mfy,len(map_grid[0]),len(map_grid)):
				display_grid[mfy][mfx] = "x"
		else:
			continue
		
	
	
def render_lines(player,map_true, map_display,angles):
	#DDA
	distances = []
	hit_coords = []
	
	max_dim = max(len(map_true),len(map_true[0]))
	for ang in angles:
		precision = 128
		raycos = math.cos(ang + degrees_to_radians(player["angle"]))/precision
		
		raysin = math.sin(ang + degrees_to_radians(player["angle"]))/precision
		
		data = DDA_raycast(map_true,player["tx"],player["ty"],raycos,raysin)
		
		dist = data[0]
		hit_coord = data[1]
		#fisheye correction
		#dist *= math.cos(raycos)
		distances.append(dist)
		hit_coords.append(hit_coord)
		
		
	for i in range(len(distances)):
		percent = ((max_dim - distances[i])/(max_dim  + distances[i]))
		line_len = round(len(map_display) * percent)
		#line_len = round(len(map_display) * ((max_dim - distances[i])/max_dim))
		#line_len = distances[i]%len(map_true)
		#line_len = round(len(map_display) * ((max_dim - distances[i])/max_dim))
		
		bright_index = round((1 - percent) * (len(ASCII_brightness) - 1))
		choice_color = ASCII_brightness[bright_index]
		#render_floors(x,display_grid,map_grid,wall_height,angle_ray,cos,sin,player):
		raycos = math.cos(angles[i] + degrees_to_radians(player["angle"]))
		
		raysin = math.sin(angles[i] + degrees_to_radians(player["angle"]))
		
		#wall drawing
		draw_vertical_line(map_display,i,choice_color,line_len)
		#floor drawing
		render_floors(i,map_display,map_true,line_len,angles[i],raycos,raysin,player)
		
		
	
	#symbol_display(map_display)
	return [distances, hit_coords]
	
	#distances.clear()
	
	

		



	
def game_loop(player, map_true,map_display,columns,rows):
	#[N,NE,E,SE,S,SW,W]
	#possible directions
	#8 direction
	#x_vectors = []
	#y_vectors = []
	#x_vectors = [0,1,-1,1,0,-1,1,-1]
	#y_vectors = [-1,-1,0,1,1,1,0,-1]
	#[N,E,S,W]
	#4 direction
	x_vectors = [0,-1,0,1]
	y_vectors = [-1,0,1,0]
	directions = {
		#y, x
		#north/up
		"w":[-1, 0],
		#east/right
		"a":[0, -1],
		#south/down
		"s":[1, 0],
		#west/left
		"d":[0, 1],
	}
	
	omni_dir = {
		#w is forward
		#a is back
		#d is right
		#s is south
		45:{
			#uses angles 
			#y, x
			#north/up
			"s":[-1, -1],
			#east/right
			"d":[1, -1],
			#south/down
			"w":[1, 1],
			#west/left
			"a":[-1, 1],
		},
		90:{
			#uses angles 
			#y, x
			#north/up
			"s":[-1, 0],
			#east/right
			"d":[0, -1],
			#south/down
			"w":[1, 0],
			#west/left
			"a":[0, 1],
		},
		135:{
			#uses angles 
			#y, x
			#north/up
			"s":[-1, 1],
			#east/right
			"d":[-1, -1],
			#south/down
			"w":[1, -1],
			#west/left
			"a":[1, 1],
		},
		180:{
			#uses angles 
			#y, x
			#north/up
			"d":[-1, 0],
			#east/right
			"w":[0, -1],
			#south/down
			"a":[1, 0],
			#west/left
			"s":[0, 1],
		},
		225:{
			#uses angles 
			#y, x
			#north/up
			"d":[-1, 1],
			#east/right
			"w":[-1, -1],
			#south/down
			"a":[1, -1],
			#west/left
			"s":[1, 1],
		},
		
		270:{
			#uses angles 
			#y, x
			#north/up
			"w":[-1, 0],
			#east/right
			"a":[0, -1],
			#south/down
			"s":[1, 0],
			#west/left
			"d":[0, 1],
		},
		315:{
			#uses angles 
			#y, x
			#north/up
			"w":[-1, 1],
			#east/right
			"a":[-1, -1],
			#south/down
			"s":[1, -1],
			#west/left
			"d":[1, 1],
		},
		360:{
			#uses angles 
			#y, x
			#north/up
			"a":[-1, 0],
			#east/right
			"s":[0, -1],
			#south/down
			"d":[1, 0],
			#west/left
			"w":[0, 1],
		},
		0:{
			#uses angles 
			#y, x
			#north/up
			"a":[-1, 0],
			#east/right
			"s":[0, -1],
			#south/down
			"d":[1, 0],
			#west/left
			"w":[0, 1],
		}
		
	}
		
		
	
	angle_rays = ray_angles(rows,player["fov"],player["tx"],player["ty"])


	
	display_string = ""
	map_true[player['y']][player['x']] = player_color
	
	
	is_animated = True
	dir = ""
	#should be 45 or 90
	angle_inc = 45
	display_screen = True
	display_map = False
	
	
	while player["playing"]:
		
		
		map_display = empty_map(cols,rows, floor_color)
	
		
		#print(player)
		
		data = render_lines(player,map_true,map_display,angle_rays)
		dist_list = data[0]
		hit_list = data[1]
		
		
		
			
		
		
		dual_map_display(map_display,map_true,hit_list,display_screen,display_map)
		#symbol_display(map_display)
		print(f'angle:{player["angle"]}')
		#print("Commands: \n \'W\':Foward \'S\':Back \'Q\':Rotate Right \n \'A\':Left \'D\':Right \'E\':Rotate Left \n \'X\':Quit \n ")
		dir = input(f"Move?")
		
		
		
		#dir processing
		for letter in dir:
			if is_animated and len(dir) > 1:
				map_display = empty_map(cols,rows, floor_color)
				data = render_lines(player,map_true,map_display,angle_rays)
				dist_list = data[0]
				hit_list = data[1]
				
				dual_map_display(map_display,map_true,hit_list,display_screen,display_map)
				
				print("Animated Move Queue")
				time.sleep(.5)
				#console.clear()
				os.system('cls')
				
			#if directions.get(letter):
			if omni_dir[player["angle"]].get(letter):
				#temp_x = player['x'] + directions[letter][1]
				#temp_y = player['y'] + directions[letter][0]
				temp_x = player['x'] + omni_dir[player["angle"]][letter][1]
				temp_y = player['y'] + omni_dir[player["angle"]][letter][0]
				if map_true[temp_y][temp_x] != wall_color: 
					#in_bounds(temp_x,temp_y,len(grid[0]),len(grid)):
					#setting previous tile back to what it was
					map_true[player['y']][player['x']] = player['ground']
					#setting the grouf tile to whatever is beneath
					player['ground'] = map_true[temp_y][temp_x]					
					#setiing and updating the player position
					player['x'] = temp_x
					player['y'] = temp_y
					player['tx'] = player['x'] + .5
					player['ty'] = player['y'] + .5
					map_true[player['y']][player['x']] = player_color
				
			
			if letter == "e":
					player["angle"] += angle_inc
			if letter == "q":
					player["angle"] -= angle_inc
				
			
			if player["angle"] > 360:
				player["angle"]  -= 360
			elif player["angle"] < 0:
				player["angle"] += 360 
			
			if letter == "x":
				player["playing"] = False
				
				
			
				
			
			
		os.system('cls')
		#console.clear()
		#symbol_display(grid)
		
		#dual_map_display(map_display,map_true,hit_list)
		map_display.clear()
		
		
		
		
		
		

true_map = [
	
	[0,0,0,0,0],
	[0,1,1,1,0],
	[0,1,1,1,0],
	[0,1,1,1,0],
	[0,0,0,0,0]
	
]

true_map = [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,1,0,0,1,1,1,1,0,0,0],
	[0,0,0,0,0,1,0,0,1,1,1,1,0,0,0],
	[0,1,1,1,1,1,0,0,1,0,0,1,0,1,0],
	[0,1,2,1,1,0,0,0,1,1,0,1,1,1,0],
	[0,1,1,1,1,0,0,0,1,0,0,1,1,1,0],
	[0,0,0,1,1,0,0,0,1,0,0,1,0,1,0],
	[0,0,0,1,1,1,2,2,2,1,1,1,1,1,0],
	[0,0,0,1,1,1,2,2,2,1,1,0,0,1,0],
	[0,0,0,1,1,1,2,2,2,1,1,0,0,1,0],
	[0,0,0,1,1,1,1,1,1,1,1,0,0,1,0],
	[0,0,0,1,0,0,0,0,1,0,1,0,0,1,0],
	[0,0,0,1,0,0,0,1,1,1,1,0,0,1,0],
	[0,0,0,1,0,0,0,1,1,1,1,1,1,1,0],
	[0,0,0,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	
	]

rows= 100
cols = 30



display_map = empty_map(cols,rows,floor_color)
'''
temp = rooms.copy()

grid, rooms = floor_maker(16,20,3)
start_room = temp[random.randint(0, len(temp) - 1)]
	
temp.remove(start_room)
	
rx = random.randint(start_room[0],start_room[0] + start_room[2] - 1)
ry = random.randint(start_room[1],start_room[1] + start_room[3] - 1)
'''
	
player = {
	
	"x":3,
	"y":3,
	"tx":3+ .5,
	"ty":3 + .5,
	"fov":60,
	"angle":90,
	"ground":floor_color,
	"playing":True
	}
	


game_loop(player, true_map,display_map, cols,rows)
