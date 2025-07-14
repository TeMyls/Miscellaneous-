def bfs(dct,node):
	visited = [node]
	queue = [node]
	print(dct)
	
	while queue:
		print(queue)
		item = queue.pop(0)
		if dct.get(item):
			for i in dct[item]:
				if i not in visited:
					queue.append(i)
					visited.append(i)
		
	print(visited)
	
def dfs(dct,node):
	visited = [node]
	stack = [node]
	print(dct)
	
	while stack:
		print(stack)
		item = stack.pop()
		if dct.get(item):
			for i in range(len(dct[item]) - 1,-1,-1):
				if dct[item][i] not in visited:
					stack.append(dct[item][i])
					visited.append(dct[item][i])
					

	print(visited)

tree_bfs = {
		'a':['b','c'],
		'b':['d'],
		'c':['e','f'],
		'd':[],
		'e':[],
		'f':[]
		}
tree_dfs = {
		'a':['b','d'],
		'b':['c'],
		'c':[],
		'd':['e','f'],
		'e':[],
		'f':['g'],
		'g':[]
		}

print('tree bfs')
bfs(tree_bfs,'a')
print('tree dfs')
dfs(tree_dfs,'a')
