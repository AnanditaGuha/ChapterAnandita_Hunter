import turtle
wn = turtle.Screen()


def draw_poly(t, ss, sz):
    
    for i in range(ss):
        turtle.forward(sz)
        turtle.left(120)

def drawequitriangle(t, sz):
    draw_poly(t, 3, sz)
    

drawequitriangle (turtle,100)