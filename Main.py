import turtle # Importing the Module.
colors=['red', 'deeppink2', 'cyan', 'chartreuse', 'blue', 'yellow'] # Giving a set of Colors.
turtle.bgcolor('black') # Giving it a background Color.
turtle.speed(20) # Giving it a speed.
for x in range(360): # Starting a loop.
    turtle.pencolor(colors[x%6]) # Changing Colors.
    turtle.width(x/100+1) # Changing Width.
    turtle.forward(x) # Making turtle Move forward.
    turtle.left(59) # Making turtle turn at an angle of 59.
turtle.exitonclick() # Making the Window Exit only when Clicked.