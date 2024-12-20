import pygame
import random
from pygame import Vector2


#starting
pygame.init()
screen = pygame.display.set_mode((800,1080))
#loading images
bird_image = pygame.image.load("birdo.png")
bottom_image = pygame.image.load("pipe_down.png")
top_image = pygame.image.load("pipe_up.png")
#Setting up the x and y coords for objects
birdo = Vector2(200,100)
bottom = Vector2(900,345)
top = Vector2(900,-1745)
counter = 0
def reset():
    global birdo
    global bottom
    global top
    global counter
    birdo = Vector2(200, 100)
    bottom = Vector2(900, 345)
    top = Vector2(900, -1745)
    counter = 0
#Other values
gravity = 0.0
clock = pygame.time.Clock()
running = True
space_pressed = False
dt  = 0
#Method that checks collision
def CheckCollision(val: Vector2, val1: Vector2):
    bo = (val.x > val1.x + 100) or (val.x + 70 < val1.x) or (val.y > val1.y + 1780) or (val.y + 70 < val1.y)
    return not bo
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not space_pressed:
                birdo.y-=70
                gravity= 0.0
                space_pressed = True  # Mark spacebar as pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space_pressed = False  # Reset the flag when spacebar is released
    #Drawings
    screen.fill("white")
    screen.blit(bird_image,birdo)
    screen.blit(pygame.font.Font(None,100).render(str(counter),False,"black"),(400,220))
    screen.blit(bottom_image,bottom)
    screen.blit(top_image,top)
    pygame.display.flip()
    #checking for collisions with the pipes
    if CheckCollision(birdo,bottom):
        reset()
    if CheckCollision(birdo,top):
        reset()
    #Simulating gravity
    birdo.y+=gravity
    gravity+=0.5
    if birdo.y>1070:
        reset()
    #simulating the scrolling
    bottom.x-=5
    top.x-=5
    if bottom.x<-200:
        y = random.randint(345,945)
        bottom = Vector2(900,y)
        top = Vector2(900,y-2090)
        counter+=1
    clock.tick(60)
pygame.quit()