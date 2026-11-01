from collections import deque


class AdjacencyList:
    def __init__(self):
        # A directed graph stored as two dictionaries.
        # The keys are node indexes, the values are lists of node indexes.
        #
        # childern:   node -> its children   (parent points to children)
        # parents: node -> its parents    (child points to parents, kept as a look up)
        #
        # Example
        """
        Parent: 0 Children: [3, 1, 2]
        Parent: 1 Children: [4]
        Parent: 2 Children: [5]
        Parent: 3 Children: [7]
        Parent: 4 Children: []
        Parent: 5 Children: [6]
        Parent: 6 Children: []
        Parent: 7 Children: []
        """
        self.childern = {}
        self.parents = {}

    def display(self):
        for key in sorted(self.childern):
            print("Node", key, "Parents:", self.parents[key], "Children:", self.childern[key])

    def insert_adjacency_list(self, alist):
        # alist maps a parent to a list of its children
        for key in alist:
            self.add_index(key)  # registers nodes that have no children and no parents
            for value in alist[key]:
                self.add_child(value, key)

    def traverse(self, node, is_bfs=True):
        if node not in self.childern:
            return []

        visited = []
        seen = set()

        if is_bfs:
            seen.add(node)
            queue = deque([node])
            while queue:
                item = queue.popleft()
                visited.append(item)
                for child in self.childern[item]:
                    if child not in seen:
                        seen.add(child)
                        queue.append(child)
        else:
            stack = [node]
            while stack:
                item = stack.pop()
                if item in seen:
                    continue
                seen.add(item)
                visited.append(item)
                # reversed so the first child is popped (visited) first
                for child in reversed(self.childern[item]):
                    if child not in seen:
                        stack.append(child)

        return visited

    def get_parent(self, idx):
        return list(self.parents.get(idx, []))

    def get_children(self, idx):
        return list(self.childern.get(idx, []))

    def add_index(self, idx, parent_idx=-1):
        if idx not in self.childern:
            self.childern[idx] = []
            self.parents[idx] = []

        if parent_idx > -1:
            self.add_child(idx, parent_idx)

    def add_child(self, child_idx, parent_idx):
        if child_idx == parent_idx:
            return

        self.add_index(child_idx)
        self.add_index(parent_idx)

        if child_idx in self.childern[parent_idx]:
            return

        self.childern[parent_idx].append(child_idx)
        self.parents[child_idx].append(parent_idx)

    def remove_child(self, child_idx, parent_idx):
        if parent_idx not in self.childern:
            return

        if child_idx not in self.childern[parent_idx]:
            return

        self.childern[parent_idx].remove(child_idx)
        self.parents[child_idx].remove(parent_idx)

    def delete_index(self, idx):
        if idx not in self.childern:
            return

        # remove every edge that touches idx so nothing points at a deleted node
        for child in self.childern[idx]:
            self.parents[child].remove(idx)

        for parent in self.parents[idx]:
            self.childern[parent].remove(idx)

        del self.childern[idx]
        del self.parents[idx]


if __name__ == "__main__":
    d = {
        0: [1, 3],
        1: [2],
        2: [],
        3: [4],
        4: [5, 6],
        5: [],
        6: [],
    }

    tree = AdjacencyList()
    tree.insert_adjacency_list(d)
    tree.display()
    print("BFS", tree.traverse(0, True))
    print("DFS", tree.traverse(0, False))

'''
class AdjacencyList:
	def __init__(self):
		
		# An Dictionary/Adjacency List of childern
		# The keys are the indexes of the container
		# The values are a list of vertex connections
		# Edges/Parents is a directed graph
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
		
		self.edges = {}
		# Childern point to their parents, parents point to their childern
		# self.parents is the same as self.childern in other iterations, but childern is kept as a look up
		self.parents = {}
		self.childern = {}

    
        
	def display(self):
		#print(self.parents)
		#print(self.childern)
		for key in self.parents:
			print("key", key, "parents", self.parents[key], "childern", self.childern[key])
			
	def insert_adjacency_list(self, alist):
		for key in alist:
			if not self.parents.get(key):
				for value in alist[key]:
					self.add_child(value, key)
			
		
	def traverse(self, node: int, is_bfs: bool = True):
		visited = [node]
		deque = [node]
		tree = self.parents
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
	

	
	def get_parent(self, idx):
		if not self.parents.get(idx):
			return -1
		return self.parents[idx]

	
	
	def add_index(self, child_idx, parent_idx = -1):
		
		if not self.parents.get(child_idx):
			self.parents[child_idx] = []
			self.childern[child_idx] = []
		
			
		if parent_idx > -1:
			self.add_child(child_idx, parent_idx)
	
	def add_child(self, child_idx, parent_idx):
		
		if not self.parents.get(child_idx):
			self.parents[child_idx] = []
		if not self.childern.get(parent_idx):
			self.childern[parent_idx] = []
			
		#if child_idx not in self.parents[parent_idx]:
		if self.parents.get(parent_idx):
			self.parents[parent_idx].append(child_idx)
		else:
			self.parents.update({parent_idx: [child_idx]})
				
		#if parent_idx not in self.childern[child_idx]:
		if self.childern.get(child_idx):
			self.childern[child_idx].append(parent_idx)
		else:
			self.childern.update({child_idx: [parent_idx]})
			
	def remove_child(self, child_idx, parent_idx):
		
		if parent_idx == child_idx:
			return
        
		if not self.childern.get(child_idx):
			return
		
		if not self.parents.get(parent_idx):
			return
		
		if child_idx not in self.parents[parent_idx]:
			return

		if self.parents[parent_idx]:
			idx = self.parents[parent_idx].index(child_idx)
			self.parents[parent_idx].pop(idx)
	
		if self.childern[child_idx]:
			idx = self.childern[child_idx].index(parent_idx)
			self.childern[child_idx].pop(idx)
            
            
		
	def delete_index(self, idx):
	
		
		if not self.childern.get(idx):
			return
		if not self.parents.get(idx):
			return
		
		self.parents.pop(idx)
		self.childern.pop(idx)

        
		





d = {
	0: [1, 3], 
	1: [2], 
	2: [],
	3: [4],
	4: [5, 6],
	5: [],
	6: []
}
	

tree = AdjacencyList()
tree.insert_adjacency_list(d)
tree.display()
print(tree.traverse(0, False))
'''

