local tree = {}
tree.__index = tree

function tree:new()
  local self = setmetatable({}, tree)
  
  self.edges = {
      --[[
        A series of indexes and their connections
        A parent widget and it's childerns index in a table/array in lua their would be no 0 index
        # EXAMPLE
        [0] = {1, 2},
        [1] = {4},
        [2] = {3, 6},
        [3] = {},
        [4] = {5},
        [5] = {},
        [6] = {}

    ]]
  }

  return self
end     

function tree:traverse(node_idx, is_bfs)
  is_bfs = is_bfs or false
  local visited = { node_idx }
  local deque = { node_idx }

  while #deque > 0 do
    
    local item = -1
    if is_bfs then
      item = table.remove(deque, 1)
    else
      item = table.remove(deque, #deque)
    end
      
    local has_item = false
    for key, value in pairs(self.edges) do
          
      if key == item then
        has_item = true
        break
      end
          
    end
      
      
    if has_item then
      
      
      for i = 1, #self.edges[item] do
        
        local in_visited = false
        local child = self.edges[item][i]
        for j = 1, #visited do
          if visited[j] == child then
            in_visited = true
            break
          end
        end
        
        if not in_visited then
          table.insert(visited, child)
          table.insert(deque, child)
        end
        
      end 


    end

  end
  return visited
end

function tree:display()
  for key, value in pairs(self.edges) do
    print("\nParent Index:", key, "\n")
    for i = 1, #self.edges[key] do
      print("\tChild Index:", self.edges[key][i])
    end
  end
end


function tree:get_parent(node_idx, is_bfs)
  is_bfs = is_bfs or false
  local visited = { node_idx }
  local deque = { node_idx }
  
  while #deque > 0 do
    local item = -1
    if is_bfs then
      item = table.remove(deque, 1)
    else
      item = table.remove(deque, #deque)
    end
      
    local has_item = false
    for key, value in pairs(self.edges) do
          
      if key == item then
        has_item = true
        break
      end
          
    end
      
      
    if has_item then
      
      
      for i = 1, #self.edges[item] do
        
        local in_visited = false
        local child = self.edges[item][i]
        for j = 1, #visited do
          if visited[j] == child then
            in_visited = true
            break
          end
        end
        
        if not in_visited then
          table.insert(visited, child)
          table.insert(deque, child)
          if child == node_idx then
            return item
          end
        end
        
      end 


    end

  end
  return -1
end

function tree:manage_childern(child_idx, parent_idx)
  local in_parent = false
  local is_parent = false 
  if self.edges[parent_idx] then
    for i = 1, #self.edges[parent_idx] do
      local child = self.edges[parent_idx][i]
      if child == child_idx then
        in_parent = true
      end
      if child == parent_idx then
        is_parent = true
      end
    end
  end
  return in_parent, is_parent 
end

function tree:get_child_idx(child_idx, parent_idx)
  if self.edges[parent_idx] then
    for i = 1, #self.edges[parent_idx] do
      local child = self.edges[parent_idx][i]
      if child == child_idx then
        return i
      end
      
    end
  end
  return -1
end

function tree:add_child(child_idx, parent_idx)
  if #self.edges > 0 then
    local in_parent, is_parent = self:manage_childern(child_idx, parent_idx)
    
    if not in_parent and not is_parent then
      if parent_idx ~= -1 then
        table.insert(self.edges[parent_idx], child_idx)
      end 
    end

  end
end

function tree:remove_child(child_idx, parent_idx)
  if #self.edges > 0 then
    local in_parent, is_parent = self:manage_childern(child_idx, parent_idx)
    if in_parent and not is_parent then
      child_idx = self:get_child_idx(child_idx, parent_idx)
      if child_idx ~= -1 then
        table.remove(self.edges[parent_idx], child_idx)
      end
    end 
  end
end

function tree:add_index(new_idx, parent_idx)
  self.edges[new_idx] = {}
  self:add_child(new_idx, parent_idx)
end

function tree:delete_array_index(idx)
  idx = idx or -1
  if idx > 0 then
    local new_edges = {}
    local has_idx = false
    for key, value in pairs(self.edges) do

      for i = 1, #self.edges[key] do
        local child = self.edges[key][i]
        if child == idx then
          has_idx = true
          break
        end
      end

      if has_idx then
        break
      end
    end

    if has_idx then

      table.remove(self.edges, idx)
      for key, value in pairs(self.edges) do
        for i = 1, #self.edges[key] do
          local child = self.edges[key][i]
          if child > idx then
            self.edges[key][i] = self.edges[key][i] - 1
            if key > idx then

              local new_key = key - 1
              if not new_edges[new_key] then
                new_edges[new_key] = {}
                table.insert(new_edges[new_key], self.edges[key][i])
              else
                table.insert(new_edges[new_key], self.edges[key][i])
              end

            else

              if not new_edges[key] then
                new_edges[key] = {}
                table.insert(new_edges[key], self.edges[key][i])
              else
                table.insert(new_edges[key], self.edges[key][i])
              end
              --new_edges[key] = self.edges[key][i]
            end
          end
        end

      end
    end
    
    self.edges = new_edges
  end
  
end




  

return tree