# https://easings.net
import math


def clamp(x, lower, upper):
	if x < lower:
		return lower
	elif x > upper:
		return upper
		
	else:
		return x

# lerp
def linear(t):
	t = clamp(t, 0.0, 1.0)
	return t


def easeInSine(t):
	t = clamp(t, 0.0, 1.0)
	return 1 - math.cos((t * math.pi) / 2)

def easeOutSine(t):
	t = clamp(t, 0.0, 1.0)
	return math.sin((t * math.pi) / 2)

def easeInOutSine(t):
	t = clamp(t, 0.0, 1.0)
	return -(math.cos(math.pi * t) - 1) / 2


def easeInQuad(t):
	t = clamp(t, 0.0, 1.0)
	return t * t

def easeOutQuad(t):
	t = clamp(t, 0.0, 1.0)
	return 1 - (1 - t) * (1 - t)

def easeInOutQuad(t):
	t = clamp(t, 0.0, 1.0)
	if t < 0.5:
		return 2 * t * t
	return 1 - math.pow(-2 * t + 2, 2) / 2


def easeInCubic(t):
	t = clamp(t, 0.0, 1.0)
	return t * t * t

def easeOutCubic(t):
	t = clamp(t, 0.0, 1.0)
	return 1 - math.pow(1 - t, 3)

def easeInOutCubic(t):
	t = clamp(t, 0.0, 1.0)
	if t < 0.5:
		return 4 * t * t * t
	return 1 - math.pow(-2 * t + 2, 3) / 2


def easeInQuart(t):
	t = clamp(t, 0.0, 1.0)
	return t * t * t * t

def easeOutQuart(t):
	t = clamp(t, 0.0, 1.0)
	return 1 - math.pow(1 - t, 4)

def easeInOutQuart(t):
	t = clamp(t, 0.0, 1.0)
	if t < 0.5:
		return 8 * t * t * t * t
	return 1 - math.pow(-2 * t + 2, 4) / 2


def easeInQuint(t):
	t = clamp(t, 0.0, 1.0)
	return  t * t * t * t * t

def easeOutQuint(t):
	t = clamp(t, 0.0, 1.0)
	return 1 - math.pow(1 - t, 5)

def easeInOutQuint(t):
	t = clamp(t, 0.0, 1.0)
	if t < 0.5:
		return 16 * t * t * t * t * t
	return 1 - math.pow(-2 * t + 2, 5) / 2


def easeInExpo(t):
	t = clamp(t, 0.0, 1.0)
	if t == 0.0:
		return 0.0
	return math.pow(2, 10 * t - 10)

def easeOutExpo(t):
	t = clamp(t, 0.0, 1.0)
	if t == 1.0:
		return 1.0
	return 1 - math.pow(2, -10 * t)

def easeInOutExpo(t):
	t = clamp(t, 0.0, 1.0)
	if t == 0.0:
		return 0.0
	if t == 1.0:
		return 1.0
	if t < 0.5:
		return math.pow(2, 20 * t - 10) / 2
	return (2 - math.pow(2, -20 * t + 10)) / 2


def easeInCirc(t):
	t = clamp(t, 0.0, 1.0)
	return 1 - math.sqrt(1 - math.pow(t, 2))

def easeOutCirc(t):
	t = clamp(t, 0.0, 1.0)
	return math.sqrt(1 - math.pow(t - 1, 2))

def easeInOutCirc(t):
	t = clamp(t, 0.0, 1.0)
	if t < 0.5:
		return (1 - math.sqrt(1 - math.pow(2 * t, 2))) / 2
	return (math.sqrt(1 - math.pow(-2 * t + 2, 2)) + 1) / 2


def easeInBack(t):
	t = clamp(t, 0.0, 1.0)
	c1 = 1.70158
	c3 = c1 + 1
	return c3 * t * t * t - c1 * t * t

def easeOutBack(t):
	t = clamp(t, 0.0, 1.0)
	c1 = 1.70158
	c3 = c1 + 1
	return 1 + c3 * math.pow(t - 1, 3) + c1 * math.pow(t - 1, 2)

def easeInOutBack(t):
	t = clamp(t, 0.0, 1.0)
	c1 = 1.70158
	c2 = c1 * 1.525
	if t < 0.5:
		return (math.pow(2 * t, 2) * ((c2 + 1) * 2 * t - c2)) / 2
	return (math.pow(2 * t - 2, 2) * ((c2 + 1) * (t * 2 - 2) + c2) + 2) / 2


def easeInElastic(t):
	t = clamp(t, 0.0, 1.0)
	c4 = (2 * math.pi) / 3
	if t == 0.0:
		return 0.0
	if t == 1.0:
		return 1.0
	return -math.pow(2, 10 * t - 10) * math.sin((t * 10 - 10.75) * c4)
	
def easeOutElastic(t):
	t = clamp(t, 0.0, 1.0)
	c4 = (2 * math.pi) / 3
	if t == 0.0:
		return 0.0
	if t == 1.0:
		return 1.0
	return math.pow(2, -10 * t) * math.sin((t * 10 - 0.75) * c4) + 1

def easeInOutElastic(t):
	t = clamp(t, 0.0, 1.0)
	c5 = (2 * math.pi)/ 4.5
	if t == 0.0:
		return 0.0
	if t == 1.0:
		return 1.0
	if t < 0.5:
		return -(math.pow(2, 20 * t - 10) * math.sin((20 * t - 11.125) * c5)) / 2
	return (math.pow(2, -20 * t + 10) * math.sin((20 * t - 11.125) * c5)) / 2 + 1

def easeOutBounce(t):
	n1 = 7.5625
	d1 = 2.75

	if t < (1 / d1):
		return n1 * t * t
	elif t < (2 / d1):
		t = t - 1.5 / d1
		return n1 * t * t + 0.75
	elif t < (2.5 / d1):
		t = t - 2.25 / d1
		return n1 * t * t + 0.9375
	else:
		t = t - 2.625 / d1
		return n1 * t * t + 0.984375

def easeInBounce(t):
	return 1 - easeOutBounce(1 - t)

def easeInOutBounce(t):
	if t < 0.5:
		return (1 - easeOutBounce(1 - 2 * t)) / 2
	return (1 + easeOutBounce(2 * t - 1)) / 2

easings = {
		"linear": linear,

		"easeInSine": easeInSine,
		"easeInQuad": easeInQuad,
		"easeInCubic": easeInCubic,
		"easeInQuart": easeInQuart,
		"easeInQuint": easeInQuint,
		"easeInExpo": easeInExpo,
		"easeInCirc": easeInCirc,
		"easeInBack": easeInBack,
		"easeInElastic": easeInElastic,
		"easeInBounce":easeInBounce,

		"easeOutSine": easeOutSine,
		"easeOutQuad": easeOutQuad,
		"easeOutCubic": easeOutCubic,
		"easeOutQuart": easeOutQuart,
		"easeOutQuint": easeOutQuint,
		"easeOutExpo": easeOutExpo,
		"easeOutCirc": easeOutCirc,
		"easeOutBack": easeOutBack,
		"easeOutElastic": easeOutElastic,
		"easeOutBounce":easeOutBounce,

		"easeInOutSine": easeInOutSine,
		"easeInOutQuad": easeInOutQuad,
		"easeInOutCubic": easeInOutCubic,
		"easeInOutQuart": easeInOutQuart,
		"easeInOutQuint": easeInOutQuint,
		"easeInOutExpo": easeInOutExpo,
		"easeInOutCirc": easeInOutCirc,
		"easeInOutBack": easeInOutBack,
		"easeInOutElastic": easeInOutElastic,
		"easeInOutBounce":easeInOutBounce
	
	}

def interpolate(a, b, percentage, ease_type = "linear"):
	return a + (b - a) * easings[ease_type](percentage)

print(interpolate(3, 7, 0.73, "linear"))
print(interpolate(3, 7, 0.73, "easeInBack"))
print(interpolate(3, 7, 0.73, "easeInOutElastic"))


