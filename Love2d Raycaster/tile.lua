local class = require 'lib/middleclass'
local anim8 = require 'lib/anim8'
local Entity = require "entity"

local Tile = class('Tile',Entity)
--the class moving tiles and switches spawn
function Tile:initialize(x,y,w,h,hp,img)
  Entity.initialize(self,x, y,w,h,hp,img)
  self.name = 'Tile'
  if img ~= nil then
    self.img = love.graphics.newImage(img)
    self.quad = love.graphics.newQuad(0,0,self.img:getWidth(),self.img:getHeight(),self.img)
  end
end

return Tile
