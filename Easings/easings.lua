local easings = {}

local _sqrt, _cos, _sin, _pow = math.sqrt, math.cos, math.sin, math.pow

function easings:new()
	self.__index = self
  return setmetatable( {} , self)
end


function easings:clamp(x, lower, upper)
	if x < lower then
		return lower
    elseif x > upper then
		return upper
		
	else
		return x
    end
end

-- lerp
function easings:linear(t)
	t = easings:clamp(t, 0.0, 1.0)
	return t
end

function easings:easeInSine(t)
	t = easings:clamp(t, 0.0, 1.0)
	return 1 - _cos((t * math.pi) / 2)
end

function easings:easeOutSine(t)
	t = easings:clamp(t, 0.0, 1.0)
	return _sin((t * math.pi) / 2)
end

function easings:easeInOutSine(t)
	t = easings:clamp(t, 0.0, 1.0)
	return -(_cos(math.pi * t) - 1) / 2
end

function easings:easeInQuad(t)
	t = easings:clamp(t, 0.0, 1.0)
	return t * t
end

function easings:easeOutQuad(t)
	t = easings:clamp(t, 0.0, 1.0)
	return 1 - (1 - t) * (1 - t)
end

function easings:easeInOutQuad(t)
	t = easings:clamp(t, 0.0, 1.0)
	if t < 0.5 then
		return 2 * t * t
    end
	return 1 - _pow(-2 * t + 2, 2) / 2
end

function easings:easeInCubic(t)
	t = easings:clamp(t, 0.0, 1.0)
	return t * t * t
end

function easings:easeOutCubic(t)
	t = easings:clamp(t, 0.0, 1.0)
	return 1 - _pow(1 - t, 3)
end

function easings:easeInOutCubic(t)
	t = easings:clamp(t, 0.0, 1.0)
	if t < 0.5 then
		return 4 * t * t * t
    end
	return 1 - _pow(-2 * t + 2, 3) / 2
end

function easings:easeInQuart(t)
	t = easings:clamp(t, 0.0, 1.0)
	return t * t * t * t
end

function easings:easeOutQuart(t)
	t = easings:clamp(t, 0.0, 1.0)
	return 1 - _pow(1 - t, 4)
end

function easings:easeInOutQuart(t)
	t = easings:clamp(t, 0.0, 1.0)
	if t < 0.5 then
		return 8 * t * t * t * t
    end
	return 1 - _pow(-2 * t + 2, 4) / 2
end

function easings:easeInQuint(t)
	t = easings:clamp(t, 0.0, 1.0)
	return  t * t * t * t * t
end

function easings:easeOutQuint(t)
	t = easings:clamp(t, 0.0, 1.0)
	return 1 - _pow(1 - t, 5)
end

function easings:easeInOutQuint(t)
	t = easings:clamp(t, 0.0, 1.0)
	if t < 0.5 then
		return 16 * t * t * t * t * t
    end
	return 1 - _pow(-2 * t + 2, 5) / 2
end

function easings:easeInExpo(t)
	t = easings:clamp(t, 0.0, 1.0)
	if t == 0.0 then
		return 0.0
    end
	return _pow(2, 10 * t - 10)
end

function easings:easeOutExpo(t)
	t = easings:clamp(t, 0.0, 1.0)
	if t == 1.0 then
		return 1.0
    end
	return 1 - _pow(2, -10 * t)
end

function easings:easeInOutExpo(t)
	t = easings:clamp(t, 0.0, 1.0)
	if t == 0.0 then
		return 0.0
    end
	if t == 1.0 then
		return 1.0
    end
	if t < 0.5 then
		return _pow(2, 20 * t - 10) / 2
    end
	return (2 - _pow(2, -20 * t + 10)) / 2
end

function easings:easeInCirc(t)
	t = easings:clamp(t, 0.0, 1.0)
	return 1 - _sqrt(1 - _pow(t, 2))
end

function easings:easeOutCirc(t)
	t = easings:clamp(t, 0.0, 1.0)
	return _sqrt(1 - _pow(t - 1, 2))
end

function easings:easeInOutCirc(t)
	t = easings:clamp(t, 0.0, 1.0)
	if t < 0.5 then
		return (1 - _sqrt(1 - _pow(2 * t, 2))) / 2
    end
	return (_sqrt(1 - _pow(-2 * t + 2, 2)) + 1) / 2
end

function easings:easeInBack(t)
	t = easings:clamp(t, 0.0, 1.0)
	local c1 = 1.70158
	local c3 = c1 + 1
	return c3 * t * t * t - c1 * t * t
end

function easings:easeOutBack(t)
	t = easings:clamp(t, 0.0, 1.0)
	local c1 = 1.70158
	local c3 = c1 + 1
	return 1 + c3 * _pow(t - 1, 3) + c1 * _pow(t - 1, 2)
end

function easings:easeInOutBack(t)
	t = easings:clamp(t, 0.0, 1.0)
	local c1 = 1.70158
	local c2 = c1 * 1.525
	if t < 0.5 then
		return (_pow(2 * t, 2) * ((c2 + 1) * 2 * t - c2)) / 2
    end
	return (_pow(2 * t - 2, 2) * ((c2 + 1) * (t * 2 - 2) + c2) + 2) / 2
end

function easings:easeInElastic(t)
	t = easings:clamp(t, 0.0, 1.0)
	local c4 = (2 * math.pi) / 3
	if t == 0.0 then
		return 0.0
    end
	if t == 1.0 then
		return 1.0
    end
	return -_pow(2, 10 * t - 10) * _sin((t * 10 - 10.75) * c4)
end

function easings:easeOutElastic(t)
	t = easings:clamp(t, 0.0, 1.0)
	local c4 = (2 * math.pi) / 3
	if t == 0.0 then
		return 0.0
    end
	if t == 1.0 then
		return 1.0
    end
	return _pow(2, -10 * t) * _sin((t * 10 - 0.75) * c4) + 1
end

function easings:easeInOutElastic(t)
	t = easings:clamp(t, 0.0, 1.0)
	local c5 = (2 * math.pi)/ 4.5
	if t == 0.0 then
		return 0.0
    end
	if t == 1.0 then
		return 1.0
    end
	if t < 0.5 then
		return -(_pow(2, 20 * t - 10) * _sin((20 * t - 11.125) * c5)) / 2
    end
	return (_pow(2, -20 * t + 10) * _sin((20 * t - 11.125) * c5)) / 2 + 1
end

function easings:easeOutBounce(t)
	local n1 = 7.5625
	local d1 = 2.75

	if t < (1 / d1) then
		return n1 * t * t
	elseif t < (2 / d1) then
		t = t - 1.5 / d1
		return n1 * t * t + 0.75
	elseif t < (2.5 / d1) then
		t = t - 2.25 / d1
		return n1 * t * t + 0.9375
	else
		t = t - 2.625 / d1
		return n1 * t * t + 0.984375
	
	end
end

function easings:easeInBounce(t)
	return 1 - easings:easeOutBounce(1 - t)
end

function easings:easeInOutBounce(t)
	if t < 0.5 then
		return (1 - easings:easeOutBounce(1 - 2 * t)) / 2
	end
	return (1 + easings:easeOutBounce(2 * t - 1)) / 2
end

function easings:interpolate(a, b, percentage)
	return a + (b - a) * easings:linear(percentage)
end

return easings


