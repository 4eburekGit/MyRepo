from turtle import *
from datetime import datetime
hideturtle()
def jump(dist,angle=0):
    penup()
    rt(angle)
    fd(dist)
    lt(angle)
    pd()
def Needle(leng,width):
    hideturtle()
    color("black")
    begin_fill()
    fd(leng)
    rt(90)
    fd(width)
    rt(90)
    fd(leng)
    rt(90)
    fd(width)
    end_fill()
def make_needle_shape(name,leng,width):
    reset()
    jump(leng)
    begin_poly()
    Needle(leng,width)
    end_poly()
    needle_form=get_poly()
    register_shape(name,needle_form)
def clock(rad):
    reset()
    pu()
    goto(0,0)
    dot(100,"red")
    pensize(2)
    goto(-191.073,-10)
    pd()
    for i in range(60):
        if i%5==0:
            dot(10,"red")
            pu()
            pd()
            if (i)//5<=3:
                write(9+i//5,False,"center",("Gothic",12,"bold"))
            if (i)//5>3:
                write(i//5-3,False,"center",("Gothic",12,"bold"))
            jump(-rad)
        else:
            dot(4,"purple")
            jump(-rad)
        right(6)
    hideturtle()
def prep():
    global Min_Needle, Hr_Needle, Sec_Needle
    mode()
    make_needle_shape("Min_Needle",70,4)
    make_needle_shape("Hr_Needle",50,8)
    make_needle_shape("Sec_Needle",100,2)
    clock(-20)
    Min_Needle = Turtle()
    Min_Needle.shape("Min_Needle")
    Hr_Needle = Turtle()
    Hr_Needle.shape("Hr_Needle")
    Sec_Needle = Turtle()
    Sec_Needle.shape("Sec_Needle")
    for Needle in Sec_Needle,Min_Needle,Hr_Needle:
        Needle.resizemode("user")
        Needle.shapesize(1,1,1)
        Needle.speed(0)
def Tick():
    t=datetime.today()
    sec=t.second+t.microsecond*0.000001
    minute=t.minute+sec/60
    hour=t.hour+minute/60
    try:
        tracer(True)
        Sec_Needle.setheading(6*sec)
        Min_Needle.setheading(6*minute)
        Hr_Needle.setheading(30*hour)
        tracer(True)
        ontimer(Tick,100)
    except Terminator:
        pass
def main():
    tracer(False)
    prep()
    tracer(True)
    Tick()
    return "EVENTLOOP"
if __name__=="__main__":
    mode("logo")
    msg = main()
    print(msg)
    mainloop()
        
    

