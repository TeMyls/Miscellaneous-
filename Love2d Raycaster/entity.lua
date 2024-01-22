local class = require 'lib/middleclass'
local anim8 = require 'lib/anim8'
local bump = require 'lib/bump'

local Entity = class('Entity')
world = bump.newWorld()

function Entity:initialize(x,y,w,h,hp,img)
  self.x, self.y, self.w, self.h =  x,y,w,h
  world:add(self, x,y,w,h)
  self.hp = hp
  self.flipx = 1
  self.flipy = 1
  self.img = nil
  self.quad = nil
  if self.img ~= nil then
    self.grid = anim8.newGrid(self.w,self.h,self.img:getWidth(),self.img:getHeight())
    self.animations = {}
    self.animations.first = nil
    self.anim = self.animations.idle
  end
  
  --platformer code
  self.jump_height = -100
  self.gravity = -400
  self.friction = 2
  self.vy = -1
  self.vx = 0
  self.acceleration = 550
  self.vt = 300
  self.t = 1
  self.cd = 1/self.t
  --to use is to do self.cd -= dt and 
  --once its less than or equal to zero 
  --do whatever
  --set back to self.cd = self.cd = 1/self.t
  --now to self.t
  --values above one is rate in actions per second
  --values below one is longer than a second
  --this length can be determined by changing self.t
  --to your goal in second^-1
  --print("x: "..tostring(self.x))
  
  
end

function Entity:animanager(dt)
  
  
end




--methods which act on the actor regardless
function Entity:applyGravity(dt)
  --print("vx: "..tostring(self.vx))
  
  if self.vy ~= 0 then
    self.y = self.y + self.vy * dt
    self.vy = self.vy - self.gravity * dt
  end
  
  
  if self.vy > self.vt  then
    self.vy = self.vt
  end

end

function Entity:applyFriction(dt)
  
  if self.vx > .0001 or self.vx < -.0001  then
    self.vx = self.vx * (1-math.min(dt * self.friction,1))
  end
end

function Entity:takeHit()
  
end

--both input an ai manipulate the actor
function Entity:input(dt)
  
end

function Entity:ai(dt)
  
end


--keeps player interacting with the world
function Entity:collide(dt)
  local x,y,vx,vy= self.x,self.y,self.vx,self.vy
  local futureX =  x + vx * dt
  local futureY =  y + vy * dt
  local nextX,nextY,cols,len = world:move(self,futureX,futureY)
  
  self.x = nextX
  self.y = nextY
end

--removes item from the table and destroys its body
function Entity:destroy(desk,order,item)
  table.remove(desk, order)
  world:remove(item)
end


--one actually draws the other draws a box
function Entity:draw()
  love.graphics.draw(self.img,self.quad,self.x,self.y)
end

function Entity:display(mode)
  --mode used to take the place of argument 1
  love.graphics.rectangle(mode,self.x,self.y,self.w,self.h)
end



return Entity



