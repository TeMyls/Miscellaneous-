--[[
  adjacency matrix-uses a 2D array to a represent a graph/tree class 
    that uses thr row indexes as nodes and each individual rows contents as edges containing childerv

    Index 1:_ _ 3 4 _ 
    Index 2:_ _ _ _ 5 
    Index 3:_ _ _ _ _ 
    Index 4:_ _ _ _ _ 
    Index 5:_ _ _ _ _ 

]]
local tree = {}
tree.__index = tree

function tree:new()
   local self = setmetatable({}, tree)
   self.edges = {}
   self.directed = true
   return self
end

function tree:create_2D_array(width, height, filler)
   local array_2d = {}
   for y = 1, height do
      table.insert( array_2d, {})
      for x = 1, width do
         -- in the case the array is an array
         table.insert( array_2d[y], filler )
      end
   end
   return array_2d
end

function tree:create_1D_array(length, filler)
   local array_1d = {}
   for x = 1, length do
      table.insert( array_1d, filler )
   end
   return array_1d
end

function tree:set_size(size)
   self.edges = self:create_2D_array(size, size, -1)
end


function tree:display()
   local s = ""
   for row = 1, #self.edges do
      s = s..("Index %d:"):format(row)
      for col = 1, #self.edges[row] do
         local ele = self.edges[row][col]
         
         if ele == -1 then
            s = s.."_ "
            
         else
            s = s..tostring(ele).." "
         end
      end
      s = s.."\n"
   end
   print(s)
end

function tree:add_node()
   local size = #self.edges
   
   local i = 1
   while i <= size do
      table.insert(self.edges[i], -1)
      i = i + 1
   end
   table.insert(self.edges, self:create_1D_array(size + 1, -1))
end


function tree:remove_node(node_idx)
   local size = #self.edges
   if node_idx > size then
      return
   end
   
   if node_idx < 1 then
      return
   end
   
   local i = 1
   local j = 1
   while i <= size do
      
      while j <= size do
         local ele = self.edges[i][j]
         if ele ~= -1 then
            self.edges[i][j] =  self.edges[i][j] - 1
         end
         j = j + 1
      end
      
      
      table.remove(self.edges[i], node_idx)
      j = 1
      i = i + 1
   end
   table.remove(self.edges, node_idx)
   
end

function tree:add_child(child_idx, parent_idx)
   local size = #self.edges
   if child_idx < 1 or child_idx > size then
      return
   end
   
   if parent_idx < 1 or parent_idx > size then
      return
   end
   
   if parent_idx == child_idx then
      return
   end
   
   -- no undirected graphs
   if self.directed then
      if self.edges[child_idx][parent_idx] == parent_idx then
         return
      end
      
      self.edges[parent_idx][child_idx] = child_idx

   else

      self.edges[parent_idx][child_idx] = child_idx
      self.edges[child_idx][parent_idx] = parent_idx

   end
   
end


function tree:remove_child(child_idx, parent_idx)
   local size = #self.edges
   if child_idx < 1 or child_idx > size then
      return
   end
   
   if parent_idx < 1 or parent_idx > size then
      return
   end
   
   if parent_idx == child_idx then
      return
   end
   
   -- no undirected graphs
   if self.directed then
      
      
      self.edges[parent_idx][child_idx] = -1

   else

      self.edges[parent_idx][child_idx] = -1
      self.edges[child_idx][parent_idx] = -1

   end
   
end



function tree:traverse(node_idx, is_bfs)
   if #self.edges == 0 then
      return 
   end
   
   is_bfs = is_bfs or false
   local visited = {[node_idx] = true}
   local deque = {node_idx}
   
   
   while #deque > 0 do
      local parent = -1
      if is_bfs then
         parent = table.remove(deque, 1)
      else
         parent = table.remove(deque)
      end
      
      if #self.edges[parent] then
         for i = 1, #self.edges[parent] do
            local child = self.edges[parent][i]
            if child ~= -1 then
               if not visited[child] then
                  table.insert( deque, child )
                  visited[child] = true
               end
            end
            
         end
      end
      
   end
   local visited_keys = {}
   for k, v in pairs(visited) do
      if v then
         table.insert(visited_keys, k)
      end
   end
   return visited_keys
end

function tree:input_indexes(idx_dict)
   self:set_size(#idx_dict)
   for k, v in pairs(idx_dict) do
      for i = 1, #v do
         self:add_child(v[i], k)
      end
   end
end

return tree