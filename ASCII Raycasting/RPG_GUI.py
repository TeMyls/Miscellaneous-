import math
import time
import console
import random
import os
#from maze_gen import *

class nodeGraph:
	def __init__(self):
		
		# An Dictionary/Adjacency List of edges
		# The keys are the indexes of the container
		# The values are a list of vertex connections
		# Edges is a directed graph
		# Example
		
		"""
		Parent: 0 Childern: [3, 1, 2]
		Parent: 1 Childern: [4]
		Parent: 2 Childern: [5]
		Parent: 3 Childern: [7]
		Parent: 4 Childern: []
		Parent: 5 Childern: [6]
		Parent: 6 Childern: []
		Parent: 7 Childern: []
		"""
		# if it were an undirected graph
		"""
		Parent: 0 Childern: [3, 1, 2]
		Parent: 1 Childern: [4, 0]
		Parent: 2 Childern: [5, 0]
		Parent: 3 Childern: [7, 0]
		Parent: 4 Childern: [1]
		Parent: 5 Childern: [6, 2]
		Parent: 6 Childern: [5]
		Parent: 7 Childern: [3]
		"""
		
		self.edges = {
		
		}
		
	def display(self):
		for key in self.edges:
			print(key, self.edges[key])
		
	def traverse(self, node: any, is_bfs: bool):
		visited = [node]
		deque = [node]
		tree = self.edges
		#print("yop" , tree)
		
		while deque:
			#print(deque)
			item = deque.pop(0) if is_bfs else deque.pop()
			if tree.get(item):
				for i in range(len(tree[item]) - 1,-1,-1):
					if tree[item][i] not in visited:
						deque.append(tree[item][i])
						visited.append(tree[item][i])
						

		#print(visited)
		return visited
		
	def get_parent(self, idx, is_bfs):
		root_node = 0
		visited = [root_node]
		deque = [root_node]
		#print("9" ,self.edges)
		
		while deque:
			#print(deque)
			item = deque.pop(0) if is_bfs else deque.pop()
			if self.edges.get(item):
				for i in range(len(self.edges[item]) - 1,-1,-1):
					child = self.edges[item][i]
					if child not in visited:
						deque.append(child)
						visited.append(child)
						if child == idx:
							return item
		return -1
	def edit_index(self, idx, parent_idx = -1):
		pass
		
		#self.edges[idx] = []
		
	def add_index(self, idx, parent_idx = -1):
		self.edges[idx] = []
		
		if parent_idx > -1:
			self.add_child(idx, parent_idx)
		
	
		
	def add_child(self, child_idx, parent_idx):
		if len(self.edges) > 1:
			#if self.edges.get(parent_idx) and parent_idx != child_idx:
				#if child_idx not in self.edges[parent_idx]:
				self.edges[parent_idx].append(child_idx)
					# print("yippe")
		
	def remove_child(self, child_idx, parent_idx):
		if len(self.edges) > 1:
			if self.edges.get(parent_idx) and parent_idx != child_idx:
				if child_idx in self.edges[parent_idx]:
					self.edges[parent_idx].remove(child_idx)
			
		
	
		
	def delete_index(self, idx):
		
		if len(self.edges) > 0:
			
			if idx > -1:
				idx = idx % len(self.edges.keys())
				#print(idx)
				
				
				#--------------------------------------
				# updating the edges list
				# self.edges is an adjcency list
				# print("remove vert")
				# getting rid of the deleted vertex in the dictionary
				self.edges.pop(idx)

				dict_new = {}
				for key in self.edges:
					#getting rid of the deleted vertex in the vertex's array
					if idx in self.edges[key]:
						self.edges[key].remove(idx)
						#self.edge_options[key].pop(v_ind)
						#reorganizing the dictionary with updated indexes to reflect deletion
						for i in range(len(self.edges[key])):
							if self.edges[key][i] > idx:
								self.edges[key][i] = self.edges[key][i] - 1
								#filling the replacement dictionary
								if key > idx:
									#print('ye')
									new_key = key - 1
									dict_new[new_key] = self.edges[key]
								else:
									#print('ne')
									dict_new[key] = self.edges[key]
						self.edges = dict_new
						#----------------------------------------------------------------------------------------------------

		
# GUIM end
#_____________________________________		
class GUI_Manager:
	def __init__(self):
		# space sets of x1-y1-x2-y2 
		self.space_tree = nodeGraph()
		
		# Sets of x1-y1-x2-y2 
		# the widget area itself
		self.areas = []
		# text anchor, internal anchor, external anchor
		# Sets of either C, N, NE, E, SE, S, SW, W, or NE:
		# or
		# N, NE, NW, EN, E, ES, WN, W, WS, S, SE, SW, WNW, NEN, SES, WSW: if external
			# describes how a string or another x1-y1-x2-y2 is positioned inside or outside a x1-y1-x2-y2
			# default "" or Center
			# designates the location of the widget in the sub space
		self.tanchors = []
		self.ianchors = []
		self.eanchors = []
		
		
		# Sets of "", X", "Y", or "Both"
			# default: ""
			# makes the widget take up more parts of it's sub space, horizontally, vertically or both
		self.fills = []
		# the color of the widget and the area it inhabits
		self.fgs = []
		
		self.grid = self.empty_map(5, 5, "?")
		
		# height percentage of parent
		self.wpcts = []
		# width percentage of parent
		self.hpcts = []
		# minimal size percentage of parent, always squart
		self.mnpcts = []
		# individual strings
		self.texts = []
		
		

		
		#self.add_area()
	def animate(self, wait = False):
		if wait:
			time.sleep(.5)
		# for Windows
		#os.system('cls')

		# for Pythonista
		console.clear()
	
	def get_dimensions(self, parent_idx, idx):
		child = self.areas[idx]
		aw = round(abs(child[2] - child[0]))
		ah = round(abs(child[3] - child[1]))
		
		parent = self.areas[parent_idx]
		uw = round(abs(parent[2] - parent[0]))
		uh = round(abs(parent[3] - parent[1]))
		
		return aw, ah, uw, uh
		
	def get_iAnchor(self, parent_idx, idx):
		
		aw, ah, uw, uh = self.get_dimensions(parent_idx, idx)
		parent = self.areas[parent_idx]

		
		top_x = parent[0]
		top_y = parent[1]
		mid_x = parent[0] + round(uw/2 - aw/2)
		mid_y = parent[1] + round(uh/2 - ah/2)
		end_x = parent[2] - aw
		end_y = parent[3] - ah
		
		
		
		
		return {
			"N"  : [mid_x, top_y],
			"NE" : [end_x, top_y],
			"NW" : [top_x, top_y],
			"C"  : [mid_x, mid_y],
			"E"  : [end_x, mid_y],
			"W"  : [top_x, mid_y],
			"S"  : [mid_x, end_y],
			"SE" : [end_x, end_y],
			"SW" : [top_x, end_y]
		}
		#return N, NE, NW, C, E, W, S, SE, SW
		
	def get_eAnchor(self, parent_idx, idx):
		
		#aw = round(abs(self.areas[idx][2] - self.areas[idx][0]))
		#ah = round(abs(self.areas[idx][3] - self.areas[idx][1]))
		aw, ah, uw, uh = self.get_dimensions(parent_idx, idx)
		parent = self.areas[parent_idx]
		#uw = round(abs(parent[2] - parent[0]))
		#uh = round(abs(parent[3] - parent[1]))
		
		top_x = parent[0]
		top_y = parent[1]
		mid_x = parent[0] + round(uw/2 - aw/2)
		mid_y = parent[1] + round(uh/2 - ah/2)
		end_x = parent[2] - aw
		end_y = parent[3] - ah
		
		
		return {
			
			"N"  : [mid_x, top_y - ah],
			"NE" : [end_x, top_y - ah],
			"NW" : [top_x, top_y - ah],
			
			"EN" : [end_x + aw, top_y],
			"E"  : [end_x + aw, mid_y],
			"ES" : [end_x + aw, end_y],
			
			"WN" : [top_x - aw, top_y],
			"W"  : [top_x - aw, mid_y],
			"WS" : [top_x - aw, end_y],
			
			"S"  : [mid_x, end_y + ah],
			"SE" : [end_x, end_y + ah],
			"SW" : [top_x, end_y + ah],
			
			"WNW" : [top_x - aw, top_y - ah],
			"NEN" : [end_x + aw, top_y - ah],
			"SES" : [end_x + aw, end_y + ah],
			"WSW" : [top_x - aw, end_y + ah]
			
		}
		
	def get_tAnchor(self, idx: int, text: str):
		
		
		parent = self.areas[idx]

		
		top_x = parent[0]
		top_y = parent[1]
		mid_x = parent[0] + math.floor((parent[2] - parent[0])/2 - len(text)/2)
		mid_y = parent[1] + math.floor((parent[3] - parent[1])/2)
		end_x = parent[2] - len(text)
		end_y = parent[3] - 1
		
		
		
		
		return {
			"N"  : [mid_x, top_y],
			"NE" : [end_x, top_y],
			"NW" : [top_x, top_y],
			"C"  : [mid_x, mid_y],
			"E"  : [end_x, mid_y],
			"W"  : [top_x, mid_y],
			"S"  : [mid_x, end_y],
			"SE" : [end_x, end_y],
			"SW" : [top_x, end_y]
		}
		
	def add_area(self, kwargs):
		
		
		has_x1 = kwargs.get("x1")
		has_y1 = kwargs.get("y1")
		has_x2 = kwargs.get("x2")
		has_y2 = kwargs.get("y2")
		
		has_area = kwargs.get("area")
		
		has_text = kwargs.get("text")
		
		has_fill = kwargs.get("fill")
		
		has_ianchor = kwargs.get("ianchor")
		has_eanchor = kwargs.get("eanchor")
		has_tanchor = kwargs.get("tanchor")
		
		# two strings one representing the space color and the othe the sub soace
		has_bg = kwargs.get("bg")
		has_fg = kwargs.get("fg")
		
		has_hpct = kwargs.get("hpct")
		has_wpct = kwargs.get("wpct")
		has_mnpct = kwargs.get("mnpct")
		
		
		has_parent = kwargs.get("pidx")
		#
		#print("This Parent", has_parent)
		
		if has_hpct:
			self.hpcts.append(has_hpct)
		else:
			self.hpcts.append(-1)
			
		if has_wpct:
			self.wpcts.append(has_wpct)
		else:
			self.wpcts.append(-1)
			
		if has_mnpct:
			self.mnpcts.append(has_mnpct)
		else:
			self.mnpcts.append(-1)
			
		# Sets of "", "X", "Y", or "Both"
			# default ""
			# makes the widget take up more parts of it's sub space, horizontally, vertically or both
		if has_fill:
			self.fills.append(has_fill)
		else:
			self.fills.append("")
		
		# Sets of either N, NE, E, C, SE, S, SW, W, or NE:
			# default C or Center
			# designates the location of the widget inside a space
		if has_ianchor:
				
			self.ianchors.append(has_ianchor)
		else:
			self.ianchors.append("")
			
		# Sets of either N, NE, E, C, SE, S, SW, W, or NE:
			# default C or Center
			# designates the location of the widget inside a space
		if has_tanchor:
				
			self.tanchors.append(has_tanchor)
		else:
			self.tanchors.append("")
			
		# Sets of either 
		# N, NE, NW, EN, E, ES, WN, W, WS, S, SE, SW, WNW, NEN, SES, WSW:
			# default ""
			# designates the location of the widget outside a space
		if has_eanchor:
				
			self.eanchors.append(has_eanchor)
		else:
			self.eanchors.append("")
			
		if has_fg:
			self.fgs.append(has_fg)
		else:
			self.fgs.append("•")
		
		
		
		idx = len(self.areas)
		self.space_tree.add_index(idx)
		if has_parent != None:
			self.space_tree.add_child(idx, has_parent)
			
		if has_area != None:
			self.areas.append(has_area)
		else:
			self.areas.append(self.get_box(-1, -1, -1, -1))
		
		if has_text != None:
			self.texts.append(has_text)
		else:
			self.texts.append("")
	
		parent_idx = self.space_tree.get_parent(idx, False)
		
		
		if parent_idx != -1:
			
			
			
			wpct = self.wpcts[idx]/100
			hpct = self.hpcts[idx]/100
			mnpct = self.mnpcts[idx]/100
			if self.mnpcts[idx] != -1:
				aw, ah, uw, uh = self.get_dimensions(parent_idx, idx)
				mn = min(uw, uh)
				if self.wpcts[idx] != -1:
					self.areas[idx] = [
															0, 0,
															mn * mnpct, mn * mnpct
														]
			else:
				
				aw, ah, uw, uh = self.get_dimensions(parent_idx, idx)
				if self.wpcts[idx] != -1:
					self.areas[idx] = [
															0, 0,
															uw * wpct, ah
														]
	
				aw, ah, uw, uh = self.get_dimensions(parent_idx, idx)
	
				if self.hpcts[idx] != -1:
					self.areas[idx] = [
															0, 0,
															aw, uh * hpct
														]
			
			aw, ah, uw, uh = self.get_dimensions(parent_idx, idx)
			directions = self.get_iAnchor(parent_idx, idx)
		
			if directions.get(self.ianchors[idx]):
				XY = directions[self.ianchors[idx]]
				self.areas[idx] = [
					XY[0], XY[1],
					XY[0] + aw, XY[1] + ah
				]
				
				is_top = self.ianchors[idx] == "N" or self.ianchors[idx] == "NW" or self.ianchors[idx] == "NE"
				
				is_bottom = self.ianchors[idx] == "S" or self.ianchors[idx] == "SW" or self.ianchors[idx] == "SE"
				
				is_left = self.ianchors[idx] == "W" or self.ianchors[idx] == "NW" or self.ianchors[idx] == "SW"
				
				is_right = self.ianchors[idx] == "E" or self.ianchors[idx] == "NE" or self.ianchors[idx] == "SE"
				
				if self.fills[idx] == "Y":
					
					if is_left:
					
						self.areas[idx] = [
							directions["NW"][0], 
							directions["NW"][1],
							directions["SW"][0] + aw, 
							directions["SW"][1] + ah
						]
						
				
						
					elif is_right:
						
						self.areas[idx] = [
							directions["NE"][0], 
							directions["NE"][1],
							directions["SE"][0] + aw, 
							directions["SE"][1] + ah
						]
						
						
						
				elif self.fills[idx] == "X":
					
					if is_top:
						
						self.areas[idx] = [
							directions["NW"][0], 
							directions["NW"][1],
							directions["NE"][0] + aw, 
							directions["NE"][1] + ah
						]
						
						
						
					elif is_bottom:
						
						self.areas[idx] = [
							directions["SW"][0], 
							directions["SW"][1],
							directions["SE"][0] + aw, 
							directions["SE"][1] + ah
						]
						
						
						
				elif self.fills[idx] == "Both":
				
					self.areas[idx] = [
						directions["NW"][0], 
						directions["NW"][1],
						directions["SW"][0] + aw, 
						directions["SW"][1] + ah,
					]
					
				
			
			
			aw, ah, uw, uh = self.get_dimensions(parent_idx, idx)
			directions = self.get_eAnchor(parent_idx, idx)
			
			if directions.get(self.eanchors[idx]):
				XY = directions[self.eanchors[idx]]
				self.areas[idx] = [
					XY[0], XY[1],
					XY[0] + aw, XY[1] + ah
				]
			
			
			
		return idx
		
	
	def render_areas(self):
		
		if self.space_tree.edges:
			root_node = 0
			area = self.areas[root_node]
			ow = abs(area[2] - area[0])
			oh = abs(area[3] - area[1])
			#len(self.grid)#
			#self.grid = self.empty_map(oh, ow, "@")
			deque = self.space_tree.traverse(0, True)
			#print(self.space_tree.edges)
			#print(deque, self.areas)
			while deque:
			
				item = deque.pop(0) 
				area = self.areas[item]
				x1, y1, x2, y2 = area
				self.set_box(x1, y1, x2, y2, self.fgs[item], self.grid)
				text = self.texts[item]
				t_anchor = self.tanchors[item]
				if text != "":
					if t_anchor != "":
						tx = math.floor((x2 - x1)/2)
						ty = math.floor((y2 - y1)/2)
						tx, ty = self.get_tAnchor(item, text)[t_anchor]
						tlen = len(text)
						for i in range(tlen):
							
							self.grid[ty][tx + i] = text[i]
				
							
			#self.display_true(self.grid)
			#print("fin")
		
		
	def display_grid(self):
		self.display_true(self.grid)
	
	def clear_console(self):
		# clearing the console
		#on windows
		os.system('cls')
		#on pythonista
		#console.clear()
		
	
	

	def empty_map(self, rows,columns,color):
		return [[color]*columns for i in range(rows)]
	
	def in_bounds(self, x, y, w, h):
		return -1 < x < w and -1 < y < h
		
	
		
	def display_data(self):
		
		if self.space_tree.edges:
			print("Edges")
			idxs = self.space_tree.traverse(0, False)
			while idxs:
				key = idxs.pop(0)
				print(f"Idx: {key}\n Internal Anchor:  {self.ianchors[key]}\nExternal Anchor:  {self.eanchors[key]}\n Fills: {self.fills[key]}\nArea: {self.areas[key]}\n\n FG Color: {self.fgs[key]}\n")
		
			
			

		
		
	def display_true(self, arr):
		h=''
		for i in arr:
			for j in i:
					h = h + str(j) #+ " "
			h = h + '\n'
		print(h)
		
	def set_box(self, x1, y1, x2, y2, color, arr):
		for x in range(int(x1), int(x2)):
			for y in range(int(y1), int(y2)):
				if self.in_bounds(x, y, len(arr[0]), len(arr)):
					arr[y][x] = color
				
		
	def get_box(self, x1, y1, x2, y2):
		return [x1, y1, x2, y2]
		
	
		#return N, NE, NW, C, E, W, S, SE, SW
	
	
	
	def remove_area(self, idx):
		self.eanchors.pop(idx)
		self.ianchors.pop(idx)
		self.fills.pop(idx)
		self.space_tree.remove_child(idx)

# GUIM end
#_____________________________________		
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
		
def empty_map(rows,columns,color):
	return [[color]*columns for i in range(rows)]

def in_bounds(x, y, w, h):
	return -1 < x < w and -1 < y < h
	
def display_board(grid):
	#displays map as numbers
	
	
	h=''
	for y in range(len(grid)):
	
		h += "|"
		for x in range(len(grid[y])):
			
				
				h += str(grid[y][x]) + " "
				
		h = h + '|\n'
	print(h)	
	
	
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
	valid_tiles = [floor_color, enemy_color]
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
		
		

		
def rand_choice(arr, weight_ls, k):
	return random.choices(arr,weights = weight_ls,k = k)

	
def flatten(list_of_lists):
	return [ele for ls in list_of_lists for ele in ls]
	
def get_cell_colors(arr2d, color):
	cells = []
	for y in range(len(arr2d)):
		for x in range(len(arr2d[y])):
			if arr2d[y][x] == color:
				cells.append([x, y])
	return cells
	
def get_ready(units: list):
	# Fill initiative bars
	
	ready = []
	while True:
		for unit in units:
			unit["time"] += unit["speed"]
			
		ready = [u for u in units if u["time"] >= 100]
		if ready:
			break
	return  ready
	
def start_ready(ready: list):
	if ready:
		# decide who moves
		print("ready", ready)
		actor = ready[0]
		for unit in ready:
			if unit["time"] > actor["time"]:
				actor = unit
				
		print("{} acts".format( actor["name"] ))
	
		# Spend initiative
		actor["time"] -= actor["time"]
		print([(u["name"], u["time"]) for u in units])
		print()
		
def make_unit(name : str, speed: int, hp: int, dmg: int ):
	return {
		"name" : name,
		"speed": speed,
		"hp": hp,
		"time" : 0
	}


'''
units = [
	
	make_unit("Hero", 20),
	make_unit("Goblin", 30),
	make_unit("Mage", 10),
	make_unit("Thief", 45)

]


for turn in range(50):
	print(f"Turn {turn + 1}")
	ready = get_ready(units)
	start_ready(ready)
'''		
	
		
	
Z = GUI_Manager()
Z.grid = Z.empty_map(16, 44, "X")


base = {
			# ints
			"area": Z.get_box(
				0,
				0,
			 	len(Z.grid[0]),
				len(Z.grid),
				
				),
			"fill": "",
			"ianchor": "C",
			"fg": ".",
			"pidx":None
			
}

first = Z.add_area(base)

one = {}
one["area"] = Z.get_box(0, 0, 22, 8)
one["wpct"] = 90
one["hpct"] = 90
one["fg"] = "*"
one["ianchor"] = "C"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = first

second = Z.add_area(one)

one = {}
one["area"] = Z.get_box(0, 0, 22, 8)
one["wpct"] = 100
one["hpct"] = 40
one["fg"] = "u"
one["ianchor"] = "S"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = second

third = Z.add_area(one)

one = {}
one["area"] = Z.get_box(0, 0, 22, 8)
one["wpct"] = 90
one["hpct"] = 60
one["fg"] = "n"
one["ianchor"] = "N"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = second

screen_idx = Z.add_area(one)

one = {}
one["area"] = Z.get_box(0, 0, 22, 8)
one["wpct"] = 45
one["hpct"] = 45
one["text"] = "Player 1 Box"
one["tanchor"] = "N"
one["fg"] = "~"
one["ianchor"] = "NW"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = third

player_1_box = Z.add_area(one)


one = {}
one["area"] = Z.get_box(0, 0, 22, 8)
one["wpct"] = 45
one["hpct"] = 45
one["text"] = "Player 2 Box"
one["tanchor"] = "N"
one["fg"] = "~"
one["ianchor"] = "NE"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = third

player_2_box = Z.add_area(one)

one = {}
one["area"] = Z.get_box(0, 0, 22, 8)
one["wpct"] = 45
one["hpct"] = 45
one["text"] = "Player 3 Box"
one["tanchor"] = "N"
one["fg"] = "~"
one["ianchor"] = "SW"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = third

player_3_box = Z.add_area(one)

one = {}
one["area"] = Z.get_box(0, 0, 22, 8)
one["wpct"] = 45
one["hpct"] = 45
one["text"] = "Player 4 Box"
one["tanchor"] = "N"
one["fg"] = "~"
one["ianchor"] = "SE"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = third

player_4_box = Z.add_area(one)


one = {}
one["area"] = Z.get_box(0, 0, 22, 8)
one["wpct"] = 100
one["hpct"] = 25
one["text"] = " Player 1 "
one["tanchor"] = "N"
one["fg"] = "/"
one["ianchor"] = "N"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = player_1_box

player_1 = Z.add_area(one)

one = {}
one["area"] = Z.get_box(0, 0, 22, 8)
one["wpct"] = 100
one["hpct"] = 25
one["text"] = " Player 2 "
one["tanchor"] = "N"
one["fg"] = "/"
one["ianchor"] = "N"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = player_2_box

player_2 = Z.add_area(one)

one = {}
one["area"] = Z.get_box(0, 0, 22, 8)
one["wpct"] = 100
one["hpct"] = 25
one["text"] = " Player 3 "
one["tanchor"] = "N"
one["fg"] = "/"
one["ianchor"] = "N"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = player_3_box

player_3 = Z.add_area(one)


one = {}
one["area"] = Z.get_box(0, 0, 22, 8)
one["wpct"] = 100
one["hpct"] = 25
one["text"] = " Player 4 "
one["tanchor"] = "N"
one["fg"] = "/"
one["ianchor"] = "N"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = player_4_box

player_4 = Z.add_area(one)



one = {}
one["area"] = Z.get_box(0, 0, 22, 8)
one["wpct"] = 90
one["hpct"] = 90
one["fg"] = "_"
one["ianchor"] = "N"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = screen_idx

display_idx = Z.add_area(one)

one = {}
one["area"] = Z.get_box(0, 0, 5, 5)
#one["wpct"] = 25
#one["hpct"] = 90
one["mnpct"] = 25
one["fg"] = "%"
one["ianchor"] = "NW"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = display_idx

map_idx = Z.add_area(one)


one = {}
one["area"] = Z.get_box(0, 0, 22, 8)
#one["wpct"] = 50
#one["hpct"] = 100
one["mnpct"] = 90
one["text"] = " Enemy "
one["fg"] = "\\"
one["tanchor"] = "C"
one["ianchor"] = "C"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = display_idx

sub_screen = Z.add_area(one)


#Z.set_text(player_1, "Player 1", "NW")
#Z.set_text(player_2, "Player 2", "NW")
#Z.set_text(player_3, "Player 3", "NW")
#Z.set_text(player_4, "Player 4", "NW")

#Z.set_text(second, "Player 1", "NW")

#Z.display_data()
#______________________________________

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

map_true = [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,1,0,0,1,1,1,1,0,0,0],
	[0,0,0,0,0,1,0,0,1,1,1,1,0,0,0],
	[0,1,1,1,1,1,0,0,1,0,0,1,0,1,0],
	[0,1,1,1,1,0,0,0,1,1,0,1,1,1,0],
	[0,1,1,1,1,0,0,0,1,0,0,1,1,1,0],
	[0,0,0,1,1,0,0,0,1,0,0,1,0,1,0],
	[0,0,0,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,0,0,1,1,1,1,1,1,1,1,0,0,1,0],
	[0,0,0,1,1,1,1,0,1,1,1,0,0,1,0],
	[0,0,0,1,1,1,1,1,1,1,1,0,0,1,0],
	[0,0,0,1,0,0,0,0,1,0,1,0,0,1,0],
	[0,0,0,1,0,0,0,1,1,1,1,0,0,1,0],
	[0,0,0,1,0,0,0,1,1,1,1,1,1,1,0],
	[0,0,0,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

]

#map_true = make_maze(16,16)

floor_color = 1
wall_color = 0
player_color = 7
enemy_color = 6

#ASCII_brightness = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
#ASCII_brightness = "WM*zcvu-_+^'"
#ASCII_brightness = "WMzc+:'"
#print(ASCII_brightness)
ASCII_brightness = "█▓▒░"

colors = {
	#wall
	wall_color:'#',
	#floor
	floor_color:'.',
	#player
	player_color:'@',
	
	enemy_color:"C"
	
	
	
	
}




floor_cells = get_cell_colors(map_true, floor_color)
	
enemy_cells = []
print(floor_cells)
e = 5
while e != 0:
	ex, ey = floor_cells.pop(random.randint(1, len(floor_cells) - 1))
	enemy_cells.append([ex, ey])
	map_true[ey][ex] = e
	e -= 1
	

angle_sym = {
	0: ">",
	90: "V",
	180: "<",
	270: "A",
	360: ">",
}

px, py = rand_choice(
	floor_cells, 
	[1] * len(floor_cells),
	1
)[0] 
'''
rand_choice(
	floor_cells, 
	[1] * len(floor_cells),
	1
)[0] 

floor_cells.pop(random.randint(1, len(floor_cells) - 1))
'''

rangle = rand_choice(
	list(angle_sym.keys()), 
	[1] * len(angle_sym), 
	1
)[0]
'''
rand_choice(
	list(angle_sym.keys()), 
	[1] * len(angle_sym), 
	1
)[0]

floor_cells.pop(random.randint(1, len(floor_cells) - 1))
'''

print(px, py, rangle)

player = {

	"x":px,
	"y":py,
	"tx":px + .5,
	"ty":py + .5,
	"fov":90,
	"angle": rangle,
	"ground": floor_color,
	"playing":True
}
rows = Z.areas[display_idx][3] - Z.areas[display_idx][1]
cols = Z.areas[display_idx][2] - Z.areas[display_idx][0]

angle_rays = ray_angles(
	cols,
	player["fov"],
	player["tx"],
	player["ty"]
)

#print("rows", rows , "cols", cols, len(angle_rays))

#map_display = empty_map()



display_string = ""
# map_true[player['y']][player['x']] = player_color


is_animated = True
dir = ""
#should be 45 or 90
angle_inc = 90
display_screen = True
display_map = True

Z.display_true(map_true)
Z.render_areas()
Z.display_grid()

# below to test the layout
#while False:
while player["playing"]:
	Z.clear_console()
	
	player_names = [
		"player_1"
		"player_1",
		"player_1",
		"player_1",
		
	]
	
	on_enemy = [player["x"], player["y"]] in enemy_cells
	if on_enemy:
		Z.texts[ screen_idx ]= f' The Party Encouters!!! '
		
	else:
		Z.texts[ screen_idx ]= f' X: {player["x"]} Y: {player["y"]} Angle: {player["angle"]} '
		
	Z.tanchors[ screen_idx ] = "S"
	#Z.texts[ player_1 ]= "Encounters"
	Z.render_areas()
	
	#Z.render_areas()
	
	#map_display = empty_map(,rows, floor_color)

	
	#print(player)
	
	distances = []
	hit_coords = []
	
	
	max_dim = max(len(map_true),len(map_true[0]))
	for ang in angle_rays:
		#DDA by a fixed value
		#by dividing it's increments by a precision value'
		#the resulting line or raycast drawn will be more accurate to the true distance it covers
		precision = 300
		raycos = math.cos(ang + degrees_to_radians(player["angle"]))/precision
		
		raysin = math.sin(ang + degrees_to_radians(player["angle"]))/precision
		
		data = DDA_raycast(map_true,player["tx"],player["ty"],raycos,raysin)
		if data:
			dist = data[0]
			hit_coord = data[1]
			#fisheye correction
			dist *= math.cos(raycos)
			distances.append(dist)
			hit_coords.append(hit_coord)
	
	#print(player.true_x, player.true_y)
	#print(hit_coords, len(hit_coords))
	#print(distances, len(distances))
	#print(max_dim)
		
		
	
		#
		#self.render_floors(i,display_grid,map_grid,line_len,angles[i],raycos,raysin,player)
		
		
	for i in range(len(distances)):
		percent = ((max_dim - distances[i])/(max_dim  + distances[i]))
		#print(percent)
		#line_len = round(self.rows * percent)
		#line_len = round(rows * ((max_dim - distances[i])/max_dim))/1.2
		line_len = round(rows * ((distances[i])/max_dim) * .75)
		
		#line_len = distances[i]%len(map_grid)
		#line_len = round(self.rows * ((max_dim - distances[i])/max_dim))
		
		bright_index = round((1 - percent) * (len(ASCII_brightness) - 1))
		#bright_index = round((percent) * (len(ASCII_brightness) - 1))
		#print(bright_index, len(ASCII_brightness))
		choice_color = ASCII_brightness[bright_index]
		
		raycos = math.cos(angle_rays[i] + degrees_to_radians(player["angle"]))
		
		raysin = math.sin(angle_rays[i] + degrees_to_radians(player["angle"]))
		
		#wall drawing
		#y = Z.areas[display_idx][1]
		x = Z.areas[display_idx][0] + i
		#if in_bounds(x, y,len(map_true[0]),len(map_true)):
		#start y
		# y = round((len(grid) - size)/2)
		# end_y = len(grid) - y
		#
		y = round(Z.areas[display_idx][1] + line_len/2)
		end_y = round(Z.areas[display_idx][3] - line_len/2)
		#y = Z.areas[display_idx][1] + round((len(grid) - size)/2)
		#print(x, y, end_y)
		while y < end_y:
			
			Z.grid[y][x] = choice_color
			y = y + 1	#draw_vertical_line(Z.grid,i,choice_color,line_len)
		#floor drawing
		
		#self.render_floors(i,display_grid,map_grid,line_len,angles[i],raycos,raysin,player)
		
	# minimap
	x1 = Z.areas[map_idx][0]
	y1 = Z.areas[map_idx][1]
	x2 = Z.areas[map_idx][2]
	y2 = Z.areas[map_idx][3]
	# minimap middle
	mx = math.floor(x1 + (x2 - x1)/2)
	my = math.floor(y1 + (y2 - y1)/2)
	px = round(player['x'] - (x2 - x1)/2)
	py = round(player['y'] - (y2 - y1)/2)
	#print("Ewh", x1, y1, x2, y2, mx, my)
	#map_true[player['y']][player['x']]
	for y in range(y1, y2):
		#px = round(player['x'] - (x2 - x1)/2)
		#py = round(player['y'] - (y2 - y1)/2)
		
		py = player['y'] + (my - y) * -1
		for x in range(x1, x2):
			px = player['x'] + (mx - x) * -1
			#print(x - x1, y - y1)
			#print(px, py)
			if in_bounds(px, py,len(map_true[0]),len(map_true)):
				if colors.get(map_true[py][px]):
					
					Z.grid[y][x] = colors[map_true[py][px]]
				else:
					Z.grid[y][x] = map_true[py][px]
					
				if y == my and x == mx:
					Z.grid[y][x] = angle_sym[player["angle"]]
					
				#if Z.grid[y][x] == colors[player_color]:
					#Z.grid[y][x] = angle_sym[player["angle"]]
					
			else:
				Z.grid[y][x] = "?"
	
	
	if on_enemy:
		area = Z.areas[sub_screen]
		x1, y1, x2, y2 = area
		Z.set_box(x1, y1, x2, y2, Z.fgs[sub_screen], Z.grid)
		text = Z.texts[sub_screen]
		t_anchor = Z.tanchors[sub_screen]
		if text != "":
			if t_anchor != "":
				tx = math.floor((x2 - x1)/2)
				ty = math.floor((y2 - y1)/2)
				tx, ty = Z.get_tAnchor(sub_screen, text)[t_anchor]
				tlen = len(text)
				for i in range(tlen):
					
					Z.grid[ty][tx + i] = text[i] 
	
	#Z.display_true(map_true)
	
	
	Z.display_grid()
	
	#print(f'loc:{player["x"]} {player["y"]}')
	#print('Angle: {}'.format(player["angle"]))
	#print("Commands: \n \'W\':Foward \'S\':Back \'Q\':Rotate Right \n \'A\':Left \'D\':Right \'E\':Rotate Left \n \'X\':Quit \n ")
	#print(map_true[player["y"]][player["x"]])
	dir = input(f"Move")
	
	
	
	#dir processing/ movement
	for letter in dir:
		
			
		#if directions.get(letter):
		if omni_dir[player["angle"]].get(letter):
			#temp_x = player['x'] + directions[letter][1]
			#temp_y = player['y'] + directions[letter][0]
			temp_x = player['x'] + omni_dir[player["angle"]][letter][1]
			temp_y = player['y'] + omni_dir[player["angle"]][letter][0]
			if map_true[temp_y][temp_x] != wall_color: 
				#in_bounds(temp_x,temp_y,len(grid[0]),len(grid)):
					
				#setting previous tile back to what it was
				#map_true[player['y']][player['x']] = player['ground']
				
				#setting the grouf tile to whatever is beneath
				#player['ground'] = map_true[temp_y][temp_x]					
				
				#setiing and updating the player position
				player['x'] = temp_x
				player['y'] = temp_y
				player['tx'] = player['x'] + .5
				player['ty'] = player['y'] + .5
				# map_true[player['y']][player['x']] = player_color
			
		
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
			
			
		
			
		
	
	#os.system('cls')
	

	
	
	
	#Z.display_true(Z.grid)
	#player["playing"] = False


	
	
		

