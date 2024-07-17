def dict_tree_bfs(dct,node):
	visited = [node]
	
	kyu = [node]

	
	
	#print(set(list(dct.keys()) + pos_vals))
	#cur_val = dct[d_root]
	print(dct)
	
	while kyu:
		print(kyu)
		item = kyu.pop(0)
		
		if dct.get(item):
			for i in dct[item]:
				if i not in visited:
					kyu.append(i)
					visited.append(i)
		
	print(visited)
	
def dict_tree_dfs(dct,node):
	visited = []
	
	stack = [node]
	tcd = dct.copy()
	
	
	#print(set(list(dct.keys()) + pos_vals))
	#cur_val = dct[d_root]
	print(dct)
	ind = 0
	anti = 0
	prev = node
	
	
	
	
	#print(node)
	#print(stack)
	while stack:
		print(stack)
		item = stack.pop()
		visited.append(item)
		if dct.get(item):
			for i in range(len(dct[item]) - 1,-1,-1):
				
				if dct[item][i] not in visited:
					stack.append(dct[item][i])
					
				
				
		
	
			
			
			
		
			
						
		
	
	print(visited)

tree_dict_bfs = {'a':['b','c'],'b':['d'],'c':['e','f'],'d':[],'e':[],'f':[]}

tree_dict_dfs = {'a':['b','d'],'b':['c'],'c':[],'d':['e','f'],'e':[],'f':['g'],'g':[]}



dict_tree_dfs(tree_dict_dfs,'a')
