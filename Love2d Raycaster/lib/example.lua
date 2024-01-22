SW = love.graphics.getWidth()
SH = love.graphics.getHeight()



function loader()
  --all libraries
  wf = require 'lib/windfield'
  world = wf.newWorld(0,5000)
  camera = require 'lib/camera'
  cam = camera()
  anim8 = require('lib/anim8')
  sti = require('lib/sti')
  gameMap = sti('maps/wasteland.lua')
  love.graphics.setDefaultFilter('nearest','nearest')
  bg0 = love.graphics.newImage("/maps/Wasteland_Sky.png")
  bg1 = love.graphics.newImage("/maps/Wasteland_Mountains_2.png")
  bg2 = love.graphics.newImage('/maps/Wasteland_Sky_Top.png')
  
  ---player object
  player = {}
  
  player.w = 18
 
  player.h = 16
  player.x = 10
  player.y = 10
  player.speed = 150
  player.flip = 1
  player.collider = world:newRectangleCollider(player.x,player.y,player.w,player.h)
  player.collider:setFixedRotation(true)
  
  player.img = love.graphics.newImage("/sprites/gobgob.png")
  player.grid = anim8.newGrid(18,16,162,304)
  ---list of animations
  player.animations = {}
  player.animations.idle = anim8.newAnimation(player.grid('1-8',1),0.2)
  player.animations.walk = anim8.newAnimation(player.grid('1-6',7),0.15)
  player.animations.jump = anim8.newAnimation(player.grid('1-6',12),0.15)
   player.animations.drop = anim8.newAnimation(player.grid('1-6',13),0.15)
  player.anim = player.animations.walk
      
      
      
      
  walls = {}
  if gameMap.layers['Walls'] then
    for i,obj in pairs(gameMap.layers['Walls'].objects) do 
      wall = world:newRectangleCollider(obj.x,obj.y,obj.width,obj.height)
      wall:setType('static')
      table.insert(walls,wall)
    end
  end
  
  
  
end

loader()



function love.update(dt)
  local vx = 0
  local vy = 0
  local moving = false
  local falling = false
  if love.keyboard.isDown('right') then
    vx =  player.speed 
    player.anim = player.animations.walk
    player.flip = 1
    moving = true
  elseif  love.keyboard.isDown('left') then
    vx = -1 * player.speed 
    player.anim = player.animations.walk
    player.flip = -1
    moving = true
  elseif key == 'up' then 
    vy = 5000
  end
  
  if moving == false then
    player.anim = player.animations.idle
  end
  ----
  if vy > 0 then
    player.anim = player.animations.drop
    
  end
  player.collider:setLinearVelocity(vx,vy)
  
  
  player.anim:update(dt)
  cam:lookAt(player.x,player.y)
  --camera
  local w,h = love.graphics.getWidth(),love.graphics.getHeight()
  if cam.x < w/2 then
    cam.x = w/2
  end
  if cam.y < h/2 then
    cam.y = h/2
  end
  world:update(dt)
  player.x = player.collider:getX()
  player.y = player.collider:getY()
  local mapW = gameMap.width * gameMap.tilewidth
  local mapH = gameMap.height * gameMap.tileheight
  
  if cam.x > (mapW - w/2) then
    cam.x = (mapW - w/2)
  end
  if cam.y > (mapH - h/2) then
    cam.y = (mapH - h/2)
  end
  
end

function love.keypressed(key)
  
end

function love.draw()
  
  cam:attach()
    --love.graphics.scale(2,2)
    love.graphics.draw(bg2,0,0,0,1,1)
    love.graphics.draw(bg2,512,0,0,1,1)
    love.graphics.draw(bg2,1024,0,0,1,1)
    love.graphics.draw(bg0,512,0,0,1,1)
    love.graphics.draw(bg1,0,0,0,1,1)
    love.graphics.draw(bg1,1024,0,0,1,1)
    love.graphics.draw(bg1,512,0,0,1,1)
    gameMap:drawLayer(gameMap.layers['Ground'])
    player.anim:draw(player.img,player.x,player.y,nil,1*player.flip,1,8,9)
    --draws colliders
    world:draw()
    
  cam:detach()
end
