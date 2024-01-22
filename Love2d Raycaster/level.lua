local class = require 'lib/middleclass'
bump = require 'lib/bump'

world = bump.newWorld()

protag = {}
local Player = require('player')
local Tile = require('tile')
deltaTime = 0
local Level = class('Level')
TILESIZE = 32
protag = {}
tiles = {}

levels = {}



map_tiles = {
  
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
            {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1},
            {1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1},
            {1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1},
            {1,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1},
            {1,0,1,1,1,0,0,0,0,0,0,0,1,0,1,1},
            {1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1},
            {1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1},
            {1,0,1,0,1,1,1,1,0,1,1,1,1,0,1,1},
            {1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1},
            {1,0,1,1,0,1,0,0,0,1,1,1,1,1,1,1},
            {1,0,0,1,0,1,1,1,1,1,0,0,0,0,0,1},
            {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1},
            {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1},
            {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1},
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}

}

local FullMapWidth = #map_tiles[1] * TILESIZE 
local FullMapHeight = #map_tiles * TILESIZE 
local width = love.graphics.getWidth()
local height = love.graphics.getHeight()

function Level:initialize()
  local free_tiles = {}
  for y =1,#map_tiles do
    for x = 1,#map_tiles[y]  do
      --the x is offset so it projects to the side of the screen
      --why tilesize-tilesize, to offet the postion so x and y start at 0 on the screen, 
      --since lua arrays start from one
      
      if map_tiles[y][x] == 1  then
        
        local tile = Tile:new(
       
          x*TILESIZE-TILESIZE + width/2,
          y*TILESIZE-TILESIZE,
          TILESIZE,
          TILESIZE,
          nil,
          nil
          )
        
        table.insert(tiles,tile)
        
        
      elseif map_tiles[y][x] == 0 then
        table.insert(free_tiles,{x*TILESIZE-TILESIZE + width/2,y*TILESIZE-TILESIZE})
      end

    end
  end
  --Player(x*TILESIZE-TILESIZE+ width/2,y*TILESIZE-TILESIZE,TILESIZE,TILESIZE,10,nil)
  local random_tile = love.math.random(1,#free_tiles)
  local player = Player:new(
    free_tiles[random_tile][1],
    free_tiles[random_tile][2],
    --love.math.random(2,#map_tiles[1] - 2) * TILESIZE + width/2,
    --love.math.random(2,#map_tiles - 2) * TILESIZE,
    math.floor(TILESIZE/2),
    math.floor(TILESIZE/2),
    nil,
    nil
  
    
  )
  player.tile_size = TILESIZE
  player.angle = 0
  player:map_reference(map_tiles)
  table.insert(protag,player)

end


function Level:switch(key)
  
end




function love.mousepressed(x,y,button)
 
end

function love.keypressed(key)
  
end

function checkCollision(a, b)
  --'a' is meant to be self and 'b' is meant to be other
  return a.x < b.x + b.w + 3--is the left of 'a' less than the right of 'b'
  and b.x - 3 < a.x + a.w  -- is the right of 'a' greater than the left of 'b'
  and a.y < b.y + b.h + 3 -- is the top of 'a' less than the bottom of 'b'
  and b.y - 3 < a.y + a.w -- is the bottom of 'a' greater than the top of 'b' 
  and b.name ~= self.name
end


function Level:update(dt)
  --Level:offset(dt)
 
  --for i,v in ipairs (tiles) do
    
  --end
  deltaTime = dt
  for u,p in ipairs(protag) do

  
    p:update(dt)
    --
  end

    
end



function Level:draw()
  --cam:attach()
      
      for i,v in ipairs(tiles) do
          --love.graphics.setColor(1, 0, 0)
          v:display('fill')
       
      end
      
       
       
     
       
      for u,p in ipairs(protag) do
        --love.graphics.setColor(0, 0, 1)
        p:display('line')
        
        
        --love.graphics.print({{0,0,0},p.name},font,p.x + p.w/3,p.y + p.h/3)
         
      end
      --love.graphics.setColor(0, 0, 0)
      love.graphics.print(string.format("Framerate: %.0f", 1/deltaTime),100,10)
      --love.graphics.clear(1,1,1)
      love.graphics.print("MapX: "..tostring(#map_tiles[1]),width - 100,20)
  love.graphics.print("MapY: "..tostring(#map_tiles),width - 100,30)
  --cam:detach()
  



 
end


return Level
