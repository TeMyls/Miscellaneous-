function normalize(vector)
  --:return: The vector scaled to a length of 1
  local norm = math.sqrt(vector[1]^2 + vector[2]^2)
  return {vector[1]/norm , vector[2]/norm}
end

function dot(vector1,vector2)
  --:return: The dot (or scalar) product of the two vectors
  return vector1[1] * vector2[1] + vector1[2] * vector2[2]
end

function edge_direction(point0, point1)
  --:return: A vector going from point0 to point1
  return {point1[1] - point0[1], point1[2] - point0[2]}
end

function orthogonal(vector)
  --:return: A new vector which is orthogonal to the given vector
  return {vector[2], -vector[1]}
end

function vertices_to_edges(vertices)
  --:return: A table of the edges of the vertices as vectors
  --print(tostring(#vertices))
  
  local edges_table = {}
  for i, vertex in ipairs(vertices) do
    local overflow = (i + 1)
    if overflow > #vertices then
      overflow = 1
      
    end
  
    table.insert(edges_table, edge_direction(vertices[i],vertices[overflow]))
    
    
  end
  
  
  return edges_table
end



function project(vertices,axis)
  --:return: A vector showing how much of the vertices lies along the axis
  local dots = {}
 
  for i, vertex in ipairs(vertices) do
    table.insert(dots,dot(vertex,axis))
  end
  
  return {math.min(unpack(dots)),math.max(unpack(dots))}
end

function overlap(projection1, projection2)
  --:return: Boolean indicating if the two projections overlap
  
  local bool_1 = math.min(unpack(projection1)) <= math.max(unpack(projection2))
  
  local bool_2 = math.min(unpack(projection2)) <= math.max(unpack(projection1))
  
  return bool_1 and bool_2
end

function table_concat(t1,t2)
   for i=1,#t2 do
      t1[#t1+1] = t2[i]
   end
   return t1
end


function separating_axis_theorem(vertices_a,vertices_b)
  local edges = table_concat(vertices_to_edges(vertices_a), vertices_to_edges(vertices_b))
  
  
  local axes = {}
  for i, edge in ipairs(edges) do
   
    table.insert(axes,normalize(orthogonal(edge)))
  end
  for i, axis in ipairs(axes) do
    projection_a = project(vertices_a,axis)
    projection_b = project(vertices_b,axis)
    
    overlapping = overlap(projection_a, projection_b)
    if not overlapping then
      return false
    end
  end
  return true
  
end


--[[

a_vertices = {{0, 0}, {70, 0}, {0, 70}}
b_vertices = {{70, 70}, {150, 70}, {70, 150}}
c_vertices = {{30, 30}, {150, 70}, {70, 150}} 
print(separating_axis_theorem(a_vertices, b_vertices))
print(tostring(separating_axis_theorem(a_vertices, c_vertices)))
print(tostring(separating_axis_theorem(b_vertices, c_vertices)))

-]]--