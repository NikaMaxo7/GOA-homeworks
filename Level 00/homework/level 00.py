from turtle import * 

#we are building house

speed(50)
width(6)
begin_fill()
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

#end of scquere


forward(75)
color("cyan")
left(90)

begin_fill()

forward(90)    #height of the door
right(90)

forward(50)
right(90)

forward(90)

end_fill()

penup()
goto(75, 1)
pendown()

color("cyan")
left(90)
forward(45)

penup()
goto(75, 0)
pendown()

color("cyan")
forward(47)


#end of drawing door

#start drawing roof
penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
left(120)
forward(200)

left(120)
forward(200)
end_fill()
#end of roof

#start drawing left window
penup()
goto(30, 110)
pendown()

color("black")
left(120)
forward(45)

left(90)
forward(45)

left(90)
forward(45)

left(90)
forward(45)

penup()
goto(52, 110)
pendown()

color("black")
right(180)
forward(45)

penup()
goto(30, 133)
pendown()
right(90)
forward(45)

#end of left window

#drawing second window

penup()
goto(170, 110)
pendown()

color("black")
left(90)
forward(45)

left(90)
forward(45)

left(90)
forward(45)

left(90)
forward(45)

penup()
goto(148, 110)
pendown()

left(90)
forward(45)

penup()
goto(125, 133)
pendown()

right(90)
forward(45)


#end of right window

#start of doorhandle

color("black")
penup()
goto(85, 50)
pendown()

forward(5)
right(90)
forward(3)

#end of doorhandle

penup()
goto(500, 500)
pendown()




exitonclick()