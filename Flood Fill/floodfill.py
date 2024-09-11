import time
import console

def empty_map(rows,columns,empty_arr):
	for i in range(rows):
		empty_arr.append([0]*columns)
			
	return  empty_arr
			

			

			

def display(arr):
	
	for i in arr:
		print(i)
		

		
	
		
def symbol_display(arr):
	h=''
	for i in arr:
		for j in i:
			
			if j == 0:
				h = h + '⬜️'
			if j == 1:
				h = h +  '🟥'
			
		h = h + '\n'
	print(h)

def flood_fill_i(arr, row, col):
	w = len(arr)
	h = len(arr[0])
	#BFS flood fill
	#queue
	
	visited = []
	kyu = []
	kyu.append((row,col))
	while kyu:
		#print(kyu)
		
		
		
		cur = kyu.pop(0)
		
		
		if cur[0] >= w or cur[0] < 0 or cur[1] >= h or cur[1] < 0 or	arr[cur[0]][cur[1]] != 0:
			continue
		else:
			
			arr[cur[0]][cur[1]] = 1
			kyu.append((cur[0] + 1, cur[1]))
			kyu.append((cur[0] - 1, cur[1]))
			kyu.append((cur[0], cur[1] + 1))
			kyu.append((cur[0], cur[1] - 1))
			console.clear()
			symbol_display(arr)
			
			time.sleep(.1)
	

def all_cells_filled(arr):
	tally = 0
	total = 0
	
	for i in arr:
		tally += i.count(0)
		total += len(i)
	
	#The goal os to get rid of all the empty spaces, or zeros
	return total - tally == total
	
	
def floodFillHelper(image, x, y, color, newColor):
	m = len(image)
	n = len(image[0])

	if image[x][y] == color:
		image[x][y] = newColor
		console.clear()
		symbol_display(arr)
		
		time.sleep(.1)
		if x >= 1:
			#left
			floodFillHelper(image, x - 1, y, color, newColor)
		if y >= 1:
			#up
			floodFillHelper(image, x, y - 1, color, newColor)
		if x + 1 < m:
			floodFillHelper(image, x + 1, y, color, newColor)
		if y + 1 < n:
			floodFillHelper(image, x, y + 1, color, newColor) 

def flood_fill_r(image, x, y, newColor):
	color = image[x][y]
	if color != newColor:
		floodFillHelper(image, x, y, color, newColor)
	return image
	
	
arr = empty_map(16,16,[])
flood_fill_i(arr,10,2)
#flood_fill_r(arr,10,2,1)
