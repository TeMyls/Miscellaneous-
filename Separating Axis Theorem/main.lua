screen_width = love.graphics.getWidth()
screen_height = love.graphics.getHeight()

Object = require "lib.classic"
require "rect"
require "sat"
shapes = {}
counter = 2

function make_shapes(number)
  for i = 1, number do
    local rw = 30
    local rh = 30
    local rx = love.math.random(math.max(rw,rh),screen_width - math.max(rw,rh))
    local ry = love.math.random(math.max(rw,rh),screen_height - math.max(rw,rh))
    local rs = love.math.random(200,400)
    local shape = rectangle(rx,ry,rw,rh,rs)
    table.insert(shapes,shape)
  end
end

function love.load()
  make_shapes(4)

end




function love.update(dt)
  --[[
  if love.mouse.isDown(1) then
		angle = angle + .5*math.pi * dt
	elseif love.mouse.isDown(2) then
		angle = angle - .5*math.pi * dt
  end]]--
  
  for i, shape in ipairs(shapes) do
    shapes[i]:update(dt)
    --[[
    if #shapes > 1 then
      for j, shape in ipairs(shapes) do
        if i ~= j then
          local x, y, r = shapes[i]:circle_params()
          if shapes[j]:circle_collision(x, y, r) then
            if separating_axis_theorem(shapes[i]:get_vertices(),shapes[j]:get_vertices()) then
              shapes[j].mode = 'fill'
              shapes[i].mode = 'fill'
              shapes[j]:bounce()
              shapes[i]:bounce()
            else
              shapes[j].mode = 'line'
              shapes[i].mode = 'line'
            end
          end
        end
      end
    end]]--
  end
  
 
  
  
end



local function drawRotatedRectangle(mode, x, y, width, height, angle)
	local cosa, sina = math.cos(angle), math.sin(angle)

	local dx1, dy1 = width*cosa,   width*sina
	local dx2, dy2 = -height*sina, height*cosa

	local px1, py1 = x,         y
	local px2, py2 = x+dx1,     y+dy1
	local px3, py3 = x+dx1+dx2, y+dy1+dy2
	local px4, py4 = x+dx2,     y+dy2
	
	love.graphics.polygon(mode, px1,py1, px2,py2, px3,py3, px4,py4)
  
end



function love.draw()
  
  for i, shape in ipairs(shapes) do shape:draw() end
  love.graphics.print("FPS:"..tostring(love.timer.getFPS()),10,20)

  

  --[[
  local major, minor, revision, codename = love.getVersion()
  local str = string.format("Version %d.%d.%d - %s", major, minor, revision, codename)
  love.graphics.print(str, 20, 40)
  ]]--
end


