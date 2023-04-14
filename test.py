from util import Point, Rect, Canvas

# prepare data ----------
x_list = [1,2,3,4,0,6]
y_list = [2,4,0,8,3,12]
color_list = [10,20,30,40,50,60]
txt_list = ['我','今111','晚2222222222','上','吃','了','个','鲸']

left_bottom = Point(0,0)
right_top = Point(3,3)
rect = Rect(left_bottom, right_top)

# begin drawing ----------
canvas = Canvas()
canvas.set_label('x轴方向', 'y轴方向')
canvas.add_rect(rect)

plst = []
for i in range(len(x_list)):
    plst.append( Point(x_list[i], y_list[i], color_list[i], txt_list[i]) )
    canvas.add_point(plst[i])

canvas.show()