import random
import math
import time
#import console
import os

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
				h = h + '#'
			elif col == floor_color:
				h = h + '.'
			elif col == unknown_color:
				h = h + '?'
			elif col == player_color:
				h = h + '@'
			elif col == up_stairs_color:
				h = h + 'u'
			elif col == down_stairs_color:
				h = h + 'd'
			else:
				h = h + '.'
			
		h = h + '\n'
	print(h)
	
def limits(arr,rect):
	#visualizes BSP borders
	#x0,y1,w2,h3
	x = rect[0]
	y = rect[1]
	w = rect[2]
	h = rect[3]
	#print(x,y,w,h,sep='_')
	for row in range(y,y+h):
		for col in range(x,x+w):
			#arr[row][col] = 1
			
			if col == x or col == x + w - 1:
				arr[row][col] = floor_color
			elif row == y or row == y + h - 1:
				arr[row][col] = floor_color
			else:
				arr[row][col] = wall_color
	
def BSP_display(borders,arr):
	for i in borders:
		limits(arr,i)
	symbol_display(arr)	
	
def paver(arr,rect):
	#paves individual rooms
	#x0,y1,w2,h3
	x = rect[0]
	y = rect[1]
	w = rect[2]
	h = rect[3]
	#print(x,y,w,h,sep='_')
	grid_w = len(arr[0]) - 1
	grid_h = len(arr) - 1
	for row in range(y,y+h):
		for col in range(x,x+w):
			#if col < grid_w and row < grid_h:
			arr[row][col] = floor_color
			'''
			if col == x or col == x + w - 1:
				arr[row][col] = 1
			elif row == y or row == y + h - 1:
				arr[row][col] = 1
			else:
				arr[row][col] = 0
			'''

		
				
		
				

	#symbol_display(arr)				
			


def dist_form(x1,y1,x2,y2):
	Xs = math.pow((x2 - x1),2)
	Ys = math.pow((y2 - y1),2)
	return int((Xs + Ys))
	
def in_bounds(x,y,arr_w,arr_h):
	return x < arr_w - 1 and x >= 0 and y < arr_h - 1 and y >= 0
	

def a_star(arr,start_x,start_y,goal_x,goal_y,diagonals):
	
	x_vectors = []
	y_vectors = []
	
	if diagonals:
		#[N,NE,E,SE,S,SW,W]
		#possible directions
		#8 direction
		x_vectors = [0,1,-1,1,0,-1,1,-1]
		y_vectors = [-1,-1,0,1,1,1,0,-1]
	else:
		#[N,E,S,W]
		#4 direction
		x_vectors = [0,-1,0,1]
		y_vectors = [-1,0,1,0]

	
	w = len(arr[0])
	h = len(arr)
	
	
	#root
	cur_name = str(start_x) + '-' + str(start_y)
	
	
	#keeps track pf all visited nodes
	
	open_list = [[start_x,start_y]]

	
	#set of nodes already evaluated
	closed_list = []
	
	
	tree = {cur_name:[None]}
	
	cur_x = start_x
	cur_y = start_y
	
	f_cost_list = []
	
	
	
	while open_list:
		#current = open_list.pop(0)
		#print(open_list)
		#print(f_cost_list)
		#print(cur_name)
		
				
		
			
		ind = 0
		current = None
		if f_cost_list:
			small = min(f_cost_list)
			ind = f_cost_list.index(small)
			current = open_list.pop(ind)
			
			f_cost_list.pop(ind)
		else:
			current = open_list.pop(ind)
			
			
		if current not in closed_list:
			closed_list.append(current)
		
		
		
		
		
		cur_x = current[0]
		cur_y = current[1]
		
		
		
		
		cur_name = str(cur_x) + '-' + str(cur_y)
		
		if arr[cur_y][cur_x] != start_color and arr[cur_y][cur_x] != goal_color:
			arr[cur_y][cur_x] = visited_color		
		
		
		#print(lowest_f_cost)
		i = 0
		
		
		while i < len(x_vectors):
			
			y = cur_y + y_vectors[i]
			x = cur_x + x_vectors[i]
			
			
			
			
			h_cost = dist_form(x,y,goal_x,goal_y)
			g_cost = abs(start_x - x) + abs(start_y - y) 
			
			f_cost = h_cost + g_cost
			
			
			
			
			if in_bounds(x,y,w,h): #and arr[y][x] != wall_color:
				#neighbor = str(x) + '-' +str(y)
				
				
				
				if tree.get(cur_name):
					info = [[x,y],g_cost,h_cost,f_cost]
					if info not in tree[cur_name]:
						tree[cur_name].append(info)
						#tree[cur_name].append([x,y])
				else:
					tree.update({cur_name:[]})
					tree[cur_name].append([[x,y],g_cost,h_cost,f_cost])
					#tree[cur_name].append([x,y])
				
				if [x,y] not in closed_list and [x,y] not in open_list:
				
					open_list.append([x,y])
					f_cost_list.append(f_cost)
				
				
				
				
				
				
				
					
					
			i += 1
					
					
		#print(open_list)
			
		
		#time.sleep(.05)
		#os.system('cls')
		#console.clear()
		#symbol_display(arr)
		
		
		if not f_cost_list:
			#print("no path")
			break
		
		if current == [goal_x, goal_y]:
			#print("path found")
			break
		
		
		"""
		if g > 30:
			print('too long')
			
			print(closed_list)
			break
		"""
		
	
	#print(tree[cur_name][-1])
	#print(cur_x, " ",cur_y, " ", cur_name)
	path = []
	if cur_x == goal_x and cur_y == goal_y:
		#last index: the goal coords
		
		while True:
			
			if tree[cur_name][0] == None: #the root node
				break
			smallest_ind = w * h
			smallest = w * h
					
			
			
			for i in range(len(tree[cur_name])):
				g_cost = tree[cur_name][i][1]
				coords = tree[cur_name][i][0]

				if coords in closed_list and coords not in path:
					if g_cost < smallest:
						smallest = g_cost
						smallest_ind = i
				
				
				#print(tree[cur_name][i])
				#print(tree[cur_name][i][0])
				
				
			
			xy = tree[cur_name][smallest_ind][0]
			cur_x = xy[0]
			cur_y = xy[1]
			cur_name = str(cur_x) + '-' + str(cur_y)
			if arr[cur_y][cur_x] != start_color and arr[cur_y][cur_x] != goal_color:
				arr[cur_y][cur_x] = traceback_color
				path.append([cur_x,cur_y])
			
			#time.sleep(.15)
			#os.system('cls')
			#console.clear()
			#symbol_display(arr)
			
					
	for i in arr:
		i = [wall_color] * w
	
	#for k, v in tree.items():
	#	print(k," ",v)			
	return path[::-1]
		
def tunnel_maker(arr,rooms):

	
	tunnels = []
	
	#assumes more than 3 rooms
	for i in range(len(rooms)-1):
		
		
		#centers of two rooms
		cx1 = (rooms[i][0] + rooms[i][0] + rooms[i][2])//2
		cy1 = (rooms[i][1] + rooms[i][1] + rooms[i][3])//2
		
		cx2 = (rooms[i+1][0] + rooms[i+1][0] + rooms[i+1][2])//2
		cy2 = (rooms[i+1][1] + rooms[i+1][1] + rooms[i+1][3])//2
		
			
		tunnels.append((cx1,cy1,cx2,cy2))
		
			
	paths = []
	for i in tunnels:
		p = a_star(arr,i[0],i[1],i[2],i[3],False)
		paths.append(p)
		#pathways(i[0],i[1],arr,i[2],i[3],i[4],i[5])		
	for path in paths:
		for cell in path:
			arr[cell[1]][cell[0]] = floor_color
			
			
def room_paver(arr,rect):
	#paves individual rooms
	#x0,y1,w2,h3
	x = rect[0]
	y = rect[1]
	w = rect[2]
	h = rect[3]
	#print(x,y,w,h,sep='_')
	grid_w = len(arr[0]) - 1
	grid_h = len(arr) - 1
	for row in range(y,y+h):
		for col in range(x,x+w):
			#if col < grid_w and row < grid_h:
			arr[row][col] = floor_color
			'''
			if col == x or col == x + w - 1:
				arr[row][col] = 1
			elif row == y or row == y + h - 1:
				arr[row][col] = 1
			else:
				arr[row][col] = 0
			'''

		
				
		
				

	#symbol_display(arr)			


def BSP(floor, splits):
	#This fuction splits a two dimensional array into a bunch of small squares
	#x0,y1,w2,h3
	#arr is the map size represented by x, y, w,h
	
	#width is the with of the map size
	#height is the height of th map soze

	#splits is how many box exists
	
	arr_x = 0
	arr_y = 0
	arr_w = len(floor[0])
	arr_h = len(floor)
	areas = [[arr_x,arr_y,arr_w,arr_h]]
	
	Vs = 0
	Hs = 0
	rigged = False
	rand = 0
	while len(areas) != splits:
		#print(areas)
		#print()
		
		
		
		if not rigged:
			
			rand = round(random.random() * 2)
		
		if rand%2 == 0:
			
			
			if Vs - Hs < 2:
				new_w = random.randint(arr_w//2,int(arr_w * .6))
				areas.append([arr_x,arr_y,new_w,arr_h])
				areas.append([arr_x + new_w,arr_y,arr_w - new_w,arr_h])
				rigged = False
				
				Vs += 1
				areas.pop(0)
				arr_x = areas[0][0]
				arr_y = areas[0][1]
				arr_w = areas[0][2]
				arr_h = areas[0][3]
			else:
				rand = 1
				rigged = True
			
				
			
				
			
		if rand%2 == 1:
			
			if Hs - Vs < 2:
				Hs += 1
				
				new_h = random.randint(arr_h//2,int(arr_h * .6))
				areas.append([arr_x,arr_y,arr_w,new_h])
				areas.append([arr_x,arr_y + new_h - 1,arr_w,arr_h - new_h + 1])
				rigged = False
				
				areas.pop(0)
				arr_x = areas[0][0]
				arr_y = areas[0][1]
				arr_w = areas[0][2]
				arr_h = areas[0][3]
			else:
				rand = 2
				rigged = True
				
				
		
		
		
	
	
	return areas
	
	
def floor_maker(rows,cols,room_num):
	grid = empty_map(rows,cols,[])
	grid2 = empty_map(rows,cols,[])
	rooms = []
	
	borders = BSP(grid2,room_num)
	BSP_display(borders,grid2)
	 
	grid_w = len(grid[0]) - 1
	grid_h = len(grid) - 1
	for i in borders:
		rw = random.randint(2,int(i[2]*.8))
		rh = random.randint(2,int(i[3]*.8))
		choice = random.randint(0,100)
		
		if rw <= 2:
			rw += random.randint(1,3)
		if rh <= 2:
			rh += random.randint(1,3)
		
		'''
		if rw/rh > 1.8:
			rw = rh
			
		elif rh/rw > 1.8:
			rh = rw
		'''
			
		
		rx = random.randint(i[0] ,(i[0] + i[2] - rw))
		ry = random.randint(i[1],(i[1] + i[3] - rh))
		print([rx,ry,rw,rh])
		
		rooms.append([rx,ry,rw,rh])
	print()
	
	
	tunnel_maker(grid,rooms)
	
	for i in rooms:
		room_paver(grid,i)
	symbol_display(grid)
	return grid, rooms



def game_loop():
	ROWS = 16
	COLS = 44
	room_num = 3
	grid, rooms = floor_maker(ROWS,COLS,room_num)
	
	
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
		#north
		"w":[-1, 0],
		#east
		"a":[0, -1],
		#south
		"s":[1, 0],
		#west
		"d":[0, 1],
	}
	
	
	
	floors = []
	#floors.append(grid)
	level = 0
	
	
	
	temp = rooms.copy()
	
	start_room = temp[random.randint(0, len(temp) - 1)]
	
	temp.remove(start_room)
	
	
	
	player = {
	"hp":10,
	"x":random.randint(start_room[0],start_room[0] + start_room[2] - 1),
	"y":random.randint(start_room[1],start_room[1] + start_room[3] - 1),
	"ground":floor_color
	
	}
	
	
	
	
	
	d_stair_room = temp[random.randint(0, len(temp) - 1)]
	
	temp.remove(d_stair_room)
	
	d_stair_x = random.randint(d_stair_room[0] + 1,d_stair_room[0] + d_stair_room[2] - 2)
	d_stair_y = random.randint(d_stair_room[1] + 1,d_stair_room[1] + d_stair_room[3] - 2)
	
	#grid, downstairs data, upstairs data, 
	floors.append([grid,[d_stair_y, d_stair_x,down_stairs_color],None])
	

	
	
	cur_floor = floors[level][0]
	cur_floor[d_stair_y][d_stair_x] = down_stairs_color
	cur_floor[player["y"]][player["x"]] = player_color
	#console.clear()
	os.system('cls')
	symbol_display(cur_floor)
	dir = ""
	msg = []
	print("Commands: \n \'W\':North \n \'A\':East \n \'S\':South \n \'D\':West")
	while True:
		
		
		
		
		
		if dir.lower() == "q":
			print("quitted")
			break
		#msg.append('{x_pos} {y_pos}'.format(x_pos = player['x'],y_pos = player['y']))
		#msg.append('{dw} \n {dy}'.format(dw = floors[level][1],dy = floors[level][2]))
		#msg.append(f'{d_stair_x} {d_stair_y}')
		#msg.append(f'{down_stairs_color}')
		#msg.append("ground value: {g}".format(g = player['ground']))
		'''
		for key in directions:
			temp_x = player['x'] + directions[key][1]
			temp_y = player['y'] + directions[key][0]
			if in_bounds(temp_x,temp_y,len(cur_floor[0]),len(cur_floor)):
				
				msg.append('{k} {d}'.format(k = key, d = cur_floor[temp_y][temp_x] ))
		'''
				
				
		if player["ground"] == down_stairs_color:
			if msg:
				for sentence in msg:
					print(sentence)
			dir = input(f"Descend?\nY/N?")
			msg.clear()
		elif player["ground"] == up_stairs_color:
			
			if msg:
				for sentence in msg:
					print(sentence)
			dir = input(f"Ascend?\nY/N?")
			msg.clear()
		else:
			
			if msg:
				for sentence in msg:
					print(sentence)
			dir = input(f"Move?")
			msg.clear()
		
		
		#dir processing
		for letter in dir:
			
			
			
			if directions.get(letter):
				temp_x = player['x'] + directions[letter][1]
				temp_y = player['y'] + directions[letter][0]
				if cur_floor[temp_y][temp_x] != wall_color and in_bounds(temp_x,temp_y,len(cur_floor[0]),len(cur_floor)):
					#setting previous tile back to what it was
					cur_floor[player['y']][player['x']] = player['ground']
					#setting the grouf tile to whatever is beneath
					player['ground'] = cur_floor[temp_y][temp_x]					
					#setiing and updating the player position
					player['x'] = temp_x
					player['y'] = temp_y
					cur_floor[player['y']][player['x']] = player_color
			
			
			
			
			if letter.lower() == "y":
				#on stair tile
				
				if player["ground"] == down_stairs_color:
					
					msg.append(f'Now on new floor')
					if level == len(floors) - 1:
						#generate a new map
						
						msg.append('floor created')
						msg.append("down at limit")
						grid, rooms = floor_maker(ROWS,COLS,room_num)
						floors.append([grid,None,None])
						#prev_floor = floors[level]
						level += 1
						cur_floor = floors[level][0]
						
						
						
						
						temp = rooms.copy()
						
						start_room = temp[random.randint(0, len(temp) - 1)]
						
						temp.remove(start_room)
						
						
						player["x"] = random.randint(start_room[0] + 1,start_room[0] + start_room[2] - 2)
						player["y"] = random.randint(start_room[1] + 1,start_room[1] + start_room[3] - 2)
						
						
						
						
						player["ground"] = up_stairs_color
						
						#player["u_stair_loc"].append([player["y"],player["x"]])
						
						
						d_stair_room = temp[random.randint(0, len(temp) - 1)]
						
						temp.remove(d_stair_room)
						
						d_stair_x = random.randint(d_stair_room[0] + 1,d_stair_room[0] + d_stair_room[2] - 2)
						d_stair_y = random.randint(d_stair_room[1] + 1,d_stair_room[1] + d_stair_room[3] - 2)
						
						#down stairs location
						floors[level][1] = [d_stair_y, d_stair_x,down_stairs_color]
						#up stairs location
						floors[level][2] = [player['y'],player['x'],up_stairs_color]
						
						cur_floor[d_stair_y][d_stair_x] = down_stairs_color
						
						cur_floor[player['y']][player['x']] = player_color
						
					else:
						#traverse floors
						#copy_floor = floors[level].copy()
						#floors[level] = #floors[level].clear()
						msg.append("down not at limit")
						level += 1
						
						cur_floor = floors[level][0]
						#floors[level - 1] = copy_floor
						#
						d_stair_x = floors[level][1][1]
						d_stair_y = floors[level][1][0]
						cur_floor[floors[level][1][0]][floors[level][1][1]] = down_stairs_color
						cur_floor[floors[level][2][0]][floors[level][2][1]] = up_stairs_color
						
						
						
						player["y"] = floors[level][2][0]
						player["x"] = floors[level][2][1]
						cur_floor[player['y']][player['x']] = player_color
						player["ground"] = up_stairs_color
						#player["u_stair_loc"].append([player["y"],player["x"]])
					break
				elif player["ground"] == up_stairs_color:
					
							
						if level > 0:
							msg.append("up")
							prev_floor = floors[level][0]
							
							level -= 1
							cur_floor = floors[level][0]
							
					
							
							player["x"] = floors[level][1][1]
							player["y"] = floors[level][1][0]
							player["ground"] = down_stairs_color
							
							break
					
				
				
			if letter.lower() == "n":
				
				
				msg.append("ok")
				break
				
			
		
		
		#console.clear()
		os.system('cls')
		symbol_display(cur_floor)
	
	

game_loop()




		
			
		
