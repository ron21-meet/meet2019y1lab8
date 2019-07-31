import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly
turtle.bgcolor("black")
turtle.color("orange")
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 5
TIME_STEP = 100

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
fod_pos = []
fod_stamp = []
block_pos = [(140,100), (-140,-100),(140,-100),(-140,100)]

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos) 
    #snake.stamp() returns a stamp ID. Save it in some variable         
    josh = snake.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(josh)

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i in range (START_LENGTH):
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp()

def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position

snake.direction = "Up"
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400



def up():
    snake.direction="Up" #Change direction to up
    print("You pressed the up key!")

#2. Make functions down(), left(), and right() that change snake.direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up, "Up") # Create listener for up key

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()
turtle.register_shape("apple.gif")
turtle.register_shape("rainbow.gif")
turtle.register_shape("blue.gif")
turtle.register_shape("red.gif")
block = turtle.clone()
block.shape("blue.gif")
fod = turtle.clone()
fod.shape("rainbow.gif")
food = turtle.clone()
food.shape("apple.gif")
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
for i in food_pos:
    food.goto(i)
    ron = food.stamp()
    food_stamps.append(ron)
block.goto
def rainbow():
    fod.goto(0,0)
    fod_stamp.append(fod.stamp())
    yooo = fod.pos()
    fod_pos.append(yooo)
rainbow()  

block.goto(140,100)
block.stamp()
block.goto(-140,-100)
block.stamp()
block.goto(-140,100)
block.stamp()
block.goto(140,-100)
block.stamp()
def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    if (food_x, food_y) not in block_pos:
        food.goto(food_x, food_y)
        food_pos.append(food.pos())
        a = food.stamp()
        food_stamps.append(a)
    

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position 
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
    elif snake.direction == "right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
    elif snake.direction == "left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
  


    #4. Write the conditions for RIGHT and LEFT on your own
    ##### YOUR CODE HERE

    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this

    new_stamp()

    ######## SPECIAL PLACE - Remember it for Part 5

    #remove the last piece of the snake (Hint Functions are FUN!)
    remove_tail()
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
        print("you hit the right edge! game over!")
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("you hit the left edge! game over!")
        quit()
    if new_y_pos >= UP_EDGE:
        print("you hit the up edge! game over!")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print("you hit the down edge! game over!")
        quit()
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
        new_stamp()
    elif snake.pos() in pos_list[0:-1]:
        print("you suicide!")
        quit()
    if snake.pos() in fod_pos:
        fod_index = fod_pos.index(snake.pos())
        fod.clearstamp(fod_stamp[fod_index])
        fod_pos.pop(fod_index)
        fod_stamp.pop(fod_index)
        new_stamp()
        new_stamp()
        new_stamp()
        new_stamp()
        new_stamp()
        global TIME_STEP
        TIME_STEP -= 10
        turtle.ontimer(rainbow,25000)
        print("yoooooo")
        
    
    if len(food_stamps) <= 6 :
        make_food()  
    if snake.pos() in block_pos:
        print("you died")
        quit()
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()

   
def right():
    snake.direction="right"
    print("you pressed the right key")
def left():
    snake.direction = "left"
    print("you pressed the left key")
def down():
    snake.direction = "Down"
    print("you pressed the down key")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(down, "Down")
turtle.done()
