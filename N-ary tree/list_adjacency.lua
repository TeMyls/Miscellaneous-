-- A directed graph stored as two tables.
-- The keys are node indexes, the values are arrays of node indexes.
--
-- edges:   node -> its children   (parent points to children)
-- parents: node -> its parents    (child points to parents, kept as a look up)

local AdjacencyList = {}
AdjacencyList.__index = AdjacencyList

-- helpers ---------------------------------------------------------------

local function index_of(list, value)
	for i = 1, #list do
		if list[i] == value then
			return i
		end
	end
	return nil
end

local function remove_value(list, value)
	local i = index_of(list, value)
	if i then
		table.remove(list, i)
	end
end

local function sorted_keys(t)
	local keys = {}
	for k in pairs(t) do
		keys[#keys + 1] = k
	end
	table.sort(keys)
	return keys
end

local function list_to_string(list)
	local parts = {}
	for i, v in ipairs(list) do
		parts[i] = tostring(v)
	end
	return "[" .. table.concat(parts, ", ") .. "]"
end

-- class -----------------------------------------------------------------

function AdjacencyList.new()
	local self = setmetatable({}, AdjacencyList)
	self.edges = {}
	self.parents = {}
	return self
end

function AdjacencyList:display()
	for _, key in ipairs(sorted_keys(self.edges)) do
		print(
			"Node", key,
			"Parents:", list_to_string(self.parents[key]),
			"Children:", list_to_string(self.edges[key])
		)
	end
end

function AdjacencyList:insert_adjacency_list(alist)
	-- alist maps a parent to an array of its children.
	-- Keys are sorted so the result does not depend on pairs() ordering.
	for _, key in ipairs(sorted_keys(alist)) do
		self:add_index(key) -- registers nodes with no children and no parents
		for _, value in ipairs(alist[key]) do
			self:add_child(value, key)
		end
	end
end

function AdjacencyList:traverse(node, is_bfs)
	if is_bfs == nil then
		is_bfs = true
	end

	if not self.edges[node] then
		return {}
	end

	local visited = {}
	local seen = {}

	if is_bfs then
		seen[node] = true
		local queue, head = { node }, 1
		while head <= #queue do
			local item = queue[head]
			head = head + 1
			visited[#visited + 1] = item
			for _, child in ipairs(self.edges[item]) do
				if not seen[child] then
					seen[child] = true
					queue[#queue + 1] = child
				end
			end
		end
	else
		local stack = { node }
		while #stack > 0 do
			local item = table.remove(stack)
			if not seen[item] then
				seen[item] = true
				visited[#visited + 1] = item
				-- walk backwards so the first child is popped (visited) first
				local kids = self.edges[item]
				for i = #kids, 1, -1 do
					if not seen[kids[i]] then
						stack[#stack + 1] = kids[i]
					end
				end
			end
		end
	end

	return visited
end

function AdjacencyList:get_parent(idx)
	local copy = {}
	for i, v in ipairs(self.parents[idx] or {}) do
		copy[i] = v
	end
	return copy
end

function AdjacencyList:get_children(idx)
	local copy = {}
	for i, v in ipairs(self.edges[idx] or {}) do
		copy[i] = v
	end
	return copy
end

function AdjacencyList:add_index(idx, parent_idx)
	if not self.edges[idx] then
		self.edges[idx] = {}
		self.parents[idx] = {}
	end

	if parent_idx ~= nil and parent_idx > -1 then
		self:add_child(idx, parent_idx)
	end
end

function AdjacencyList:add_child(child_idx, parent_idx)
	if child_idx == parent_idx then
		return
	end

	self:add_index(child_idx)
	self:add_index(parent_idx)

	if index_of(self.edges[parent_idx], child_idx) then
		return
	end

	table.insert(self.edges[parent_idx], child_idx)
	table.insert(self.parents[child_idx], parent_idx)
end

function AdjacencyList:remove_child(child_idx, parent_idx)
	if not self.edges[parent_idx] then
		return
	end

	if not index_of(self.edges[parent_idx], child_idx) then
		return
	end

	remove_value(self.edges[parent_idx], child_idx)
	remove_value(self.parents[child_idx], parent_idx)
end

function AdjacencyList:delete_index(idx)
	if not self.edges[idx] then
		return
	end

	-- remove every edge that touches idx so nothing points at a deleted node
	for _, child in ipairs(self.edges[idx]) do
		remove_value(self.parents[child], idx)
	end

	for _, parent in ipairs(self.parents[idx]) do
		remove_value(self.edges[parent], idx)
	end

	self.edges[idx] = nil
	self.parents[idx] = nil
end



return AdjacencyList