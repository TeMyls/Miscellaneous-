local class = require 'lib/middleclass'
local anim8 = require 'lib/anim8'

local Entity = require "entity"
--screen width and height
local screen_width = love.graphics.getWidth()
local screen_height = love.graphics.getHeight()
local half_screen_width = screen_width/2
local half_screen_height = screen_height/2


local Player = class('Player',Entity)

function HSL(h, s, l, a)
	if s<=0 then return l,l,l,a end
	h, s, l = h*6, s, l
	local c = (1-math.abs(2*l-1))*s
	local x = (1-math.abs(h%2-1))*c
	local m,r,g,b = (l-.5*c), 0,0,0
	if h < 1     then r,g,b = c,x,0
	elseif h < 2 then r,g,b = x,c,0
	elseif h < 3 then r,g,b = 0,c,x
	elseif h < 4 then r,g,b = 0,x,c
	elseif h < 5 then r,g,b = x,0,c
	else              r,g,b = c,0,x
	end return {r+m, g+m, b+m, a}
end

function round(x, increment)
  if increment then return round(x / increment) * increment end
  return x >= 0 and math.floor(x + .5) or math.ceil(x - .5)
end

function degrees_to_radians(degree)
  
  --helper function with self explanory name
  local radians = 0
  local pi = math.pi
  
  return degree * pi / 180
  
end

function create_rays(count,ray_table,fov,x1,y1,length)
  --gives each ray an orginal angle
  local space_per_ray = degrees_to_radians(fov/count)
  local angle_ray = -degrees_to_radians(fov/2)
  for i = 0, count - 1 do
    
    table.insert(
      ray_table,
      {x1,y1,x1 + length*math.cos(angle_ray),y1+ length*math.sin(angle_ray),angle_ray}
    )
    angle_ray = angle_ray + space_per_ray
  end
  return ray_table
end


function Player:initialize(x,y,w,h,hp,img)
  Entity.initialize(self,x, y,w,h,hp,img)
  
  
  if img ~= nil then
    self.img = love.graphics.newImage(img)
    self.quad = love.graphics.newQuad(0,0,self.img:getWidth(),self.img:getHeight(),self.img)
  end
  self.damaged = false
  self.cos = 0
  self.sin = 0
  self.vx = 0
  self.vy = 0
 
 

  self.line = {
    x1 = 0,
    y1 = 0,
    x2 = 0,
    y2 = 0,
    length = 50
  }
  
  self.map = {}
  
  self.tile_size = 0
  self.ray_len = 600
  self.fov = 60
  self.half_fov = self.fov/2
  self.render_delay = 30
  self.angle = 0
  --the current screen width in pixels is 512 
  --or really any that's over the a current any more than the width lags
  self.ray_count = 150
  self.rays = create_rays(self.ray_count,{},self.fov,self.x + self.w/2 ,self.y + self.h/2 ,self.ray_len)
  
  self.dx = 0
  self.dy = 0
  
  
  self.rotation_speed = 300
  self.move_speed = 150
  
  self.tile_img = love.graphics.newImage("assets/bricktile.png")
 
  self.tile_floor_img = love.graphics.newImage("assets/pdbrick.png")
  
end

function Player:map_reference(map)
  --giving the player a reference tot the map, IDK what to say
  self.map = map
end

function Player:draw_ray_line(x1,y1,x2,y2,color_table)
  love.graphics.setColor(color_table)
  love.graphics.line(x1,y1,x2,y2)
  
end

function Player:draw_ray_rectangle(mode,x,y,w,h,color_table)
  if color_table[1] ~= nil and color_table[2] ~= nil and color_table[3] ~= nil then
    love.graphics.setColor(color_table)
  end
  love.graphics.rectangle(mode,x,y,w,h)
  
  
end

function Player:draw_ray_texture(img,quad,x,y)
 
  love.graphics.draw(img, quad, x, y)
  
  
end

function Player:ray_display()
  --displays the rays without collision at a prefined distance
  for i = 1, #self.rays do
    --{x1,y1,x2,y2,length,count * space_per_ray - fov/2}

    love.graphics.line(self.rays[i][1], self.rays[i][2], self.rays[i][3], self.rays[i][4])
  end 
  
end





function Player:update_ray_position(dt)
  --differs from the draw raycasting function as the rays have a set end goal
  
  for i = 1, #self.rays do
      --{x1,y1,x1 + length*math.cos(angle_ray),y1+ length*math.sin(angle_ray)}
      local rad_angle = degrees_to_radians(self.angle)
      local cum_sin = math.sin(rad_angle + self.rays[i][5])
      local cum_cos = math.cos(rad_angle + self.rays[i][5]) 
      self.rays[i][1] = self.x + self.w/2 
      self.rays[i][2] = self.y + self.h/2 
      --plus the previous ray
      self.rays[i][3] = self.x + self.w/2 + self.ray_len*cum_cos 
      self.rays[i][4] =  self.y + self.h/2  + self.ray_len*cum_sin 
  end
  
end

function Player:update_line_angle(dt)
  --shows the actually line the players pointing in
  local rad_angle = degrees_to_radians(self.angle)
  self.sin = math.sin(rad_angle)
  self.cos = math.cos(rad_angle) 
  self.line.x1 = self.x + self.w/2 
  self.line.y1 = self.y + self.h/2 
  self.line.x2 = self.x + self.w/2 + self.line.length*self.cos
  self.line.y2 = self.y + self.h/2 + self.line.length*self.sin
end


function Player:update_angle(dt)
  --keys
  if love.keyboard.isDown('e') then
    
    
    self.angle = self.angle + self.rotation_speed *dt 
    if self.angle > 360 then
      self.angle = 0
    end
   
  elseif love.keyboard.isDown('q') then
   
    self.angle = self.angle - self.rotation_speed *dt 
    if self.angle < 0 then
      self.angle = 360
    end
    
  end
  --mouse
  local mx,my = love.mouse.getPosition()
  if love.mouse.isDown(2) then
    if mx > half_screen_width/2  and 
    mx < half_screen_width then
      --right of screen subsection
      self.angle = self.angle + (((mx - (half_screen_width/2))/(half_screen_width/2)) * self.rotation_speed) *dt 
      if self.angle > 360 then
        self.angle = 0
      end
      
    elseif mx < half_screen_width/2 then
      --left of screen subsection
      self.angle = self.angle - (((half_screen_width/2) - mx)/(half_screen_width/2) * self.rotation_speed) *dt 
      if self.angle < 0 then
        self.angle = 360
      end
      
    end
  end
end



function Player:foward_mouse_movement(dt)
  --mouse movement
  --goes in foward direction facing the players angle on left mouse down

  if love.mouse.isDown(1) then
    
    local mouse_siny = math.sin(degrees_to_radians(self.angle))
    local mouse_cosx = math.cos(degrees_to_radians(self.angle))
    --math.atan2(my - (self.y+self.h/2),mx - (self.x+self.w/2))
    self.vx = self.move_speed * mouse_cosx
    self.vy = self.move_speed * mouse_siny
  else
    self.vx = 0
    self.vy = 0
  end
end

function Player:classic_2d_movement(dt)
  
  --keyboard movement
  --classic up button movement going up left right and down with regards to player angle feels clunky
  --dx and dy are meant to be normalization vectors so when the character moves diagonally they don't go faster from the x and y speed together
  
  if love.keyboard.isDown('up') 
  or love.keyboard.isDown('w') then
    self.dy = -1
    self.vy = self.move_speed * self.dy
  
  elseif love.keyboard.isDown('down') 
  or love.keyboard.isDown('s') then
    self.dy =  1
    self.vy = self.move_speed * self.dy
  else
    self.dy = 0
    self.vy = 0
  end
  
  if love.keyboard.isDown('left') 
  or love.keyboard.isDown('a') then
    self.dx = -1
    self.vx = self.move_speed * self.dx
  elseif love.keyboard.isDown('right') 
  or love.keyboard.isDown('d') then
    self.dx = 1
    self.vx = self.move_speed * self.dx
  else
    self.dx = 0
    self.vx = 0
  end
  
  if self.dx == 1 then
    local length = math.sqrt(self.dx^2+self.dy^2)
    
    
    if self.dy == 1 then
      self.dx = self.dx/length
      self.dy = self.dy/length
      self.vy = self.vy * self.dy
      self.vx = self.vx * self.dx
    elseif self.dy == -1 then
      self.dx = self.dx/length
      self.dy = self.dy/length
      self.vy = self.vy * -self.dy
      self.vx = self.vx * self.dx
    end
    

  end  
  if self.dx == -1 then
    local length = math.sqrt(self.dx^2+self.dy^2)
    if self.dy == 1 then
      self.dx = self.dx/length
    
    
      self.dy = self.dy/length
      self.vy = self.vy * self.dy
      self.vx = self.vx * -self.dx
    elseif self.dy == -1 then
      self.dx = self.dx/length
      self.dy = self.dy/length
      self.vy = self.vy * -self.dy
      self.vx = self.vx * -self.dx
    end
    
    
  end
  
  
  
  
end

function Player:tank_movement(dt)
  if love.keyboard.isDown('right')
  or love.keyboard.isDown('d') then
    
    
    self.angle = self.angle + self.rotation_speed *dt 
    if self.angle > 360 then
      self.angle = 0
    end
   
  elseif love.keyboard.isDown('left')  
  or love.keyboard.isDown('a') then
   
    self.angle = self.angle - self.rotation_speed *dt 
    if self.angle < 0 then
      self.angle = 360
    end
    
  end

  
  
  local foward_y = math.sin(degrees_to_radians(self.angle))
  local foward_x = math.cos(degrees_to_radians(self.angle))
  
  local left_y = math.sin(degrees_to_radians(self.angle - 90))
  local left_x = math.cos(degrees_to_radians(self.angle - 90))
  
  local right_y = math.sin(degrees_to_radians(self.angle + 90))
  local right_x = math.cos(degrees_to_radians(self.angle + 90))
  
  local back_y = math.sin(degrees_to_radians(self.angle - 180))
  local back_x = math.cos(degrees_to_radians(self.angle - 180))
  
  if love.keyboard.isDown('up') 
  or love.keyboard.isDown('w') then
    --self.dy = -1
    self.vy = self.move_speed * foward_y --* self.dy
    self.vx = self.move_speed * foward_x --* self.dx
  elseif love.keyboard.isDown('down') 
  or love.keyboard.isDown('s') then
    --self.dy =  1
    self.vy = self.move_speed * back_y --* self.dy
    self.vx = self.move_speed * back_x --* self.dx
  else
    self.vy = 0
    self.vx = 0
  end
    
end

function Player:relative_angle_movement(dt)
  
  
  
  

  --four directional movement is relative to the angle the player is facing
  
  local foward_y = math.sin(degrees_to_radians(self.angle))
  local foward_x = math.cos(degrees_to_radians(self.angle))
  
  local left_y = math.sin(degrees_to_radians(self.angle - 90))
  local left_x = math.cos(degrees_to_radians(self.angle - 90))
  
  local right_y = math.sin(degrees_to_radians(self.angle + 90))
  local right_x = math.cos(degrees_to_radians(self.angle + 90))
  
  local back_y = math.sin(degrees_to_radians(self.angle - 180))
  local back_x = math.cos(degrees_to_radians(self.angle - 180))
  
  if love.keyboard.isDown('up') 
  or love.keyboard.isDown('w') then
    --self.dy = -1
    self.vy = self.move_speed * foward_y --* self.dy
    self.vx = self.move_speed * foward_x --* self.dx
  end
  if love.keyboard.isDown('down') 
  or love.keyboard.isDown('s') then
    --self.dy =  1
    self.vy = self.move_speed * back_y --* self.dy
    self.vx = self.move_speed * back_x --* self.dx
  end
  
  if love.keyboard.isDown('left') 
  or love.keyboard.isDown('a') then
    --self.dx = -1
    self.vy = self.move_speed * left_y --* self.dy
    self.vx = self.move_speed * left_x --* self.dx
  end
  
  if love.keyboard.isDown('right') 
  or love.keyboard.isDown('d') then
    --self.dx = 1
    self.vy = self.move_speed * right_y --* self.dy
    self.vx = self.move_speed * right_x --* self.dx
  end
  
  local unmoving = not love.keyboard.isDown('up') and not love.keyboard.isDown('w') and not love.keyboard.isDown('down') 
  and not love.keyboard.isDown('s') and not love.keyboard.isDown('left') 
  and not love.keyboard.isDown('a') and not love.keyboard.isDown('right') 
  and not love.keyboard.isDown('d')
  
  if unmoving then
    self.vy = 0
    self.vx = 0
  end
  
  --vector normalization
  
  
end

function Player:render_rays(player_x,player_y,ray_x,ray_y)
   love.graphics.line((player_x * self.tile_size) + half_screen_width - self.tile_size,
                        (player_y * self.tile_size) - self.tile_size,
                        (ray_x * self.tile_size) + half_screen_width - self.tile_size,
                        (ray_y * self.tile_size) - self.tile_size
    )
end

function Player:render_floor_textures_V(x,wall_height,ray_angle,cos,sin)
  --verical strip method of rendering floors
  
  --https://github.com/vinibiavatti1/RayCastingTutorial/wiki/Floorcasting
  local start = half_screen_height + wall_height + 1
  local rad_angle = degrees_to_radians(self.angle)
  dir_Cos = cos --math.cos(ray_angle)
  dir_Sin = sin --math.sin(ray_angle)
  for y = start, screen_height , round(screen_height/self.ray_count) do
  --for y = start, screen_height do
  
    local dist = screen_height/(2 * y - screen_height)
    dist = dist / math.cos(ray_angle) 
    --dist = (dist) --/ math.cos(ray_angle - rad_angle)
    
    --distance = distance * math.cos(self.rays[i][5]) 
    
    local tileX = dist * dir_Cos
    local tileY = dist * dir_Sin
    
    tileX = tileX + round(self.x + (self.w/2) - half_screen_width)/self.tile_size
    tileY = tileY + round(self.y + self.h/2)/self.tile_size
    
    --self.map[tileY][tileX]
    
    local texture = self.tile_floor_img
    local texture_x = math.floor(tileX * texture:getWidth()) % texture:getWidth()
    local texture_y = math.floor(tileY * texture:getHeight()) % texture:getHeight()
    local rect_x = ((x - 1)/self.ray_count) * half_screen_width
    local rect_width = half_screen_width/x
    --[[
    local quad_x = round(((i - 1)/self.ray_count) * self.tile_img:getWidth())
    local quad_w = round(self.tile_img:getWidth()/self.ray_count)
    
    local quad_slice = love.graphics.newQuad(
                    quad_x,
                    0,
                    quad_w,
                    self.tile_img:getHeight(),

                    self.tile_img
                  )
    --self:draw_ray_texture(img,quad,x,y)
   
    
    love.graphics.draw(self.tile_img,
      quad_slice,
      rect_x,
      half_screen_height - wall_height,
      0,
      rect_width/quad_w,
      (wall_height*2)/self.tile_img:getHeight()
      
    )
    ]]--
    
    local quad_slice = love.graphics.newQuad(
                    texture_x,
                    texture_y,
                    1,
                    1,

                    texture
                  )
    --self:draw_ray_texture(img,quad,x,y)
   
    
      love.graphics.draw(texture,
        quad_slice,
        rect_x,
        y,
        0,
        rect_width,
        (y/screen_height) * screen_height
        
        
        
        
      )
    

  end
  
  
end


function Player:render_floor_textures_H(player_angle,player_x,player_y)
  --Horizontal strip method of rendering floors
  
  local texture = self.tile_floor_img
  --local start = half_screen_height + wall_height + 1
  --local rad_angle = degrees_to_radians(self.angle)
  --dir_Cos = cos --math.cos(ray_angle)
  --dir_Sin = sin --math.sin(ray_angle)
 
  
  for y = half_screen_height,screen_height do
    
    
    local precision = 32
    local ray_sin_l = math.sin(self.rays[1][5] - player_angle)
    local ray_cos_l = math.cos(self.rays[1][5] - player_angle)
    local ray_sin_r = math.sin(self.rays[#self.rays - 1][5] + player_angle)
    local ray_cos_r = math.cos(self.rays[#self.rays - 1][5] + player_angle)
    
    local p = y - half_screen_height
    
    local poz_Z = half_screen_height
    
    local row_distance = poz_Z / p
    --local row_distance = screen_height/(2 * y - screen_height)
    --row_distance = row_distance / math.cos(player_angle) 
    
    local floor_stepX = row_distance * (ray_cos_r - ray_cos_l)/half_screen_width
    local floor_stepY = row_distance * (ray_sin_r - ray_sin_l)/half_screen_width
    
    local floorX = player_x + row_distance * ray_cos_l
    local floorY = player_y + row_distance * ray_sin_l
    --local x = 0
    for x = 0, half_screen_width do
      local cellX = round(floorX)
      local cellY = round(floorY)
      
      --self.tile_floor_img 
      --self.tile_floor_imgData
      local tx = math.floor(texture:getWidth() * (floorX - cellX)) 
      local ty = math.floor(texture:getHeight() * (floorY - cellY)) 
      floorX = floorX + floor_stepX
      floorY = floorY + floor_stepY
      
      
      
      local quad_slice = love.graphics.newQuad(
                    tx,
                    ty,
                    1,
                    1,

                    texture
                  )
    --self:draw_ray_texture(img,quad,x,y)
   
    
      love.graphics.draw(self.tile_floor_img,
        quad_slice,
        x,
        y,
        0
        
      )
      x = x + 1
      
    end
    
  end
  
end

function Player:render_walls_textures(current_x,side,wall_ray_x,wall_ray_y,x_rect,width_rect,height_wall)
  --wall projection drawing with images/textures
     -- local rect_x = ((i - 1)/self.ray_count) * half_screen_width
    local texture = self.tile_img
    local quad_x = round(((current_x - 1)/self.ray_count) * texture:getWidth())
    local quad_w = round(texture:getWidth()/self.ray_count)
    local draw_strip = false
    if quad_w == 0 then
      quad_w = 1/self.ray_count
    end
    --love.graphics.print("texture: "..tostring(round(self.tile_img:getWidth()/self.ray_count)),screen_width - 130,60 + 25 * i)
    
    
    if side == 1 then
      
      
      --x side 
      quad_x = (wall_ray_x%math.floor(wall_ray_x)) * texture:getWidth()
      --quad_w = 
      
    elseif side == 0 then
      --y side
      quad_x = (wall_ray_y%math.floor(wall_ray_y)) * texture:getHeight()
  
    end
    
    
    
    --love.graphics.setColor(HSL(200/360,.5,lightness, 1 - (distance*self.tile_size - self.tile_size)/half_screen_width))
    
    --love.graphics.setColor(HSL(200/360,.5,.5,lightness))
    
    
    local quad_slice = love.graphics.newQuad(
                    quad_x,
                    0,
                    quad_w,
                    texture:getHeight(),

                    self.tile_img
                  )
    --self:draw_ray_texture(img,quad,x,y)
   
    
    love.graphics.draw(texture,
      quad_slice,
      x_rect,
      half_screen_height - height_wall,
      0,
      width_rect/quad_w,
      (height_wall*2)/texture:getHeight()
      
    )
  
end


function Player:render_wall_rectangles(x_rect,width_rect,height_wall,color_red,color_blue,color_green)
  self:draw_ray_rectangle('line',
      x_rect,
      half_screen_height + height_wall,
      width_rect,
      screen_height - height_wall,
      color_green)
    
    --ceiling rectangle
    self:draw_ray_rectangle('line',
      x_rect,
      0,
      width_rect,
      half_screen_height - height_wall,
      color_blue)
    
    --walls rectangle
 
    self:draw_ray_rectangle('line',
      x_rect,
      half_screen_height - height_wall,
      width_rect,
      height_wall * 2,
      color_red)
    --love.graphics.setColor(1,1,1)
end


function Player:render_wall_lines(x_rect,height_wall,color_red,color_blue,color_green)
    -- local rect_x = ((i - 1)/self.ray_count) * half_screen_width
    self:draw_ray_line(x_rect,
                        0,
                        x_rect, 
                        half_screen_height - height_wall,
                        color_blue)
    
    --walls
    self:draw_ray_line(x_rect,
                        half_screen_height - height_wall,
                        x_rect,
                        half_screen_height + height_wall, 
                        color_red)
    
    --floor
    self:draw_ray_line(x_rect,
                        half_screen_height + height_wall,
                        x_rect,
                        screen_height,
                        color_green)
end

function Player:raycasting()
  --local ray_angle = degrees_to_radians(self.angle - self.fov)
  local rad_angle = degrees_to_radians(self.angle)
  --original coordinates of player
  --this division is to offest the player to its base position in the array/map
  --half of the width is subtracted from x to deal with its offest to the right
  -- anytime half screen with is used it deals with the offset
  local prev_x = (((self.x + self.w/2) - half_screen_width)/self.tile_size) + 1
  local prev_y = ((self.y + self.h/2)/self.tile_size) + 1
  
  --floor casting horizontal strip
  --self:render_floor_textures_H(rad_angle,prev_x,prev_y)
  
  --local start half_screen_height +
  
  
  
  local last_side = 2
  --wall casting
  for i = 1, #self.rays do
    --https://github.com/vinibiavatti1/RayCastingTutorial
    --https://permadi.com/1996/05/ray-casting-tutorial-table-of-contents/
    --https://lodev.org/cgtutor/raycasting.html
    
    
    --Pecision increases the step size when both sin and cos are added 
    --to the projecting ray position
    --as normally they go one tile in the horizonatal or vertical direction
    --the division increases the amount of steps and thus makes the scaling of lines more accurate
    local precision = 64
    local ray_sin = math.sin(self.rays[i][5] + rad_angle)/precision
    local ray_cos = math.cos(self.rays[i][5] + rad_angle)/precision
    
    
    local projecting_ray = {
      x = prev_x,
      y = prev_y
    }
    
   
    
    --player position in map array
    --love.graphics.print("Ray AX: "..tostring(math.floor(projecting_ray.x)),screen_width - 130,50 + 25 * i)
    --love.graphics.print("RAY AY: "..tostring(math.floor(projecting_ray.y)),screen_width - 130, 60 + 25 * i)
    
    --Digital Differential Analyser(DDA) Algorithm
    

    local max_dist = 10
    local cur_dist = 0
    
    
    local wall = 0
    while wall == 0 do
      
      projecting_ray.x = projecting_ray.x + ray_cos
      projecting_ray.y = projecting_ray.y + ray_sin
      
      
    
      wall = self.map[math.floor(projecting_ray.y)][math.floor(projecting_ray.x)]
      
    end
    
    
    cur_dist = math.sqrt(math.pow(prev_x - projecting_ray.x,2) + math.pow(prev_y - projecting_ray.y,2)) 
    
    --directional lighting partially based on whether the ray's x or y hit first
    local lightness = 0
    local side_xy = 2
    
    local xray_max = math.max(projecting_ray.x,round(projecting_ray.x))
    local xray_min = math.min(projecting_ray.x,round(projecting_ray.x))
    local yray_max = math.max(projecting_ray.y,round(projecting_ray.y))
    local yray_min = math.min(projecting_ray.y,round(projecting_ray.y))
    
    
    if xray_max - xray_min > yray_max - yray_min then
      --x hit
      side_xy = 1
      lightness = .5
    else 
      --y hit
      lightness = .40
      side_xy = 0
    end
   
    if cur_dist >= max_dist then
      lightness = .05
    end
    

    
    
    --the literal ray projection projection with collisions
    --self:render_rays(prev_x,prev_y,projecting_ray.x,projecting_ray.y)
   
    
    local distance  = math.sqrt(math.pow(prev_x - projecting_ray.x,2) + math.pow(prev_y - projecting_ray.y,2)) 
    --fix fisheye
    --tutorial correction didn't help
    --https://stackoverflow.com/questions/66591163/how-do-i-fix-the-warped-perspective-in-my-raycaster
    distance = distance * math.cos(self.rays[i][5]) 
    
    
    
    local wall_height = math.floor(half_screen_height/(distance)) 
    
    --debug
    
    --ray coordinates in map array
    --use with a low ray count or else it'll lag the framerate
    --love.graphics.print("XRayPos: "..tostring(math.floor(projecting_ray.x)),screen_width - 100,30 + 25 * i)
    --love.graphics.print("YRayPos: "..tostring(math.floor(projecting_ray.y)),screen_width - 100,40 + 25 * i)
    
    
    --colors HSL
    local red_color = HSL(3/360,
                          math.abs(1 - ((distance*self.tile_size - self.tile_size)/half_screen_width)),
                          math.abs(.5 - ((distance*self.tile_size - self.tile_size)/half_screen_width)),
                          1)--- ((distance*self.tile_size - self.tile_size)/half_screen_width)
    --[[
    local blue_color = HSL(136/360,
                        1,
                          .5 + ((distance*self.tile_size - self.tile_size)/half_screen_width),
                          1 - ((distance*self.tile_size - self.tile_size)/half_screen_width)
    local green_color = HSL(114/360,
                           1,
                           .5,--+ ((distance*self.tile_size - self.tile_size)/half_screen_width),
                            1 )--- ((distance*self.tile_size - self.tile_size)/half_screen_width)
    ]]--
    --RGB color
    --local red_color = {1, 0, 0, 1}
    local blue_color = {0, 0, 1, 1}
    local green_color = {0, 1, 0, 1}
    
    
    
    
    --drawing with lines
    
    --width of rectangle should be the size of screen the rays are being projected to
    --divided by the ray count
    --the height should be that of the screen
    local rect_x = ((i - 1)/self.ray_count) * half_screen_width
    local rect_width = half_screen_width/self.ray_count
    
    
    if rect_width <= 1 then
      rect_width = 1
    end
    
    ---------------------------------------------------------------------------------------------------------
    --rendering with lines
    
    --self:render_wall_lines(rect_x,wall_height,red_color,blue_color,green_color)
    ---------------------------------------------------------------------------------------------------------
    


    ---------------------------------------------------------------------------------------------------------
    --rendering with rectangles
    
    --self:render_wall_rectangles(rect_x,rect_width,wall_height,red_color,blue_color,green_color)
    ---------------------------------------------------------------------------------------------------------
    
    
    
    ---------------------------------------------------------------------------------------------------------
    --rendering walls with textures
    
    self:render_walls_textures(i,side_xy,projecting_ray.x,projecting_ray.y,rect_x,rect_width,wall_height)
    ---------------------------------------------------------------------------------------------------------
    
    
    
    ---------------------------------------------------------------------------------------------------------
    --https://raytomely.itch.io/raycasting-floorcasting
    --rendering floors with textures vertical scanline method
   
      self:render_floor_textures_V(i,wall_height,self.rays[i][5],ray_cos*precision,ray_sin*precision)
    ---------------------------------------------------------------------------------------------------------
   
    
    
  end
end

function Player:collide(dt)
  --the actually collision code for the library used for the world
  local x,y,vx,vy= self.x,self.y,self.vx,self.vy
  local futureX =  x + vx * dt
  local futureY =  y + vy * dt
  local nextX,nextY,cols,len = world:move(self,futureX,futureY)
  for i = 1 , len do
    local col = cols[i]
    local kind = col.other.class
  end
  
  self.x = nextX
  self.y = nextY
end




function Player:update(dt)
  
  self:update_line_angle(dt)
  --self:update_ray_position(dt)
  --self:shoot(dt)
  
  --self:update_angle(dt)
  --Note:tank_movement already has angles changing build in having both update angle and
  --it enabled just gives four buttons methods to change angle
  self:tank_movement(dt)
  --self:foward_mouse_movement(dt)
  --self:classic_2d_movement(dt)
  --self:relative_angle_movement(dt)
  
  self:collide(dt)
  
  

end




function Player:display(mode)
  
  
 
  self:raycasting()
  --self:ray_display()
  --love.graphics.print("ArrayPosX: "..tostring(
      --math.floor((((self.x + self.w/2) - half_screen_width)/self.tile_size) + 1)
      --),screen_width - 100,70)
  --love.graphics.print("ArrayPosY: "..tostring(math.floor(((self.y + self.h/2)/self.tile_size) + 1)),screen_width - 100,80)
  --love.graphics.setColor(1,1,1)
  love.graphics.print("Velocitys: "..tostring(self.vx) .. " ".. tostring(self.vy),screen_width - 120,70)
  love.graphics.print("Angle: "..tostring(math.floor(self.angle)),screen_width - 100,50)
  love.graphics.line(self.line.x1,self.line.y1,self.line.x2,self.line.y2)
  
  love.graphics.print("Rays " ..tostring(#self.rays),screen_width - 100,60)
  love.graphics.rectangle(mode,self.x,self.y,self.w,self.h)
  
  
end

return Player