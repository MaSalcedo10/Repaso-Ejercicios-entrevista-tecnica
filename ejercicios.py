import turtle

window = turtle.Screen()

tortuga = turtle.Turtle()
tortuga.speed(2)
tortuga.left(90)

def dibujarArbol(tamañoDeRama, tortuga):
    if tamañoDeRama > 10:
        tortuga.forward(tamañoDeRama)
        tortuga.right(45)
        dibujarArbol(tamañoDeRama / 2, tortuga)
        tortuga.left(90)
        dibujarArbol(tamañoDeRama /2 , tortuga)
        tortuga.right(45)
        tortuga.backward(tamañoDeRama)
        
dibujarArbol(100, tortuga)



# tortuga.forward(100)
# tortuga.left(45)
# tortuga.forward(50)

# tortuga.backward(50)
# tortuga.right(90)

# tortuga.forward(50)
# tortuga.backward(50)

# tortuga.left(45)
# tortuga.backward(100)

window.exitonclick()