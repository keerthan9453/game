import turtle  
import time  #here time is the library 
import random
gamespeed = 0.3 #global  variable cause we need the whole thing to have the same game speed




name= input("Enter your name :") 
score=0

bodypart = []
flag = False


# create a window
window = turtle.Screen()
window.screensize(450,450)
window.bgcolor('navy')



  


# create a border
border = turtle.Turtle()
border.color('red')
border.hideturtle()
border.penup()  #mpenup function helps in hiding the turtle 
border.width(3)
x= 150
border.goto(-x,x)
border.pendown()
border.goto(x,x)
border.goto(x,-x)  # goto is the function which helps in making the turtle move in a particular direction
border.goto(-x,-x)
border.goto(-x,x)
border.penup()
border.goto(0,-180)
border.write("Press Esc to Exit" , align='Center' , font=('Comic Sans Ms',18,'normal'))  # this fucntion is used to write the msg or display it 
border.pendown()  # makes the turtle appear 


# create the snake

snake = turtle.Turtle()
snake.color("green")
snake.shape('square')
snake.penup()
snake.direction = 'Right'  #deafult direction


# create an egg
egg=turtle.Turtle()
egg.shape('circle')
egg.color('white')
egg.penup()
egg.shapesize(0.7,0.7)
egg.speed(0)


#create  a scoreboard

scoreboard= turtle.Turtle()
scoreboard.shape('square')
scoreboard.color('purple')
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0,162)
scoreboard.write("{}'s  score:{} ".format(name,score) , align='center',font=('Courier', 20,'normal'))


def egg_eaten():

    global score

    if snake.distance(egg) <= 15: # here 15 is the pixels 
        xcoregg= random.randint(-150,150)
        ycoregg= random.randint(-150,150)  # we are making the egg spawn randomly 
        egg.goto(xcoregg,ycoregg)

        #create a new body

        newpart= turtle.Turtle()
        newpart.color('black')
        newpart.shape('square')
        newpart.speed(0)
        newpart.penup()
        bodypart.append(newpart)

        # update the score
        scoreboard.clear()
        score= score + 10
        
        scoreboard.write("{}'s  score: {} ".format(name,score) , align='center',font=('Courier', 20,'normal'))



          


# move the snake

def move_snake():
    if snake.direction == 'Up':
        y = snake.ycor()
        snake.sety(y+20)
        time.sleep(gamespeed)

    elif snake.direction =='Down':
        y = snake.ycor()
        snake.sety(y-20)
        time.sleep(gamespeed)

    elif snake.direction =='Left':
        x = snake.xcor()
        snake.setx(x-20)
        time.sleep(gamespeed)

    elif snake.direction =='Right':
        x = snake.xcor()
        snake.setx(x+20)
        time.sleep(gamespeed)


def go_up():
    if snake.direction != 'Down':
        snake.direction = 'Up'


def go_down():
    if snake.direction != 'Up':
        snake.direction = 'Down'


def go_right():
    if snake.direction != 'Left':
        snake.direction = 'Right'


def go_left():
    if snake.direction != 'Right':
        snake.direction = 'Left'


def key_controls():
#used for making the keyboard liten to your command/keyboard
    window.listen()

    window.onkey(go_up,'Up')
    window.onkey(go_down,'Down')
    window.onkey(go_left,'Left')
    window.onkey(go_right,'Right')

    
    window.onkey(go_up,'W')
    window.onkey(go_down,'S')
    window.onkey(go_left,'A')
    window.onkey(go_right,'D')

    
    window.onkey(go_up,'w')
    window.onkey(go_down,'s')
    window.onkey(go_left,'a')
    window.onkey(go_right,'d')
    
def move_body():
    last_index = len(bodypart)-1
    first_index = 0
    interval = -1

    for position in range(last_index,first_index,interval): # here we r giving the new body part the cordinates 
        x = bodypart[position-1].xcor()
        y = bodypart[position-1].ycor()
        bodypart[position].goto(x,y)


    if len(bodypart)>0:
         xcorsnake = snake.xcor()
         ycorsnake = snake.ycor()
         bodypart[0].goto(xcorsnake,ycorsnake)
          

def exit():
    global flag

    flag = True

def snake_is_dead():
    
    snake.direction = 'stop'  #give somevalue

    for i in bodypart :
        i.color('red"')

    time.sleep(2)

    for j in bodypart:
        j.goto(1000,1000)

    snake.goto(0,0)

   

    score = 0
    scoreboard.clear()
    scoreboard.write("{}'s score: {}".format(player_name , score),align = 'center' , font=('courier' , 24 ,'normal'))


    # screen becomes blank

    window.bgcolor('white')
    time.sleep(0.5)
    window.bgcolor('blue')
    
# these are the values we need to be true throught the game  
while True :

    window.listen()
    window.onkey(exit,'Escape')
    
    if flag == True:
        turtle.bye()
        break
    
# i am going to play
    
    move_snake()

    key_controls()

    egg_eaten()

    move_body()



        
    
                









        
                
    
















