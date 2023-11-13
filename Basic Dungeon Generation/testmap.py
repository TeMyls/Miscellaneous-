import random



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
			else:
				h = h + '. '
			
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
			

def pathways(x,y,arr,sx,sy,ex,ey):
  #actual tunnels
	grid_w = len(arr[0]) - 1
	grid_h = len(arr) - 1
	for row in range(sy,ey + 1):
		for col in range(sx,ex + 1):
			
			#if col < grid_w and row < grid_h:
			if col == x:
				arr[row][col] = 1
		
			if row == y:
				arr[row][col] = 1
			
		
			
def tunnel_maker(arr,rooms):

	#x0,y1,w2,h3
	tunnels = []
	#these exist to limit the area searched in the array to build tunnels
	sx,ex,sy,ey = 0,0,0,0
	#assumes more than 3 rooms
	for i in range(len(rooms)-1):
		
		
		#centers of two rooms
		cx1 = (rooms[i][0] + rooms[i][0] + rooms[i][2])//2
		cy1 = (rooms[i][1] + rooms[i][1] + rooms[i][3])//2
		
		cx2 = (rooms[i+1][0] + rooms[i+1][0] + rooms[i+1][2])//2
		cy2 = (rooms[i+1][1] + rooms[i+1][1] + rooms[i+1][3])//2
		#decides whether the tunnel between two room will be top right or bottom left compared to the center of the rooms
		choice1 = random.random()
		#decides whether a third path will be added
		choice2 = random.random()
		#print(choice2)
		if choice1 > .5:
			#arr[cy2][cx1] = 2
			if cy2 <= cy1:
				sy = cy2
				ey = cy1
			if cy2 >= cy1:
				sy = cy1
				ey = cy2
			if cx2 <= cx1:
				sx = cx2
				ex = cx1
				
			if cx2 >= cx1:
				sx = cx1
				ex = cx2
			
			tunnels.append((cx1,cy2,sx,sy,ex,ey))
			#print('a')
		else:
			#arr[cy1][cx2] = 2
			if cy2 <= cy1:
				sy = cy2 
				ey = cy1 
			if cy2 >= cy1:
				sy = cy1 
				ey = cy2 
			if cx2 <= cx1:
				sx = cx2 
				ex = cx1 
				
			if cx2 >= cx1:
				sx = cx1 
				ex = cx2 
			#print('b')
			tunnels.append((cx2,cy1,sx,sy,ex,ey))
		
		if choice2 > .8:
			#temp exists so the same room isn't selected
			temp = rooms.copy()
			temp.pop(i + 1)
			temp.pop(i)
			rand = random.randint(0,len(temp) - 1 )
			cx1 = (temp[rand][0] + temp[rand][0] + temp[rand][2])//2
			cy1 = (temp[rand][1] + temp[rand][1] + temp[rand][3])//2
			
			cx2 = (rooms[i][0] + rooms[i][0] + rooms[i][2])//2
			cy2 = (rooms[i][1] + rooms[i][1] + rooms[i][3])//2
			if cy2 <= cy1:
				sy = cy2 
				ey = cy1 
			if cy2 >= cy1:
				sy = cy1 
				ey = cy2 
			if cx2 <= cx1:
				sx = cx2 
				ex = cx1 
				
			if cx2 >= cx1:
				sx = cx1 
				ex = cx2 
			#print('b')
			tunnels.append((cx2,cy1,sx,sy,ex,ey))
		
			
	
	for i in tunnels:
		pathways(i[0],i[1],arr,i[2],i[3],i[4],i[5])
		
				
		
				

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
	grid_w = len(grid[0]) - 1
	grid_h = len(grid) - 1
	for i in borders:
		
		rw = int(i[2] * (random.randint(40,70)/100)) 
		rh = int(i[3] * (random.randint(40,70)/100)) 
		#the plus one and minus one is so rooms don't touch the edge of the grid'
		rx = random.randint(i[0] + 1,(i[0] + i[2] - rw) - 1)
		ry = random.randint(i[1] + 1,(i[1] + i[3] - rh) - 1)
		#print([rx,ry,rw,rh])
		rooms.append([rx,ry,rw,rh])
	'''
	
	for i in rooms:
		if i[2] < 3 or i[3] < 3:
			new_map = empty_map(ROWS,COLS,[])
			new_map_2 = empty_map(ROWS,COLS,[])
			floor_maker(new_map,[],BSP(new_map_2,SPLITS))
	'''
 
	tunnel_maker(grid,rooms)
	
	for i in rooms:
		paver(grid,i)
	symbol_display(grid)
	return rooms
		
	


ROWS = 40
COLS = 65
SPLITS = 3
		
#print(AABB([0,0,5,6],[2,7,2,2]))
#symbol_display(empty_map(20,19,[]))

arr = empty_map(ROWS,COLS,[])
barr = empty_map(ROWS,COLS,[])


bord = BSP(barr,SPLITS)

BSP_display(bord,barr)
	
#print(bord,end = '\n\n')
floor_maker(arr,[],bord)
#room_maker(num,carr,[])






