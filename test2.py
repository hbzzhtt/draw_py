from util import *

# begin drawing ----------
canvas = Canvas()
canvas.set_label('x轴方向', 'y轴方向')
 
canvas.add_point(Point(150,100))
canvas.add_point(Point(50,600))
canvas.add_point(Point(100,475))
canvas.add_point(Point(500,200))
canvas.add_point(Point(100,600))
canvas.add_point(Point(300,475))
canvas.add_point(Point(300,200))
canvas.add_point(Point(300,100))

# canvas.add_rect(ExtRect(Point(0,0), Ext(100,50)))
# use real point
canvas.add_rect(Rect(Point(0,0), Point(200,100)))
# use left point and right_top offset
canvas.add_rect(ExtRect(Point(0,400), Ext(100,200)))
canvas.add_rect(ExtRect(Point(100,100), Ext(400,450)))
canvas.add_rect(ExtRect(Point(500,0), Ext(200,300)))

canvas.show()
