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



a = {
		 0: [5, 1, 6],
		 1: [0, 4],
		 2: [5, 3, 4],
		 3: [2, 4],
		 4: [2, 3, 1], 
		 5: [0, 2, 6],
		 6: [0, 5]
		 }

b = {
		 0: [1, 2],
		 1: [0, 2],
		 2: [0, 1, 3], 
		 3: [2, 4],
		 4: [3, 5, 6],
		 5: [4, 6],
		 6: [4, 5]
		 
}

c = {
	0: [5, 4, 1], 
	1: [0, 2, 3], 
	2: [1, 5], 
	3: [1, 4], 
	4: [0, 3], 
	5: [0, 2]
}

d = {
	0: [1, 2, 3], 
	1: [0, 2], 
	2: [0, 1],
	3: [0, 4],
	4: [3, 5, 6],
	5: [4, 6],
	6: [4, 5]
}
	

tree = nodeGraph()
tree.edges = d
tree.display()
print(tree.traverse(0, False))
