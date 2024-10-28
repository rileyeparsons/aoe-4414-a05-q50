# ray_ellipsoid_intersection.py

# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z

# Parameters:
#  d_l_x : int 
#   x-component of origin-referenced ray direction
#  d_l_y : int 
#   y-component of origin-referenced ray direction
#  d_l_z : int 
#   z-component of origin-referenced ray direction
#  c_l_x : int 
#   x-component offset of ray origin
#  c_l_y : int 
#   y-component offset of ray origin
#  c_l_z : int 
#   z-component offset of ray origin

# Output:
#  l_d : list
#  intersection point

# Written by Riley Parsons

import sys
import math

# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456

# helper functions  
def calc_a(d_l_x, d_l_y, d_l_z):
   a = ((d_l_x*d_l_x) + (d_l_y*d_l_y) + (d_l_z*d_l_z))/(1-(E_E*E_E))
   return a

def calc_b(d_l_x, d_l_y, d_l_z, c_l_x, c_l_y, c_l_z):
   b = 2*(((d_l_x*c_l_x) + (d_l_y*c_l_y) + (d_l_z*c_l_z))/(1-(E_E*E_E)))
   return b

def calc_c(c_l_x, c_l_y, c_l_z):
   c = ((c_l_x*c_l_x) + (c_l_y*c_l_y) + (c_l_z*c_l_z))/(1-(E_E*E_E)) - R_E_KM
   return c

# main function
def ray_ellipsoid_intersection(d_l_x, d_l_y, d_l_z, c_l_x, c_l_y, c_l_z):
  a = calc_a(d_l_x, d_l_y, d_l_z)
  b = calc_b(d_l_x, d_l_y, d_l_z, c_l_x, c_l_y, c_l_z)
  c = calc_c(c_l_x, c_l_y, c_l_z)

  disc = b*b - (4*a*c)
  if disc > 0:
    d = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
    if d >=0:
      l_d = [d*d_l_x + c_l_x, d*d_l_y + c_l_y, d*d_l_z + c_l_z]
    else:
       d = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
       l_d = [d*d_l_x + c_l_x, d*d_l_y + c_l_y, d*d_l_z + c_l_z]
  else:
    l_d = None
  if l_d:
    print(l_d[0])
    print(l_d[1])
    print(l_d[2])
  else:
    print('discriminant negative! no l_d')
  return l_d
  
# initialize script arguments
d_l_x = None
d_l_y = None
d_l_z = None
c_l_x = None
c_l_y = None
c_l_z = None

# parse script arguments
if len(sys.argv)==7:
    d_l_x =  int(sys.argv[1])
    d_l_y = int(sys.argv[2])
    d_l_z = int(sys.argv[3])
    c_l_x = int(sys.argv[4])
    c_l_y = int(sys.argv[5])
    c_l_z = int(sys.argv[6])
else:
  print('Usage: python3 ray_ellipsoid_intersection.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km')
  exit()

# write script below this line
if __name__ == '__main__':
  ray_ellipsoid_intersection(d_l_x, d_l_y, d_l_z, c_l_x, c_l_y, c_l_z)
else:
   ray_ellipsoid_intersection(d_l_x, d_l_y, d_l_z, c_l_x, c_l_y, c_l_z)
