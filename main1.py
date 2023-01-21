import turtle as t

t.pensize(3)
t.pencolor("black")

t.fillcolor("green")
t.begin_fill()
t.goto(-50,0)
t.goto(0,50)
t.goto(50,0)
t.goto(-50,0)
t.end_fill()

t.fillcolor("green")
t.begin_fill()
t.goto(0,0)
t.goto(-50,-50)
t.goto(50,-50)
t.goto(0,0)
t.end_fill()

t.goto(-50,-50)
t.goto(0,-50)

t.fillcolor("green")
t.begin_fill()
t.goto(-50,-100)
t.goto(50,-100)
t.goto(0,-50)
t.end_fill()


t.goto(-50,-100)
t.goto(-5,-100)

t.goto(-5,-140)
t.goto(5,-140)
t.goto(5,-100)

t.end_fill()
t.done()
