local e = require "easings"
local easings = e:new()
print(easings:interpolate(3, 10, 0.7))