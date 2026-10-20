import math 
import random

'''
Copying a adjcency list 
	a = {
		 0: [5, 1, 6],
		 1: [0, 4],
		 2: [5, 3, 4],
		 3: [2, 4],
		 4: [2, 3, 1], 
		 5: [0, 2, 6],
		 6: [0, 5]
		 }
	
	the indexes would be each row
	the values would be in each column
		 they would be other indexes the current
		 index is connected to
	together they would form a graph/tree
	where each index has multiple values as childern
	
		 
	the above adjency list would translate to
		 
	Index: Array - ? is a filler integer,-1 
	0 :	 ?, 1, ?, ?, ?, 5, 6
	1 :	 0, ?, ?, ?, 4, ?, ?
	2 :	 ?, ?, ?, 3, 4, 5, ?
	3 :	 ?, ?, 2, ?, 4, ?, ?
	4 :  ?, 1, 2, 3, ?, ?, ?
	5 :	 0, ?, 2, ?, ?, ?, 6
	6 :	 0, ?, ?, ?, ?, 5, ?
	
'''

class AdjacencyMatrix:
	def __init__(self):
		self.edges = []
		self.directed = True
		
	def input_indexes(self, idx_dict):
		self.set_size(len(idx_dict))
		for i in idx_dict:
			for j in idx_dict[i]:
				self.add_child(i, j)
		
		
	def init_2D_array(self, rows,columns,color):
			return [[color]*columns for i in range(rows)]
		
	def set_size(self, node_count):
		self.edges = self.init_2D_array(node_count, node_count, -1)
	
	def display_tree(self):
		h=''
		for row in range(len(self.edges)):
			h += f"Index {str(row)}: "
			for col in range(len(self.edges[row])):
					ele = self.edges[row][col]
					if ele == -1:
						h = h + "_ "
					else:
						h = h + str(ele) + " "
			h = h + '\n'
		print(h)
	
	def add_node(self):
		# adds a row to the tree
		size = len(self.edges)
		
		# shrinking the size of each row by 1
		i = 0
		
		while i < size:
			self.edges[i].append(-1)
			i = i + 1
			
		self.edges.append([-1] * (size + 1))
		
	def delete_node(self, node_idx):
		size = len(self.edges)
		if node_idx > size - 1:
			return
			
		if node_idx < 0:
			return
			
		# removes a row to the tree
		
		# shrinking the size of each row by 1
		i = 0
		j = 0
		while i < size:
			
				
			#correcting the node
			while j < size:
				if self.edges[i][j] != -1:
					if self.edges[i][j] > node_idx:
						self.edges[i][j] = self.edges[i][j] - 1
					
				j = j + 1
				
			self.edges[i].pop(node_idx)
			i = i + 1
			j = 0
		
		self.edges.pop(node_idx)
		
	def add_child(self, parent_idx: int, child_idx: int):
		size = len(self.edges)
		if child_idx > size - 1 or child_idx < 0:
			return
			
		if parent_idx >= size or parent_idx < 0:
			return
			
		if parent_idx == child_idx:
			return
			
		# no undirected graphs
		if self.directed:
			if self.edges[child_idx][parent_idx] == parent_idx:
				return
			
			self.edges[parent_idx][child_idx] = child_idx
			
		else:
			
			self.edges[parent_idx][child_idx] = child_idx
			self.edges[child_idx][parent_idx] = parent_idx
		
	def remove_child(self, parent_idx: int, child_idx: int):
		# the parent is a row
		# the child is a column
		size = len(self.edges)
		if child_idx >= size:
			return
			
		if parent_idx >= size:
			return
			
		if parent_idx == child_idx:
			return
			
		if self.directed:
			self.edges[parent_idx][child_idx] = -1
		else:
			self.edges[parent_idx][child_idx] = -1
			self.edges[child_idx][parent_idx] = -1
		
	def traverse(self, idx, is_bfs = False):
		visited = [idx]
		deque = [idx]
		while deque:
			parent = -1
			print("Deque", deque)
			if is_bfs:
				parent = deque.pop(0)
			else:
				parent = deque.pop()
			
			
			for child in self.edges[parent]:
				if child == -1:
					continue
					
				if child in visited:
					continue
				
				visited.append(child)
				deque.append(child)
		return visited
	
	
	

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

	wall_color:'# ',
	floor_color:'. ',
	#player_color:'@',
	unknown_color:'? ',
	#up_stairs_color:'>',
	#enemy_color: 'V',
	#down_stairs_color:'<'
	
	
	
}

def DDA(x0, y0, x1, y1): 

	# find absolute differences 
	dx = x1 - x0
	dy = y1 - y0
	# find maximum difference 

	steps = max(abs(dx), abs(dy))
	
	# calculate the increment in x and y 
	xinc = dx/steps 
	yinc = dy/steps 

	# start with 1st point 
	x = x0
	y = y0
	# make a list for coordinates 
	coorinates = [] 

	coorinates.append([x, y]) 
	for _ in range(steps): 
		
		
		
		# increment the values 
		x = x + xinc 
		y = y + yinc 
		
		# append the x,y coordinates in respective list 
		coorinates.append([math.floor(x), math.floor(y)]) 
		
	return coorinates

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
					h = h + str(j) + " "
		h = h + '\n'
	print(h)

def display_true(arr):
	h=''
	for i in arr:
		for j in i:
				h = h + str(j) + " "
		h = h + '\n'
	print(h)
	
def connect_tree(centers, tree, grid, color):
	for y in range(len(tree.edges)):
		for x in range(len(tree.edges[y])):
			if tree.edges[y][x] == -1:
				continue
			y1, x1 = centers[y]
			y2, x2 = centers[x]
			coords = DDA(x1, y1, x2, y2)
			
			for xy in coords:
				cx, cy = xy
				grid[cy][cx] = color
				
def MST(centers, grid):
	n = len(centers)
	tree = AdjacencyMatrix()
	tree.directed = True
	for _ in range(n):
		tree.add_node()

	start = random.randint(0, n - 1)
	in_tree = {start}

	while len(in_tree) < n:
		best = None  # (distance, a, b)
		for a in in_tree:
			y1, x1 = centers[a]
			for b in range(n):
				if b in in_tree:
					continue
				y2, x2 = centers[b]
				d = distance_to(x1, y1, x2, y2)
				if best is None or d < best[0]:
					best = (d, a, b)

		_, a, b = best
		tree.add_child(a, b)
		in_tree.add(b)

	return tree
	
	
def get_area_centers(areas, grid, color):
	
	center = [] 
	for i in range(len(areas)):
		
		area = areas[i]
		
		x1 = area[0]
		y1 = area[1]
		x2 = area[2]
		y2 = area[3]
		
		cx = math.floor(lerp(x1, x2, 0.5))
		cy = math.floor(lerp(y1, y2, 0.5))
		
		center.append([cy, cx])
		grid[cy][cx] = str(i) #color
		
	return center

def outline_areas(areas, grid, color):
	
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
					grid[row][col] = color
				elif row == y1 or row == y2:
					grid[row][col] = color
				
					
	return grid



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
					random.randint(45, 55)/100
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
					random.randint(45, 55)/100
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
	
	return areas
			
	
	
	


grid = create_2D_array(20, 20, floor_color)				
areas = BSP(grid, 16)


grid = outline_areas(areas, grid, floor_color)
centers = get_area_centers(areas, grid, wall_color)
tree = MST(centers, grid)
connect_tree(centers, tree, grid, wall_color)
get_area_centers(areas, grid, floor_color)
display(grid)
#display_true(grid)
tree.display_tree()



	




			
	
				
				 