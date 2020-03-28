"""
    Author: Shivansh joshi
    External Libraries used: PyGame
    References of concept: 3Blue1Brown [What is Fourier Series? YT], Khan Academy [Fourier Transforms]
"""
import pygame, math

pygame.init()

canvas_width = 1400
canvas_height = 500

win = pygame.display.set_mode((canvas_width, canvas_height))


white = (70,70,70)
bright_white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

surface = pygame.Surface((canvas_width, canvas_height)) # Making a sureface to make the waves without refreshing the screen
surface.fill(black) # Filling the surface with a background

time_rate = 0.05 # The speed of rotations
clock = pygame.time.Clock()
run = True
time = 0
wave = [] # List to store points generated by cos() for y-axis to plot the wave

while run:
    clock.tick(60) # Running the game at 60 fps
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pos_circle_x = 150
    pos_circle_y = 150

    win.fill(black)
    surface.fill(black)
    
    x=pos_circle_x
    y=pos_circle_y

    
    # Loop to make the circles and lines 
    for i in range(10):
        prevx = x # Storing the x coordinate of the centre of last formed circle
        prevy = y # Storing the y coordinate of the centre of last formed circle
        n = 2 * i + 1 # Making n an odd number
        radius = int(70 * (4 / (n * math.pi)))   
        x +=  int(radius * math.cos(n * time)) 
        y +=  int(radius * math.sin(n * time)) 
        wave.insert(0, y-pos_circle_y) # Pushing y coordinates of the wave

        pygame.draw.line(win, bright_white, (prevx, prevy), (x, y), 2) 

        pygame.draw.circle(win, white, (prevx, prevy), radius, 1)


        prevx = x
        prevy = y

    if len(wave) > 250: wave.pop()

    # Plotting wave 
    for i in range(len(wave)):
        surface.set_at((i, wave[i]+pos_circle_y), bright_white) 

    pygame.draw.line(win, bright_white, (x, y), (300, wave[0]+pos_circle_y)) # Line between last inner circle with the wave

   
    
    time+=time_rate # rate of refreshing coordinates of the points
    
    
    win.blit(surface, (300, 0))
    pygame.display.update()

pygame.quit()