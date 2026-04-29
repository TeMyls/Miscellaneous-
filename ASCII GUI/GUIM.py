import math
import time
import console
import random
import os

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
			print(deque)
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

		
		
class GUI_Manager:
	def __init__(self):
		# space sets of x1-y1-x2-y2 
		self.space_tree = nodeGraph()
		
		# Sets of x1-y1-x2-y2 
		# the widget area itself
		self.areas = []
		# internal anchor
		# Sets of either C, N, NE, E, SE, S, SW, W, or NE:
			# describes a x1-y1-x2-y2 is positioned inside a 
			# default "" or Center
			# designates the location of the widget in the sub space
		self.ianchors = []
		# Sets of either 
		# N, NE, NW, EN, E, ES, WN, W, WS, S, SE, SW, WNW, NEN, SES, WSW:
			# default ""
			# designates the location of the widget outside a space
		self.eanchors = []
		# Sets of "", X", "Y", or "Both"
			# default: ""
			# makes the widget take up more parts of it's sub space, horizontally, vertically or both
		self.fills = []
		# the color of the widget and the area it inhabits
		self.fgs = []
		
		self.grid = self.empty_map(5, 5, "?")
		
		self.wpcts = []
		self.hpcts = []
		
		

		
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
		
		
	def add_area(self, kwargs):
		
		
		has_x1 = kwargs.get("x1")
		has_y1 = kwargs.get("y1")
		has_x2 = kwargs.get("x2")
		has_y2 = kwargs.get("y2")
		
		has_area = kwargs.get("area")
		
		
		has_fill = kwargs.get("fill")
		
		has_ianchor = kwargs.get("ianchor")
		has_eanchor = kwargs.get("eanchor")
		
		# two strings one representing the space color and the othe the sub soace
		has_bg = kwargs.get("bg")
		has_fg = kwargs.get("fg")
		
		has_hpct = kwargs.get("hpct")
		has_wpct = kwargs.get("wpct")
		
		
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
		
		
	
		parent_idx = self.space_tree.get_parent(idx, False)
		
		
		if parent_idx != -1:
			
			aw, ah, uw, uh = self.get_dimensions(parent_idx, idx)
			wpct = self.wpcts[idx]/100
			hpct = self.hpcts[idx]/100
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
			self.grid = self.empty_map(oh, ow, "@")
			deque = self.space_tree.traverse(0, True)
			#print(self.space_tree.edges)
			#print(deque, self.areas)
			while deque:
			
				item = deque.pop(0) 
				area = self.areas[item]
				x1, y1, x2, y2 = area
				self.set_box(x1, y1, x2, y2, self.fgs[item], self.grid)
				
				
							
			self.display_true(self.grid)
			#print("fin")
		
		
	
	
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
		
	
	
		
	def remove_area(self, idx):
		self.eanchors.pop(idx)
		self.ianchors.pop(idx)
		self.fills.pop(idx)
		self.space_tree.remove_child(idx)



"""
kwargs = {
			# ints
			"x1": 0,
			"y1": 0,
			"x2": len(arr[0]),
			"y2": len(arr),
			
		# Sets of "", X", "Y", or "Both"
			# default: ""
			# makes the widget take up more parts of it's sub space, horizontally, vertically or both
		"fill": "X",
		# internal anchor
		# Sets of either N, NE, E, SE, S, SW, W, or NE:
			# default C or Center
			# designates the location of the widget in the sub space
		"ianchor": "C",
		# external anchor
		# Sets of either 
		# N, NE, NW, EN, E, ES, WN, W, WS, S, SE, SW, WNW, NEN, SES, WSW:
			# default ""
			# designates the location of the widget outside a space
		"eanchor": "N",
		# the color of the area and the space it's allocated'
		"fg":"Q",
		# the parent index
		"pidx":3
			
		}
"""
		
Z = GUI_Manager()
Z.grid = Z.empty_map(20, 44, "X")


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
			"fg":"0",
			"pidx":None
			
}

first = Z.add_area(base)

one = {}
one["area"] = Z.get_box(0, 0, 22, 8)
one["fg"] = "1"
one["ianchor"] = "C"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = first

second = Z.add_area(one)

one = {}
one["area"] = Z.get_box(0, 0, 3, 3)
one["wpct"] = 50
one["fg"] = "2"
one["ianchor"] = "N"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = second

third = Z.add_area(one)

one = {}
one["area"] = Z.get_box(0, 0, 3, 3)
one["fg"] = "3"
one["ianchor"] = "E"
one["eanchor"] = ""
one["fill"] = ""
one["pidx"] = second

fourth = Z.add_area(one)

one = {}
one["area"] = Z.get_box(0, 0, 3, 3)
one["fg"] = "4"
one["hpct"] = 150
one["ianchor"] = ""
one["eanchor"] = "WS"
one["fill"] = ""
one["pidx"] = second

fifth = Z.add_area(one)

one = {}
one["area"] = Z.get_box(0, 0, 3, 3)
one["fg"] = "5"
one["wpct"] = 250
one["ianchor"] = ""
one["eanchor"] = "EN"
one["fill"] = ""
one["pidx"] = fifth

sixth = Z.add_area(one)




Z.render_areas()
#Z.display_data()
