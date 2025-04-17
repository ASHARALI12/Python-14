import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle() 
num_sides = 6
length_sides = 70
angle = 360 / num_sides
for i in range(num_sides):
    polygon.forward(length_sides)
    polygon.right(angle)

turtle.done()