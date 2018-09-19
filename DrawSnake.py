import turtle
def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0)#启动了一个窗口宽,高,在屏幕的坐标位置
    pythonsize=30
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")#可以使用("#3B9909")
    turtle.seth(-40)#表示运行方向,顺时针0到170 符号表示逆时针 负40度
    drawSnake(40,80,5,pythonsize/2)

main()
