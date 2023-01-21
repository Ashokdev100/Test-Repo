import turtle as t

t.pensize(5)

t.fillcolor("pink")
t.begin_fill()
t.goto(100,0)
t.goto(0,100)
t.goto(0,0)
t.end_fill()

t.fillcolor("red")
t.begin_fill()
t.goto(-100,0)
t.goto(0,100)
t.goto(0,0)
t.end_fill()

t.fillcolor("green")
t.begin_fill()
t.goto(-100,0)
t.goto(0,-100)
t.goto(0,0)
t.end_fill()

t.fillcolor("yellow")
t.begin_fill()
t.goto(100,0)
t.goto(0,-100)
t.goto(0,0)
t.end_fill()

t.goto(0,-200)
t.goto(0,-100)
t.goto(50,-150)
t.goto(0,-100)
t.goto(-50,-150)

t.done()