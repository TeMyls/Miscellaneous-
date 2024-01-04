rectangle = Object.extend(Object)
require "sat"



local function random_angle()
  local angle = love.math.random(0.33,math.pi/2)
  return angle
end

local function rotated_points(x, y, width, height, rot_angle)
	local cosa, sina = math.cos(rot_angle), math.sin(rot_angle)

	local dx1, dy1 = width*cosa,  width*sina
	local dx2, dy2 = -height*sina, height*cosa

	local px1, py1 = x,         y
	local px2, py2 = x+dx1,     y+dy1
	local px3, py3 = x+dx1+dx2, y+dy1+dy2
	local px4, py4 = x+dx2,     y+dy2
	return px1 ,py1 ,px2 ,py2 ,px3 ,py3 ,px4 ,py4
	--love.graphics.polygon(mode, px1,py1, px2,py2, px3,py3, px4,py4)
  
end

function rectangle:new(x, y, w, h,  speed)
    self.radius = radius
    self.x = x
    self.y = y
   
    self.w = w
    self.h = h
    self.speed = speed
    self.rotation_angle = random_angle()
    self.movement_angle = random_angle()
    self.x_1, self.y_1, self.x_2, self.y_2, self.x_3, self.y_3,self.x_4,self.y_4 = rotated_points(self.x, self.y, self.w, self.h, self.rotation_angle)
    --Given 2 Points of a Rectangle, find the Center? 
    --Top left and bottom right
    --center of rectangle
    self.cx = (self.x_1 + self.x_3)/2
    self.cy = (self.y_1 + self.y_3)/2
    self.direction = 1
    self.wrapping = false
    self.mode = 'line'
    self.bool = false
    self.shader = love.graphics.newShader[[
        vec4 effect( vec4 color, Image texture, vec2 texture_coords, vec2 screen_coords ){
          vec4 pixel = Texel(texture, texture_coords );//This is the current pixel color
          return pixel * color;
    }
  ]]
  --SAT visualization variables
  self.norm_points = {}
  self.orth_points = {}
end
--seperating axis theorem implementation
------------------------------------------------------------------------------------------------------------------------
function rectangle:normalize(vector)
  --:return: The vector scaled to a length of 1
  local norm = math.sqrt(vector[1]^2 + vector[2]^2)
 
  return {vector[1]/norm , vector[2]/norm}
end

function rectangle:dot(vector1,vector2)
  --:return: The dot (or scalar) product of the two vectors
  return vector1[1] * vector2[1] + vector1[2] * vector2[2]
end

function rectangle:edge_direction(point0, point1)
  --:return: A vector going from point0 to point1
  return {point1[1] - point0[1], point1[2] - point0[2]}
end

function rectangle:orthogonal(vector)
  --:return: A new vector which is orthogonal to the given vector
  return {vector[2], -vector[1]}
end

function rectangle:vertices_to_edges(vertices)
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



function rectangle:project(vertices,axis)
  --:return: A vector showing how much of the vertices lies along the axis
  local dots = {}
 
  for i, vertex in ipairs(vertices) do
    table.insert(dots,self:dot(vertex,axis))
  end
  
  return {math.min(unpack(dots)),math.max(unpack(dots))}
end

function rectangle:overlap(projection1, projection2)
  --:return: Boolean indicating if the two projections overlap
  
  local bool_1 = math.min(unpack(projection1)) <= math.max(unpack(projection2))
  
  local bool_2 = math.min(unpack(projection2)) <= math.max(unpack(projection1))
  
  return bool_1 and bool_2
end

function rectangle:table_concat(t1,t2)
   for i=1,#t2 do
      t1[#t1+1] = t2[i]
   end
   return t1
end


function rectangle:separating_axis_theorem(vertices_a,vertices_b)
  local edges = table_concat(vertices_to_edges(vertices_a), vertices_to_edges(vertices_b))
  
  
  local axes = {}
  for i, edge in ipairs(edges) do
   
    table.insert(axes,self:normalize(self:orthogonal(edge)))
  end
  for i, axis in ipairs(axes) do
    projection_a = self:project(vertices_a,axis)
    projection_b = self:project(vertices_b,axis)
    
    overlapping = self:overlap(projection_a, projection_b)
    if not overlapping then
      return false
    end
  end
  return true
  
end
--end of implementation
------------------------------------------------------------------------------------------------------------------------
function rectangle:colliding_with_other_rectangles()
  if #shapes > 1 then
    for j, shape in ipairs(shapes) do
      if self ~= shape then
        local x, y, r = self:circle_params()
        if shapes[j]:circle_collision(x, y, r) then
          if separating_axis_theorem(self:get_vertices(0),shapes[j]:get_vertices(0)) then
            self.mode = 'fill'
            shapes[j].mode = 'fill'
            self:bounce()
            --shapes[j]:bounce()
          else
            self.mode = 'line'
            shapes[j].mode = 'line'
          end
        end
      end
    end
  end
end


function rectangle:circle_params()
  return self.cx,self.cy,math.max(self.w,self.h) 
  
  
end

function rectangle:circle_collision(circle_x,circle_y,circle_radius)
  
  local self_radius = math.max(self.w,self.h) 
  return (self.cx - circle_x)^2 + (self.cy - circle_y)^2 <= (self_radius + circle_radius) ^ 2
  
  
end

function rectangle:bounce()
  if self.mode == 'fill' then
    self.direction = -self.direction
    
    self.speed  = -self.speed  
  end
end



function rectangle:get_vertices(buffer)
  return {{self.x_1 - buffer,self.y_1 - buffer},{self.x_2 - buffer,self.y_2 + buffer},{self.x_3 + buffer,self.y_3 + buffer},{self.x_4 + buffer,self.y_4 - buffer}}
    
end


function rectangle:wall_bounce(x_1, x_2, x_3, x_4,y_1, y_2, y_3, y_4)
    
  
    if x_1 <= 1 then
      self.movement_angle = -self.movement_angle
      self.speed  = -self.speed  
      self.direction = -self.direction
    end
    if x_2 <= 1 then
      self.movement_angle = -self.movement_angle
      self.speed  = -self.speed  
      self.direction = -self.direction
    end
    if x_3 <= 1  then
      self.movement_angle = -self.movement_angle
      self.speed  = -self.speed  
      self.direction = -self.direction
    end
    if x_4 <= 1 then
      self.movement_angle = -self.movement_angle
      self.speed  = -self.speed  
      self.direction = -self.direction
    end
    
    if x_1 > screen_width - 1 then
      self.movement_angle = -self.movement_angle
      self.speed  = -self.speed 
      self.direction = -self.direction
    end
    if x_2 > screen_width - 1 then
      self.movement_angle = -self.movement_angle
      self.speed  = -self.speed 
      self.direction = -self.direction
    end
    if x_3 > screen_width - 1 then
      self.movement_angle = -self.movement_angle
      self.speed  = -self.speed 
      self.direction = -self.direction
    end
    if x_4 > screen_width - 1 then
      self.movement_angle = -self.movement_angle
      self.speed  = -self.speed 
      self.direction = -self.direction
    end
    
    if y_1 <= 1 then
      self.movement_angle = -self.movement_angle
      self.speed  = self.speed  
      self.direction = -self.direction
    end
    if y_2 <= 1 then
      self.movement_angle = -self.movement_angle
      self.speed  = self.speed  
      self.direction = -self.direction
    end
    if y_3 <= 1 then
      self.movement_angle = -self.movement_angle
      self.speed  = self.speed  
      self.direction = -self.direction
    end
    if y_4 <= 1 then
      self.movement_angle = -self.movement_angle
      self.speed  = self.speed  
      self.direction = -self.direction
    end
    
    if y_1 > screen_height - 1 then
      self.movement_angle = -self.movement_angle
      self.speed  = self.speed  
      self.direction = -self.direction
    end
    if y_2 > screen_height - 1 then
      self.movement_angle = -self.movement_angle
      self.speed  = self.speed  
      self.direction = -self.direction
    end
    if y_3 > screen_height - 1 then
      self.movement_angle = -self.movement_angle
      self.speed  = self.speed  
      self.direction = -self.direction
    end
    if y_4 > screen_height - 1 then
      self.movement_angle = -self.movement_angle
      self.speed  = self.speed  
      self.direction = -self.direction
    end
  

    
  
  

end



function rectangle:rotated_points(x, y, width, height, rot_angle)
  --relative to box top right,x,y
	local cosa, sina = math.cos(rot_angle), math.sin(rot_angle)

	local dx1, dy1 = width*cosa,  width*sina
	local dx2, dy2 = -height*sina, height*cosa

	local px1, py1 = x,         y
	local px2, py2 = x+dx1,     y+dy1
	local px3, py3 = x+dx1+dx2, y+dy1+dy2
	local px4, py4 = x+dx2,     y+dy2
  --self.cx,self.cy = x+dx1/2+dx2/2, y+dy1/2+dy2/2
	return px1 ,py1 ,px2 ,py2 ,px3 ,py3 ,px4 ,py4
	--love.graphics.polygon(mode, px1,py1, px2,py2, px3,py3, px4,py4)
  
end

function rectangle:update_points(cx, cy, width, height, rot_angle)
  --relative to center of box,cx,cy
  local cosa, sina = math.cos(rot_angle), math.sin(rot_angle)

	local dx1, dy1 = width*cosa,  width*sina
	local dx2, dy2 = -height*sina, height*cosa

	local px1, py1 = cx - (dx1/2)  - (dx2/2), cy - (dy1/2)  - (dy2/2)
	local px2, py2 = px1+dx1,     py1+dy1
	local px3, py3 = px1+dx1+dx2, py1+dy1+dy2
	local px4, py4 = px1+dx2,     py1+dy2
  
	return px1 ,py1 ,px2 ,py2 ,px3 ,py3 ,px4 ,py4
end

function rectangle:draw_mode(wrapping,mode)
  if wrapping then
   
    for y = -1, 1 do
      for x = -1, 1 do
        love.graphics.origin()
        love.graphics.translate(x * screen_width, y * screen_height)
        love.graphics.polygon(mode, self.x_1, self.y_1, self.x_2, self.y_2, self.x_3, self.y_3,self.x_4,self.y_4)
      end
      
    end
     
  else
    love.graphics.polygon(mode, self.x_1, self.y_1, self.x_2, self.y_2, self.x_3, self.y_3,self.x_4,self.y_4)
  end
  
end

function rectangle:move(dt,screen_wrap,bounce_wall)

  self.movement_angle = self.movement_angle % (2*math.pi) 
  self.rotation_angle = self.rotation_angle + self.direction * .5*math.pi * dt
    
  local cos,sin = math.cos(self.movement_angle), math.sin(self.movement_angle)
  --self.cx = (self.x_1 + self.x_3)/2
  --self.cy = (self.y_1 + self.y_3)/2

  if screen_wrap == true and bounce_wall == false then
    --self.x = (self.x + cos * self.speed * dt) % screen_width
    --self.y = (self.y + sin * self.speed  * dt) % screen_height
    self.cx = (self.cx + cos * self.speed * dt) % screen_width
    self.cy = (self.cy + sin * self.speed  * dt) % screen_height
    --rotates around top right of the box
    --self.x_1, self.y_1, self.x_2, self.y_2, self.x_3, self.y_3,self.x_4,self.y_4 = self:rotated_points(self.x, self.y, self.w, self.h, self.rotation_angle)
    --rotates around center of the box
    self.x_1, self.y_1, self.x_2, self.y_2, self.x_3, self.y_3,self.x_4,self.y_4 = self:update_points(self.cx, self.cy, self.w, self.h, self.rotation_angle)
    self.wrapping = true
  end
  if screen_wrap == false and bounce_wall == true then
     --rotates around top right of the box
    --self.x = (self.x + cos * self.speed * dt) 
    --self.y = (self.y + sin * self.speed  * dt) 
    
    
    self.cx = (self.cx + cos * self.speed * dt) 
    self.cy = (self.cy + sin * self.speed  * dt) 
    
    --rotates around top right of the box
    self.x_1, self.y_1, self.x_2, self.y_2, self.x_3, self.y_3,self.x_4,self.y_4 = self:rotated_points(self.x, self.y, self.w, self.h, self.rotation_angle)
    --rotates around center of the box
    self.x_1, self.y_1, self.x_2, self.y_2, self.x_3, self.y_3,self.x_4,self.y_4 = self:update_points(self.cx, self.cy, self.w, self.h, self.rotation_angle)
    self.wrapping = false
    self:wall_bounce(self.x_1, self.x_2, self.x_3, self.x_4,self.y_1, self.y_2, self.y_3, self.y_4)
  end

  
  
  
    
end

function rectangle:update(dt)
    
    self:colliding_with_other_rectangles()
    self:move(dt,false, true)
    
    
    
    
 
end



function rectangle:draw()
  
  self:draw_mode(self.wrapping,self.mode)
 --Given 2 Points of a Rectangle, find the Center? 
 --Top left snd bottom right
 --love.graphics.points(self.cx,self.cy)
 --math.max(self.w,self.h)
 --love.graphics.circle('line',self.cx,self.cy,10)
  
  
  --love.graphics.print(tostring(dbool),10,10)
  --love.graphics.print(self.movement_angle,10,20)
  
  
  --self:draw_rotated("line",self.x,self.y,self.w,self.h,self.angle)
end