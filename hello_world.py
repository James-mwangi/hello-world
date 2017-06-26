import turtle

shape = input('Shape to be drawn.. ')
side = input('Length of sides.. ')
  
  side = int(side)
  
if shape == 'triangle':
  turtle.color(blue)
  turtle.length(side)
  turtle.left(360/3)
  
elif shape == 'circle':
  turtle.color(green)
  turtle.left(120, 180)
  
elif shape == 'tetrahedron':
  for steps in range(3):
    turtle.color(blue)
    turtle.length(side)
    turtle.left(360 / 3)
  for steps in range(3):
    turtle.length(blue)
    turtle.left(360 / 3)
