import turtle as tl 

def draw_circle(radius):
    tl.circle(radius)


tl.speed(0)
for i in range(18):
    c = ['blue', 'red', 'green', 'yellow', 'purple'][i % 5]
    tl.color(c)
    tl.left(20)
    # for _ in range(3):
    #     tl.forward(100)
    #     tl.left(120)

    draw_circle(100)

tl.right(90)
tl.forward(100)

radius = 100
tl.circle(radius, 90) 
tl.done()