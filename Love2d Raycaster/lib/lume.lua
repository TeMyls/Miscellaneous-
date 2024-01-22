--
-- lume
--
-- Copyright (c) 2020 rxi
--
-- Permission is hereby granted, free of charge, to any person obtaining a copy of
-- this software and associated documentation files (the "Software"), to deal in
-- the Software without restriction, including without limitation the rights to
-- use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
-- of the Software, and to permit persons to whom the Software is furnished to do
-- so, subject to the following conditions:
--
-- The above copyright notice and this permission notice shall be included in all
-- copies or substantial portions of the Software.
--
-- THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
-- IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
-- FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
-- AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
-- LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
-- OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
-- SOFTWARE.
--

local lume = { _version = "2.3.0" }

local pairs, ipairs = pairs, ipairs
local type, assert, unpack = type, assert, unpack or table.unpack
local tostring, tonumber = tostring, tonumber
local math_floor = math.floor
local math_ceil = math.ceil
local math_atan2 = math.atan2 or math.atan
local math_sqrt = math.sqrt
local math_abs = math.abs

local noop = function()
end

local identity = function(x)
  return x
end

local patternescape = function(str)
  return str:gsub("[%(%)%.%%%+%-%*%?%[%]%^%$]", "%%%1")
end

local absindex = function(len, i)
  return i < 0 and (len + i + 1) or i
end

local iscallable = function(x)
  if type(x) == "function" then return true end
  local mt = getmetatable(x)
  return mt and mt.__call ~= nil
end

local getiter = function(x)
  if lume.isarray(x) then
    return ipairs
  elseif type(x) == "table" then
    return pairs
  end
  error("expected table", 3)
end

local iteratee = function(x)
  if x == nil then return identity end
  if iscallable(x) then return x end
  if type(x) == "table" then
    return function(z)
      for k, v in pairs(x) do
        if z[k] ~= v then return false end
      end
      return true
    end
  end
  return function(z) return z[x] end
end



function lume.clamp(x, min, max)
  return x < min and min or (x > max and max or x)
end


function lume.round(x, increment)
  if increment then return lume.round(x / increment) * increment end
  return x >= 0 and math_floor(x + .5) or math_ceil(x - .5)
end


function lume.sign(x)
  return x < 0 and -1 or 1
end


function lume.lerp(a, b, amount)
  return a + (b - a) * lume.clamp(amount, 0, 1)
end


function lume.smooth(a, b, amount)
  local t = lume.clamp(amount, 0, 1)
  local m = t * t * (3 - 2 * t)
  return a + (b - a) * m
end


function lume.pingpong(x)
  return 1 - math_abs(1 - x % 2)
end


function lume.distance(x1, y1, x2, y2, squared)
  local dx = x1 - x2
  local dy = y1 - y2
  local s = dx * dx + dy * dy
  return squared and s or math_sqrt(s)
end


function lume.angle(x1, y1, x2, y2)
  return math_atan2(y2 - y1, x2 - x1)
end


function lume.vector(angle, magnitude)
  return math.cos(angle) * magnitude, math.sin(angle) * magnitude
end


function lume.random(a, b)
  if not a then a, b = 0, 1 end
  if not b then b = 0 end
  return a + math.random() * (b - a)
end


function lume.randomchoice(t)
  return t[math.random(#t)]
end


function lume.weightedchoice(t)
  local sum = 0
  for _, v in pairs(t) do
    assert(v >= 0, "weight value less than zero")
    sum = sum + v
  end
  assert(sum ~= 0, "all weights are zero")
  local rnd = lume.random(sum)
  for k, v in pairs(t) do
    if rnd < v then return k end
    rnd = rnd - v
  end
end


function lume.isarray(x)
  return type(x) == "table" and x[1] ~= nil
end


function lume.push(t, ...)
  local n = select("#", ...)
  for i = 1, n do
    t[#t + 1] = select(i, ...)
  end
  return ...
end


function lume.remove(t, x)
  local iter = getiter(t)
  for i, v in iter(t) do
    if v == x then
      if lume.isarray(t) then
        table.remove(t, i)
        break
      else
        t[i] = nil
        break
      end
    end
  end
  return x
end


function lume.clear(t)
  local iter = getiter(t)
  for k in iter(t) do
    t[k] = nil
  end
  return t
end