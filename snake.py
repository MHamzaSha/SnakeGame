import turtle
import time
import random
delay=0.1 
#score
score = 0
high_score = 0
wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)

head.direction = "stop"
#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
segment=[]
#pen
pen =turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("Score : 0 High score : 0 ",align="center", font=("Courier", 24,"normal"))
#function
def go_up():
    if head.direction !="down":
        head.direction="up"
def go_down():
    if head.direction !="up":    
        head.direction="down"
def go_left():
    if head.direction != "right": 
        head.direction="left"
def go_right(): 
    if head.direction !="left":
        head.direction="right"    
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)  
#keyboard bindings  
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")
#main game loop
while True:
    wn.update()
    move()
    #check for border collision 
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head .ycor()<-290:
        time.sleep (1)
        head.goto(0,0)
        head.direction="sleep"
        for seg in segment:
            seg.goto(1000,1000)
        segment.clear()
        score = 0
        delay=0.1
        pen.clear()
        pen.write("Score : {} High score : {}".format(score,high_score), align="center",font=("Courier",24,"normal"))    
    #check for head collision with the body segment
    for seg in segment:
        if seg.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction ="stop"
            #hide segments
            for seg in segment:
                seg.goto(1000,1000)
            segment.clear()
            score = 0
            delay=0.1
            pen.clear()
            pen.write("Score : {} High score : {}".format(score,high_score), align="center",font=("Courier",24,"normal"))    
    #check for collision with the food
    if head.distance(food) < 20:
        #move the food to random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        #add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)

        #increasing the score
        score+= 10
        
        if score > high_score:
            high_score = score
        pen.clear()    
        pen.write("Score : {} High score : {}".format(score,high_score), align="center",font=("Courier",24,"normal"))    
         
    #move end segments first in reverse order 
    for index in range(len(segment)-1,0,-1):
        x= segment[index-1].xcor()
        y= segment[index-1].ycor()
        segment[index].goto(x,y)
    #move segment 0to where the head is
    if len (segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x,y)


        
    time.sleep(delay)




wn.mainloop()
