local bump = require 'lib/bump'
love.graphics.setDefaultFilter("nearest", "nearest")
font = love.graphics.newFont( "/fonts/8bitOperatorPlus-Regular.ttf" )
love.graphics.setFont(font)
world = bump.newWorld()

local Level = require('level')



function love.load()
  


 Level:new()
  
  
  
  
  
  

 
  
end




function love.update(dt)
  
  
  Level:update(dt)

end





function love.draw()
  Level:draw()
  
 
end