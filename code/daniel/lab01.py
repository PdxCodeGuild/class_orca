from turtle import *

# # head
# left(90)
# forward(100)
# right(90)
# i = 0
# while i < 100:
#     forward(2)
#     left(360/100)
#     i = i + 1
# right(90)
# forward(100)

# # right leg
# right(15)
# forward(125)
# right(180)
# forward(125)
# # left leg
# right(150)
# forward(125)
# right(180)
# forward(125)
# right(15)

# # arms
# forward(85)
# # right arm
# left(135)
# forward(50)
# left(25)
# forward(50)
# left(180)
# forward(50)
# right(25)
# forward(50)
# right(45)
# # left arm
# forward(50)
# left(45)
# forward(50)
# left(180)

# done()

# # draw a square
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)

# done()

# # filling in the square
# fillcolor('red')
# begin_fill()

# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)

# end_fill()

# done()

# # drawing a star
# forward(100)
# right(144)
# forward(100)
# right(144)
# forward(100)
# right(144)
# forward(100)
# right(144)
# forward(100)

# done()

# # drawing a square with a loop
# from turtle import *

# i = 0
# while i < 4:
#     forward(100)
#     left(90)
#     i = i + 1

# done()

# # drawing a circle with a loop 
# i = 0
# while i < 360:
#     forward(1)
#     left(1)
#     i = i + 1

# done()

# # drawing a staircase
# i = 0
# while i < 4:    
# 	forward(100)
# 	left(90)
# 	forward(100)
# 	right(90)
# 	i = i + 1
# done()

# # drawing an n-sided figure
# edge_length = 300
# n_sides = 9

# i = 0
# while i < n_sides:
# 	forward(edge_length/n_sides)
# 	right(360/n_sides)
# 	i = i + 1

# done()

# # draw an 8-sided spiral
# fillcolor('blue')

# n_sides = 8
# edge_length = 0

# i = 0
# begin_fill()
# while i < 150:
# 	forward(edge_length)
# 	right(360/n_sides)
# 	i = i + 1
# 	edge_length = edge_length + 1
# end_fill()
# done()

# # draw an expanding star
# edge_length = 0
# i = 0
# while i < 100:
#     forward(edge_length)
#     right(144)
#     edge_length += 4
#     i += 1
# done()
    