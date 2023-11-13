import random
import math



def empty_map(rows,columns,empty_arr):
	for i in range(rows):
		empty_arr.append([0]*columns)
			
	return  empty_arr
	
	
def symbol_display(arr):
	#displays map in readable format
	h=''
	for row in arr:
		for col in row:
			if col == 0:
				h = h + '# '
			elif col == 1:
				h = h + '. '
			elif col == 2:
				h = h + 'N '
			elif col == 3:
				h = h + 'S '
			elif col == 4:
				h = h + 'E '
			elif col == 5:
				h = h + 'W '
			elif col == 6:
				h = h + 'Q '
		h = h + '\n'
	print(h)
				
				
def AABB(a,b):
	#x0,y1,w2,h3
	#rectangle collision
	#returns true if collision false if not
	return a[0] <= b[0] + b[2] and a[0] + a[2] >= b[0] and a[1] <= b[1] + b[3] and a[1] + a[3] >= b[1]


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
				arr[row][col] = 1
			elif row == y or row == y + h - 1:
				arr[row][col] = 1
			else:
				arr[row][col] = 0
				
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
			arr[row][col] = 1
			'''
			if col == x or col == x + w - 1:
				arr[row][col] = 1
			elif row == y or row == y + h - 1:
				arr[row][col] = 1
			else:
				arr[row][col] = 0
			'''
			


def cross(arr,sx,sy,ex,ey,s_vec,e_vec):
	#[up,right,down,left]
	#x_vectors = [0,1,0,-1]
	#y_vectors = [-1,0,1,0]
	#order is x y
	#up_vec = [0,-1]
	#right_vec = [1,0]
	#down_vec = [0,1]
	#left_vec = [-1,0]
	
	#s_vec = []
	#e_vec = []
	#literal space between to points
	total_spaces_y = max(sy,ey) - min(sy,ey)
	total_spaces_x = max(sx,ex) - min(sx,ex)
	
	partial_x = random.randint(0,total_spaces_x)
	partial_y = random.randint(0,total_spaces_y)
	
	rest_x = total_spaces_x - partial_x
	rest_y = total_spaces_y - partial_y
	
	orig_sx = sx
	orig_sy = sy
	orig_ex = ex
	orig_ey = ey
	grid_w = len(arr[0]) - 1
	grid_h = len(arr) - 1
	
	#up and down
	if s_vec == [0,-1] and e_vec == [0,1]:
		
		while partial_y != 0:

			orig_sx += s_vec[0]
			orig_sy += s_vec[1]
			partial_y -= 1
			arr[orig_sy][orig_sx] = 1
			
		while rest_y != 0:
			orig_ex += e_vec[0]
			orig_ey += e_vec[1]
			rest_y -= 1
			arr[orig_ey][orig_ex] = 1
			
		#connecting the two adjecent corridors
		if orig_sx < orig_ex: 
			
			while [orig_sx,orig_sy] != [orig_ex,orig_ey]:
				orig_sx += 1
				arr[orig_sy][orig_sx] = 1
				
		elif orig_sx > orig_ex: 
			
			while [orig_sx,orig_sy] != [orig_ex,orig_ey]:
				orig_ex += 1
				arr[orig_ey][orig_ex] = 1
				
	elif s_vec == [0,1] and e_vec == [0,-1]:
		
		while partial_y != 0:
			#symbol_display(arr)
			orig_sx += s_vec[0]
			orig_sy += s_vec[1]
			partial_y -= 1
			arr[orig_sy][orig_sx] = 1
			
		while rest_y != 0:
			orig_ex += e_vec[0]
			orig_ey += e_vec[1]
			rest_y -= 1
			arr[orig_ey][orig_ex] = 1
			
		#connecting the two adjecent corridors
		if orig_sx < orig_ex: 
			while [orig_sx,orig_sy] != [orig_ex,orig_ey]:
				orig_sx += 1
				arr[orig_sy][orig_sx] = 1
				
		elif orig_sx > orig_ex: 
			
			while [orig_sx,orig_sy] != [orig_ex,orig_ey]:
				orig_ex += 1
				arr[orig_ey][orig_ex] = 1
				
	#left and right
	elif s_vec == [1,0] and e_vec == [-1,0]:
		
		while partial_x != 0:
			#symbol_display(arr)
			orig_sx += s_vec[0]
			orig_sy += s_vec[1]
			partial_x -= 1
			arr[orig_sy][orig_sx] = 1
			
		while rest_x != 0:
			orig_ex += e_vec[0]
			orig_ey += e_vec[1]
			rest_x -= 1
			arr[orig_ey][orig_ex] = 1
			
		#connecting the two adjecent corridors
		if orig_sy < orig_ey: 
			while [orig_sx,orig_sy] != [orig_ex,orig_ey]:
				orig_sy += 1
				arr[orig_sy][orig_sx] = 1
				
		elif orig_sy > orig_ey: 
			
			while [orig_sx,orig_sy] != [orig_ex,orig_ey]:
				orig_ey += 1
				arr[orig_ey][orig_ex] = 1
				
	elif s_vec == [-1,0] and e_vec == [1,0]:
		
		while partial_x != 0:
			#symbol_display(arr)
			orig_sx += s_vec[0]
			orig_sy += s_vec[1]
			partial_x -= 1
			arr[orig_sy][orig_sx] = 1
			
		while rest_x != 0:
			orig_ex += e_vec[0]
			orig_ey += e_vec[1]
			rest_x -= 1
			arr[orig_ey][orig_ex] = 1
			
		#connecting the two adjecent corridors
		if orig_sy < orig_ey: 
			
			while [orig_sx,orig_sy] != [orig_ex,orig_ey]:
				orig_sy += 1
				arr[orig_sy][orig_sx] = 1
				
		elif orig_sy > orig_ey: 
			
			while [orig_sx,orig_sy] != [orig_ex,orig_ey]:
				orig_ey += 1
				arr[orig_ey][orig_ex] = 1
				
	else:
		#up_vec = [0,-1]
		#right_vec = [1,0]
		#down_vec = [0,1]
		#left_vec = [-1,0]
		#since the opposite direction is already covered we cover the leftovers
		
		if s_vec == [0,-1]:
			
			while orig_sy > orig_ey:
					orig_sx += s_vec[0]
					orig_sy += s_vec[1]
					arr[orig_sy][orig_sx] = 1
					
			if e_vec == [1,0]:
				
				while orig_sx > orig_ex:
					orig_ex += e_vec[0]
					orig_ey += e_vec[1]
					arr[orig_ey][orig_ex] = 1
					
			elif e_vec == [-1,0]:
				
				while orig_sx < orig_ex:
					orig_ex += e_vec[0]
					orig_ey += e_vec[1]
					arr[orig_ey][orig_ex] = 1
					
		elif s_vec == [1,0]:
			
			while orig_sx < orig_ex:
					orig_sx += s_vec[0]
					orig_sy += s_vec[1]
					arr[orig_sy][orig_sx] = 1
					
			if e_vec == [0,1]:
				
				while orig_sy > orig_ey:
					orig_ex += e_vec[0]
					orig_ey += e_vec[1]
					arr[orig_ey][orig_ex] = 1
					
			elif e_vec == [0,-1]:
				
				while orig_sy < orig_ey:
					orig_ex += e_vec[0]
					orig_ey += e_vec[1]
					arr[orig_ey][orig_ex] = 1
					
		elif s_vec == [0,1]:
			
			while orig_sy < orig_ey:
					orig_sx += s_vec[0]
					orig_sy += s_vec[1]
					arr[orig_sy][orig_sx] = 1
					
			if e_vec == [1,0]:
				
				while orig_sx > orig_ex:
					orig_ex += e_vec[0]
					orig_ey += e_vec[1]
					arr[orig_ey][orig_ex] = 1
					
			elif e_vec == [-1,0]:
				
				while orig_sx < orig_ex:
					orig_ex += e_vec[0]
					orig_ey += e_vec[1]
					arr[orig_ey][orig_ex] = 1
					
		elif s_vec == [-1,0]:
			
			while orig_sx > orig_ex:
					orig_sx += s_vec[0]
					orig_sy += s_vec[1]
					arr[orig_sy][orig_sx] = 1
					
			if e_vec == [0,1]:
				
				while orig_sy > orig_ey:
					orig_ex += e_vec[0]
					orig_ey += e_vec[1]
					arr[orig_ey][orig_ex] = 1
					
			elif e_vec == [0,-1]:
				
				while orig_sy < orig_ey:
					orig_ex += e_vec[0]
					orig_ey += e_vec[1]
					arr[orig_ey][orig_ex] = 1
		
				
				

	

def dist_form(x1,y1,x2,y2):
	Xs = math.pow((x2 - x1),2)
	Ys = math.pow((y2 - y1),2)
	return int(round(math.sqrt(Xs + Ys),0))

def least_dist(arr_1,arr_2):
	dist_dict = {}
	all_distances = []
	for coords in arr_1:
		for points in arr_2:
			dist = dist_form(coords[0],coords[1],points[0],points[1])
			if dist not in all_distances:
				dist_dict.update({dist:[coords[0],coords[1],points[0],points[1]]})
				all_distances.append(dist)
	return dist_dict[min(all_distances)]
			


def tunnel_maker_b(arr,rooms):
	
	#x0,y1,w2,h3
	tunnels = []
	#these exist to limit the area searched in the array to build tunnels
	sx,ex,sy,ey = 0,0,0,0
	#[up,right,down,left]
	x_vectors = [0,1,0,-1]
	y_vectors = [-1,0,1,0]
	#order is x y
	#the direction the tunnels will extend from
	up_vec = [0,-1]
	right_vec = [1,0]
	down_vec = [0,1]
	left_vec = [-1,0]
	
	s_vec = []
	e_vec = []
	
	#assumes more than 3 rooms
	for i in range(len(rooms) - 1):
		
		
		#centers of two rooms
		cx1 = (rooms[i][0] + rooms[i][0] + rooms[i][2])//2
		cy1 = (rooms[i][1] + rooms[i][1] + rooms[i][3])//2
		#The center of the top,left,bottom,and right of the room
		cx1_north = cx1 
		cy1_north = cy1 - rooms[i][3]//2
		
		#arr[cy1_north][cx1_north] = 2
		
		cx1_south = cx1 
		cy1_south = cy1 + rooms[i][3]//2
		
		#arr[cy1_south][cx1_south] = 3
		
		cx1_east = cx1 + rooms[i][2]//2
		cy1_east = cy1 
		
		#arr[cy1_east][cx1_east] = 4
		
		cx1_west = cx1 - rooms[i][2]//2
		cy1_west = cy1 
		
		#arr[cy1_west][cx1_west] = 5
		
		arr_1 = [
			[cx1_north,cy1_north],
			[cx1_south,cy1_south],
			[cx1_east,cy1_east],
			[cx1_west,cy1_east]
	
		]
		
		
		cx2 = (rooms[i+1][0] + rooms[i+1][0] + rooms[i+1][2])//2
		cy2 = (rooms[i+1][1] + rooms[i+1][1] + rooms[i+1][3])//2
		
		cx2_north = cx2
		cy2_north = cy2 - rooms[i + 1][3]//2
		
		#arr[cy2_north][cx2_north] = 2
		
		cx2_south = cx2
		cy2_south = cy2 + rooms[i + 1][3]//2
		
		#arr[cy2_south][cx2_south] = 3
		
		cx2_east = cx2 + rooms[i + 1][2]//2
		cy2_east = cy2 
		
		#arr[cy2_east][cx2_east] = 4
		
		cx2_west = cx2 - rooms[i + 1][2]//2
		cy2_west = cy2 
		
		#arr[cy2_west][cx2_west] = 5
		
		arr_2 = [
			[cx2_north,cy2_north],
			[cx2_south,cy2_south],
			[cx2_east,cy2_east],
			[cx2_west,cy2_west]
	
		]
		#returns x1,y1 and x2,y2 of closest points
		closest_points = least_dist(arr_1,arr_2)
		#print(closest_points)
		#choosing a random part of one of the walls on the north, south,east or west walls
		offset_x1 = rooms[i][2]//2
		offset_y1 = rooms[i][3]//2
		
		offset_x2 = rooms[i+1][2]//2
		offset_y2 = rooms[i+1][3]//2
		
		choice_x1 = random.randint(-offset_x1,offset_x1)
		
		choice_y1 = random.randint(-offset_y1,offset_y1)
		
		choice_x2 = random.randint(-offset_x2,offset_x2)
		
		choice_y2 = random.randint(-offset_y2,offset_y2)
		
		if closest_points[0] == cx1_north and closest_points[1] == cy1_north:
			closest_points[0] += choice_x1
			s_vec = up_vec
			#closest_points[1] += choice_y
		elif closest_points[0] == cx1_south and closest_points[1] == cy1_south:
			closest_points[0] += choice_x1
			s_vec = down_vec
			#closest_points[1] += choice_y
		elif closest_points[0] == cx1_east and closest_points[1] == cy1_east:
			#closest_points[0] += choice_x 
			s_vec = right_vec
			closest_points[1] += choice_y1
		elif closest_points[0] == cx1_west and closest_points[1] == cy1_west:
			#closest_points[0] += choice_x 
			s_vec = left_vec
			closest_points[1] += choice_y1
			
		
		if closest_points[2] == cx2_north and closest_points[3] == cy2_north:
			closest_points[2] += choice_x2
			e_vec = up_vec
			#closest_points[3] += choice_y
		elif closest_points[2] == cx2_south and closest_points[3] == cy2_south:
			closest_points[2] += choice_x2
			e_vec = down_vec
			#closest_points[3] += choice_y
		elif closest_points[2] == cx2_east and closest_points[3] == cy2_east:
			#closest_points[2] += choice_x
			e_vec = right_vec
			closest_points[3] += choice_y2
		elif closest_points[2] == cx2_west and closest_points[3] == cy2_west:
			#closest_points[2] += choice_x
			closest_points[3] += choice_y2
			e_vec = left_vec
			
		arr[closest_points[1]][closest_points[0]] =  1
		arr[closest_points[3]][closest_points[2]] =  1
		
		#establishing the direction
		#vec_x, vec_y = vec_maker(closest_points)
		
		
		
		#decides whether the tunnel between two room will be top right or bottom left compared to the center of the rooms
		#print(closest_points)
		
		sx = closest_points[0]
		sy = closest_points[1]
		ex = closest_points[2]
		ey = closest_points[3]
		tunnels.append((sx,sy,ex,ey,s_vec,e_vec))
		
		another_room =  random.random()
		if another_room > .75:
			#temp exists so the same room isn't selected
			
			
			temp = rooms.copy()
			temp.pop(i + 1)
			temp.pop(i)
			
			rand = random.randint(0,len(temp) - 1 )
			#centers of two rooms
			cx1 = (rooms[i][0] + rooms[i][0] + rooms[i][2])//2
			cy1 = (rooms[i][1] + rooms[i][1] + rooms[i][3])//2
			
			
			#The center of the top,left,bottom,and right of the room
			cx1_north = cx1 
			cy1_north = cy1 - rooms[i][3]//2
			
			#arr[cy1_north][cx1_north] = 2
			
			cx1_south = cx1 
			cy1_south = cy1 + rooms[i][3]//2
			
			#arr[cy1_south][cx1_south] = 3
			
			cx1_east = cx1 + rooms[i][2]//2
			cy1_east = cy1 
			
			#arr[cy1_east][cx1_east] = 4
			
			cx1_west = cx1 - rooms[i][2]//2
			cy1_west = cy1 
			
			#arr[cy1_west][cx1_west] = 5
			
			arr_1 = [
				[cx1_north,cy1_north],
				[cx1_south,cy1_south],
				[cx1_east,cy1_east],
				[cx1_west,cy1_east]
		
			]
			cx2 = (temp[rand][0] + temp[rand][0] + temp[rand][2])//2
			cy2 = (temp[rand][1] + temp[rand][1] + temp[rand][3])//2
			
			
			
			cx2_north = cx2
			cy2_north = cy2 - temp[rand][3]//2
			
			#arr[cy2_north][cx2_north] = 2
			
			cx2_south = cx2
			cy2_south = cy2 + temp[rand][3]//2
			
			#arr[cy2_south][cx2_south] = 3
			
			cx2_east = cx2 + temp[rand][2]//2
			cy2_east = cy2 
			
			#arr[cy2_east][cx2_east] = 4
			
			cx2_west = cx2 - temp[rand][2]//2
			cy2_west = cy2 
			
			#arr[cy2_west][cx2_west] = 5
			
			arr_2 = [
				[cx2_north,cy2_north],
				[cx2_south,cy2_south],
				[cx2_east,cy2_east],
				[cx2_west,cy2_west]
		
			]
			#returns x1,y1 and x2,y2 of closest points
			closest_points = least_dist(arr_1,arr_2)
			#print(closest_points)
			#choosing a random part of one of the walls on the north, south,east or west walls
			offset_x1 = rooms[i][2]//2
			offset_y1 = rooms[i][3]//2
			
			offset_x2 = temp[rand][2]//2
			offset_y2 = temp[rand][3]//2
			
			choice_x1 = random.randint(-offset_x1,offset_x1)
			
			choice_y1 = random.randint(-offset_y1,offset_y1)
			
			choice_x2 = random.randint(-offset_x2,offset_x2)
			
			choice_y2 = random.randint(-offset_y2,offset_y2)
			
			if closest_points[0] == cx1_north and closest_points[1] == cy1_north:
				closest_points[0] += choice_x1
				s_vec = up_vec
				#closest_points[1] += choice_y
			elif closest_points[0] == cx1_south and closest_points[1] == cy1_south:
				closest_points[0] += choice_x1
				s_vec = down_vec
				#closest_points[1] += choice_y
			elif closest_points[0] == cx1_east and closest_points[1] == cy1_east:
				#closest_points[0] += choice_x 
				s_vec = right_vec
				closest_points[1] += choice_y1
			elif closest_points[0] == cx1_west and closest_points[1] == cy1_west:
				#closest_points[0] += choice_x 
				s_vec = left_vec
				closest_points[1] += choice_y1
				
			
			if closest_points[2] == cx2_north and closest_points[3] == cy2_north:
				closest_points[2] += choice_x2
				e_vec = up_vec
				#closest_points[3] += choice_y
			elif closest_points[2] == cx2_south and closest_points[3] == cy2_south:
				closest_points[2] += choice_x2
				e_vec = down_vec
				#closest_points[3] += choice_y
			elif closest_points[2] == cx2_east and closest_points[3] == cy2_east:
				#closest_points[2] += choice_x
				e_vec = right_vec
				closest_points[3] += choice_y2
			elif closest_points[2] == cx2_west and closest_points[3] == cy2_west:
				#closest_points[2] += choice_x
				closest_points[3] += choice_y2
				e_vec = left_vec
				
			arr[closest_points[1]][closest_points[0]] =  1 #6
			arr[closest_points[3]][closest_points[2]] =  1 #6
			#print(arr[closest_points[1]][closest_points[0]])
			
   
			#establishing the direction
			#vec_x, vec_y = vec_maker(closest_points)
			
			
			
			#decides whether the tunnel between two room will be top right or bottom left compared to the center of the rooms
			#print(closest_points)
			
			sx = closest_points[0]
			sy = closest_points[1]
			ex = closest_points[2]
			ey = closest_points[3]
			tunnels.append((sx,sy,ex,ey,s_vec,e_vec))
			
	#symbol_display(arr)
			
	#print(tunnels)
	for i in tunnels:
		#print('yes')
		cross(arr,i[0],i[1],i[2],i[3],i[4],i[5])
	
				
		
				

	#symbol_display(arr)	
			


			
def BSP(floor, splits):
	#This fuction splits a two dimensional array into a bunch of small squares 
	#using a queue to add smaller squares and remove larger squares that the smaller ones were solit from
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
	
	
	
	while len(areas) != splits:
		#print(areas)
		#print()
		rand = int(random.random() * 2)
		#print(rand)
		if len(areas)%2 == rand:
			
	
			new_w = random.randint(arr_w//2,int(arr_w * .6))
			areas.append([arr_x,arr_y,new_w,arr_h])
			areas.append([arr_x + new_w - 1,arr_y,arr_w - new_w + 1,arr_h])
			#borders.append([arx,ary,nw,arh])
			#borders.append([arx + nw - 1,ary,arw-nw,arh])
				
			
				
			
		else:
			new_h = random.randint(arr_h//2,int(arr_h * .6))
			areas.append([arr_x,arr_y,arr_w,new_h])
			areas.append([arr_x,arr_y + new_h - 1,arr_w,arr_h - new_h + 1])
			#borders.append([arx,ary,arw,nh])
			#borders.append([arx,ary + nh - 1,arw,arh - nh + 1])
			
		areas.pop(0)
		arr_x = areas[0][0]
		arr_y = areas[0][1]
		arr_w = areas[0][2]
		arr_h = areas[0][3]
		
		
	#print(areas)
	#print('done')
	
	return areas
	
			


				
				
def floor_maker(grid,rooms,borders):
    #x0,y1,w2,h3
	grid_w = len(grid[0]) - 1
	grid_h = len(grid) - 1
	for i in borders:
		
		rw = 8 #int(i[2] * (random.randint(40,70)/100)) 
		rh = 6 #int(i[3] * (random.randint(40,70)/100)) 
		#the plus one and minus one is so rooms don't touch the edge of the grid'
		rx = random.randint(i[0] + 1,(i[0] + i[2] - rw) - 1)
		ry = random.randint(i[1] + 1,(i[1] + i[3] - rh) - 1)
		#print([rx,ry,rw,rh])
		rooms.append([rx,ry,rw,rh])
	
	#tunnel_maker_b(grid,rooms)
	
	for i in rooms:
		paver(grid,i)
	
	tunnel_maker_b(grid,rooms)
	
	return grid
		
	


ROWS = 40
COLS = 80
SPLITS = 3
		
#print(AABB([0,0,5,6],[2,7,2,2]))
#symbol_display(empty_map(20,19,[]))

arr = empty_map(ROWS,COLS,[])
barr = empty_map(ROWS,COLS,[])


bord = BSP(barr,SPLITS)

BSP_display(bord,barr)
	
#print(bord,end = '\n\n')
symbol_display(floor_maker(arr,[],bord))
#room_maker(num,carr,[])
