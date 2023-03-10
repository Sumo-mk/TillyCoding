import pygame, sys, random

BLACK = (50,50,255)

def box_restart():
    global box_speed_x, box_speed_y
    box.center = (screen_width/2, screen_height/2)
    box_speed_y *= random.choice((1,-1))  
    box_speed_x *= random.choice((1,-1))

 

def box_animation():
    global box_speed_x, box_speed_y 
    
    box.x += box_speed_x
    box.y += box_speed_y


    if box.top <= 0 or box.bottom >= screen_height :  
        box_speed_y *= -1
        #CHANGE COLOUR
      
    if box.left <= 0 or box.right >= screen_width:  
        box_speed_x *= -1   
        # change colour
        


pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption('DVD')


box = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 100 ,100)

background_colour = pygame.Color('grey12')
light_grey = (200,200,200)

box_speed_x = 7 * random.choice((1,-1))   
box_speed_y = 7 * random.choice((1,-1))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    box_animation() 
   
    screen.fill(background_colour)
    pygame.draw.rect(screen, light_grey, box)   
   
    pygame.display.flip()
    clock.tick(60)
