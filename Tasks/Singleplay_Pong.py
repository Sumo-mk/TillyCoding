import pygame, sys, random

#the animation section could be directly included within the while loop below the background colour definition
# but for cleanliness it looks best to have it as a separate function that is called into the loop
def opponent_animation():
     #All makes sure that opponent is roughly in line with the ball, if the ball is higher, it moves down ...
    if opponent.top <ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        player.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))  #Allows the ball to move in a random direction after it resets
    ball_speed_x *= random.choice((1,-1))
    
    

def player_animation():
    player.y += player_speed
    if player.top <= 0 :
        player.top = 0 
    if player.bottom >= screen_height:
        player.bottom = screen_height
    #teleports the player back to the middle if they go too far

def ball_animation():
    global ball_speed_x, ball_speed_y #Globalising the variables so that they are no longer local and can be used in the main program

    #animating the movement of the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #creating the collision conditions for the frame
    if ball.top <= 0 or ball.bottom >= screen_height :   #handles the vertical
        ball_speed_y *= -1
       # using <= rather than == protects from potential bug that would involve it going beyond the frame 
        # reverses the scale so that the  ball reverses direction by multiplying the speed by -1
    if ball.left <= 0 or ball.right >= screen_width:     #handles the horizontal
        ball_restart()
    

    #defining the collision conditions for the ball with the paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


pygame.init()
clock = pygame.time.Clock()

score_player = 0 
score_opponent = 0 
screen_width = 1280
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height)) #creates a display screen
pygame.display.set_caption('Pong')

opp_score = 0
play_score = 0



#Game rectangles defining
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30,30)
# corresponds to x,y,width,height

# the width and height are altered in this way to make sure the ball is centered

player = pygame.Rect(screen_width -20, screen_height/2 - 70, 10,140)
opponent = pygame.Rect(10,screen_height/2 -70,10,140)
# these are all currently empty rectangles

background_colour = pygame.Color('grey12')
light_grey = (200,200,200)

#To create the animation of movement we add a section between the definintion of the shapes and the drawing of the shapes that means that they incrementally change (move)
ball_speed_x = 7 * random.choice((1,-1))  #randomises direction for start 
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Gameplay mechanics (up or down pressed)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:        #checks if correct key pressed
                # see initialisations - have to define player speed
                player_speed += 7 
            if event.key == pygame.K_UP:
                player_speed -= 7
            #Repeat this for the other arrow
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:        
                player_speed -= 7 
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation() 
    player_animation()
    opponent_animation()
    

    #Drawing the visuals for the rectangles
    screen.fill(background_colour)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)   # takes the base sketch of a rectangle but fills it in so only a circlular shape is left
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))   #not sure what calculations are happening but this sets them to correct place on display

    pygame.display.flip()
    clock.tick(60)

