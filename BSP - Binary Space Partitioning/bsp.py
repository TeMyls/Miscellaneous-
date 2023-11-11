import random



def empty_map(rows,columns,empty_arr):
    for i in range(rows):
	    empty_arr.append([0]*columns)
    return empty_arr

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

ROWS = 40
COLS = 80
SPLITS = 3

arr = empty_map(ROWS,COLS,[])
barr = empty_map(ROWS,COLS,[])


bord = BSP(barr,SPLITS)

BSP_display(bord,barr)
