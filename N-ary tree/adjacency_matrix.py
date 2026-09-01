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

class TreeIndexGrid:
	def __init__(self):
		self.edges = []
		self.directed = True
		
	def input_indexes(self, idx_dict):
		self.set_size(len(idx_dict))
		for i in idx_dict:
			for j in idx_dict[i]:
				t.add_child(i, j)
		
		
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
	
	
	
t = TreeIndexGrid()

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
	
		 0: [1],
		 1: [2],
		 2: [3],
		 3: [0],
		 
		 }

t.input_indexes(a)

t.display_tree()
print(t.traverse(0))


dlt = 1
print(f"\n	Deleting {dlt}\n")

t.delete_node(dlt)
t.display_tree()
print("adding")
t.add_node()
print("adding")
t.add_node()
t.display_tree()



