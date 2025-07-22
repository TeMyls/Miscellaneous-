import math
import random

#https://www.jeffreythompson.org/collision-detection/table_of_contents.php
#collisions
#floats preferable on all arguments

def get_distance(x1, y1, x2, y2):
  dx = x1 - x2
  dy = y1 - y2
  s = dx * dx + dy * dy
  return math.sqrt(s)


def point_point(x1, y1, x2, y2, buffer = 0):
  #exact points
  #buffer
  b = buffer
  if x1 + b <= x2 <= x1 - b and 1 + b <= y2 <= y1 - b:
    return True
  else:
    return False
  



def point_circle(px, py, cx, cy, r):
  #get distance between the point and the circle's center
  dist = get_distance(px, py, cx, cy)
  #if the distance is less than the circle's radius,
  #the point is inside
  if dist <= r:
    return True
  
  return False


def circle_circle(cx1, cy1, cr1, cx2, cy2, cr2):
  #get distance between the circle's centers
  dist = get_distance(cx1, cy1, cx2, cy2)
  #if the distance is less the circle's
  #radii, the circles are touching
  if dist <= cr1 + cr2: 
      return True
  
  return False



def point_rectangle(px, py, rx, ry, rw, rh):
  #is the point inside the rectangles bounds
  #right ot the left edge   #left of the right edge     #below the top    #above the bottom
  if px >= rx and px <= rx + rw and py >= ry and py <= ry + rh:   
    return True
  
  return False


def rectangle_rectangle(rx1, ry1, rw1, rh1, rx2, ry2, rw2, rh2):
  #AABB
  #or axis aligned bounding box
  if rx1 + rw1 >= rx2 and rx1 <= rx2 + rw2 and ry1 + rh1 >= ry2 and ry1 <= ry2 + rh2:
    return True
  
  return False


def circle_rectangle(cx, cy, r, rx, ry, rw, rh):
  test_x = cx
  test_y = cy

  #which edge is closest
  if cx < rx:  #test left edge
    test_x = rx
  elif cx > rx + rw:  #test right edge
    test_x = rx + rw
  

  if cy < ry: #test top edge
    test_y = ry
  elif cy > ry + rh: #test bottom edge
    test_y = ry + rh
  

  dist = get_distance(cx, cy, test_x, test_y)

  #if the distance is less than the radius collision
  if dist <= r: 
    return True
  
  return False



def line_point(x1, y1, x2, y2, px, py, buffer = 0):
  #distance from the point to the two end of the line
  
  dist_1 = get_distance(px, py, x1, y1)
  dist_2 = get_distance(px, py, x2, y2)

  #the length of the line segment
  line_len = get_distance(x1, y1, x2, y2)
  #buffer
  b = buffer
  if dist_1 + dist_2 >= line_len - b and dist_1 + dist_2 <=  line_len + b:
    return True

  return False


def line_circle(x1, y1, x2, y2, cx, cy, r):
  #is either  inside the circle
  #if so return True immediately
  inside_1 = point_circle(x1, y1, cx, cy, r)
  inside_2 = point_circle(x2, y2, cx, cy, r)

  if inside_1 or inside_2: 
    return True
  
  #getting the length the line
  line_len = get_distance(x1, y1, x2, y2)

  #getting the dot product of the line and circle
  dot = (((cx - x1) * (x2 * x1)) + ((cy - y1) * (y2 - y1))) /  (line_len * line_len)
  #closest point on the line
  closest_x = x1 + (dot * (x2 - x1))
  closest_y = y1 + (dot * (y2 - y1))
  #is the point actually on the line segment
  #if so keep going if not return False
  on_segment = line_point(x1, y1, x2, y2, closest_x, closest_y)

  if not on_segment:
    return False

  dist = get_distance(cx, cy, closest_x, closest_y)

  if dist <= r:
    return True
  
  return False



def line_line(x1, y1, x2, y2, x3, y3, x4, y4):
  #calculate the distance to the intersection point
  uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
  uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
  #if uA and uB are between 0-1, lines are colliding
  if uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1: 
    return True
  
  return False

def line_line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
  #calculate the distance to the intersection point
  uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
  uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
  #if uA and uB are between 0-1, lines are colliding
  if uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1: 
    intersection_x = x1 + (uA * (x2 - x1))
    intersection_y = y1 + (uA * (y2 - y1))
    return [intersection_x, intersection_y]
  
  return []



def line_rectangle(x1, y1, x2, y2, rx, ry, rw, rh):
    #check if the line has hit any of the rectangle's sides
    #uses the Line/Line def below
    left =   line_line(x1,y1,x2,y2, rx,ry,rx, ry+rh)
    right =  line_line(x1,y1,x2,y2, rx+rw,ry, rx+rw,ry+rh)
    top =    line_line(x1,y1,x2,y2, rx,ry, rx+rw,ry)
    bottom = line_line(x1,y1,x2,y2, rx,ry+rh, rx+rw,ry+rh)

    #if ANY of the above are True, the line
    #has hit the rectangle
    if left or right or top or bottom:
      return True
    
    return False



def polygon_point(vertices, px, py):
  #vertices arranged in x, y, x, y to allow easy polygons 
  #the least amount of vertex a shape can have is 3, a triangle, meaning 3 pairs of x y coords
  collision = False

  if len(vertices) >= 6:
    v_len = (len(vertices))
    for i in range(0, v_len, 2):
      #current and next index
      cx_ind = i
      cy_ind = i + 1
      nx_ind = (i + 2) % (v_len)
      ny_ind = (i + 3) % (v_len)

      vcx = vertices[cx_ind]
      vcy = vertices[cy_ind]
      vnx = vertices[nx_ind]
      vny = vertices[ny_ind]
    
      if ((vcy >= py and vny < py) or (vcy < py and vny >= py)) and px < (vnx-vcx)*(py-vcy) / (vny-vcy)+vcx:
          collision = not collision

  return collision



def polygon_circle(vertices, cx, cy, r):
  #vertices arranged in x, y, x, y to allow easy polygons 
  #the least amount of vertex a shape can have is 3, a triangle, meaning 3 pairs of x y coords
  collision = False

  if len(vertices) >= 6:
    v_len = (len(vertices))
    for i in range(0, v_len, 2):
      #current and next index
      cx_ind = i
      cy_ind = i + 1
      nx_ind = (i + 2) % (v_len)
      ny_ind = (i + 3) % (v_len)

      vcx = vertices[cx_ind]
      vcy = vertices[cy_ind]
      vnx = vertices[nx_ind]
      vny = vertices[ny_ind]
    
      collision = line_circle(vcx, vcy, vnx, vny, cx, cy, r)
      if collision: 
        return True

  return False



def polygon_rectangle(vertices, rx, ry, rw, rh):
  #vertices arranged in x, y, x, y to allow easy polygons 
  #the least amount of vertex a shape can have is 3, a triangle, meaning 3 pairs of x y coords
  collision = False

  if len(vertices) >= 6:
    v_len = (len(vertices))
    for i in range(0, v_len, 2):
      #current and next index
      cx_ind = i
      cy_ind = i + 1
      nx_ind = (i + 2) % (v_len)
      ny_ind = (i + 3) % (v_len)

      vcx = vertices[cx_ind]
      vcy = vertices[cy_ind]
      vnx = vertices[nx_ind]
      vny = vertices[ny_ind]
    
      collision = line_rectangle(vcx, vcy, vnx, vny, rx, ry, rw, rh)
      if collision: 
        return True

  return False



def polygon_line(vertices, x1, y1, x2, y2):
  #vertices arranged in x, y, x, y to allow easy polygons 
  #the least amount of vertex a shape can have is 3, a triangle, meaning 3 pairs of x y coords
  collision = False

  if len(vertices) >= 6:
    v_len = (len(vertices))
    for i in range(0, v_len, 2):
      #current and next index
      cx_ind = i
      cy_ind = i + 1
      nx_ind = (i + 2) % (v_len)
      ny_ind = (i + 3) % (v_len)

      vcx = vertices[cx_ind]
      vcy = vertices[cy_ind]
      vnx = vertices[nx_ind]
      vny = vertices[ny_ind]
    
      collision = line_line(x1, y1, x2, y2, vcx, vcy, vnx, vny)
      if collision: 
        return True

  return False



def polygon_polygon(vertices, vertices_2):
  #vertices arranged in x, y, x, y to allow easy polygons 
  #the least amount of vertex a shape can have is 3, a triangle, meaning 3 pairs of x y coords
  collision = False

  if len(vertices) >= 6:
    v_len = (len(vertices))
    for i in range(0, v_len, 2):
      #current and next index
      cx_ind = i
      cy_ind = i + 1
      nx_ind = (i + 2) % (v_len)
      ny_ind = (i + 3) % (v_len)

      vcx = vertices[cx_ind]
      vcy = vertices[cy_ind]
      vnx = vertices[nx_ind]
      vny = vertices[ny_ind]
    
      collision = polygon_line(vertices_2, vcx, vcy, vnx, vny)
      if collision:
        return True
      
  
    
    
  
  return False



def triangle_point(x1, y1, x2, y2, x3, y3, px, py):

    areaOrig = math.abs( (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1) )

    #get the area of 3 triangles made between the point
    #and the corners of the triangle
    area1 =    math.abs( (x1-px)*(y2-py) - (x2-px)*(y1-py) )
    area2 =    math.abs( (x2-px)*(y3-py) - (x3-px)*(y2-py) )
    area3 =    math.abs( (x3-px)*(y1-py) - (x1-px)*(y3-py) )

    #if the sum of the three areas equals the original,
    #we're inside the triangle!
    if area1 + area2 + area3 == areaOrig: 
      return True

    return False














