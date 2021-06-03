# initializes pygame
import pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800,600))
# Board startup
image = pygame.image.load('grid.png')
x = pygame.image.load('x.png')
o = pygame.image.load('o.png')
empty = pygame.image.load('BLANK_ICON.png')
locklist = [0,0,0,0,0,0,0,0,0]
s1 = empty
s2 = empty
s3 = empty
s4 = empty
s5 = empty
s6 = empty
s7 = empty
s8 = empty
s9 = empty
turn = 0
#Title
pygame.display.set_caption('Tic Tac Toe')
icon = pygame.image.load('grid.png')
pygame.display.set_icon(icon)

# Turn system
def turn_check(x):
    if x == 0 or x % 2 == 0:
        return True
    elif x == 1 or x % 2 != 0:
        return False
# Clear Board
def clear_board():
    s1 = empty
    s2 = empty
    s3 = empty
    s4 = empty
    s5 = empty
    s6 = empty
    s7 = empty
    s8 = empty
    s9 = empty
# Creates the Board
image = pygame.image.load('grid.png')
x = pygame.image.load('x.png')
o = pygame.image.load('o.png')
empty = pygame.image.load('BLANK_ICON.png')


def board(check):
    global s1,s2,s3,s4,s5,s6,s7,s8,s9,turn,locklist
    if check == 0:
        if pygame.mouse.get_pressed()[0] and pygame.Rect(250, 150, 90, 90).collidepoint(mouse_pos) and locklist[0] <= 0:
            if turn_check(turn) == True:
                s1 = x
            elif turn_check(turn) == False:
                s1 = o
            turn += 1
            locklist[0] += 1
        
        if pygame.mouse.get_pressed()[0] and pygame.Rect(355, 150, 90, 90).collidepoint(mouse_pos) and locklist[1] <= 0:
            if turn_check(turn) == True:
                s2 = x
            elif turn_check(turn) == False:
                s2 = o
            turn += 1
            locklist[1] += 1
        if pygame.mouse.get_pressed()[0] and pygame.Rect(460, 150, 90, 90).collidepoint(mouse_pos) and locklist[2] <= 0:
            if turn_check(turn) == True:
                s3 = x
            elif turn_check(turn) == False:
                s3 = o
            turn += 1
            locklist[2] += 1
        
        if pygame.mouse.get_pressed()[0] and pygame.Rect(250, 255, 90, 90).collidepoint(mouse_pos) and locklist[3] <= 0:
            if turn_check(turn) == True:
                s4 = x
            elif turn_check(turn) == False:
                s4 = o
            turn += 1
            locklist[3] += 1
        if pygame.mouse.get_pressed()[0] and pygame.Rect(355, 255, 90, 90).collidepoint(mouse_pos) and locklist[4] <= 0:
            if turn_check(turn) == True:
                s5 = x
            elif turn_check(turn) == False:
                s5 = o
            turn += 1
            locklist[4] += 1
        if pygame.mouse.get_pressed()[0] and pygame.Rect(460, 255, 90, 90).collidepoint(mouse_pos) and locklist[5] <= 0:
            if turn_check(turn) == True:
                s6 = x
            elif turn_check(turn) == False:
                s6 = o
            turn += 1
            locklist[5] += 1
        if pygame.mouse.get_pressed()[0] and pygame.Rect(250, 360, 90, 90).collidepoint(mouse_pos) and locklist[6] <= 0:
            if turn_check(turn) == True:
                s7 = x
            elif turn_check(turn) == False:
                s7 = o
            turn += 1
            locklist[6] += 1
        if pygame.mouse.get_pressed()[0] and pygame.Rect(355, 360, 90, 90).collidepoint(mouse_pos) and locklist[7] <= 0:
            if turn_check(turn) == True:
                s8 = x
            elif turn_check(turn) == False:
                s8 = o
            turn += 1
            locklist[7] += 1
        if pygame.mouse.get_pressed()[0] and pygame.Rect(460, 360, 90, 90).collidepoint(mouse_pos) and locklist[8] <= 0:
            if turn_check(turn) == True:
                s9 = x
            elif turn_check(turn) == False:
                s9 = o
            turn += 1
            locklist[8] += 1
        
        screen.blit(s1,(275,175))
        screen.blit(s2,(380, 175))
        screen.blit(s3,(485,175))
        screen.blit(s4,(275, 275))
        screen.blit(s5,(380,275))
        screen.blit(s6,(485, 275))
        screen.blit(s7,(275,375))
        screen.blit(s8,(380, 375))
        screen.blit(s9,(485, 375))
    if check == 1:
        locklist = [0,0,0,0,0,0,0,0,0]
        screen.blit(empty,(275,175))
        screen.blit(empty,(380, 175))
        screen.blit(empty,(485,175))
        screen.blit(empty,(275, 275))
        screen.blit(empty,(380,275))
        screen.blit(empty,(485, 275))
        screen.blit(empty,(275,375))
        screen.blit(empty,(380, 375))
        screen.blit(empty,(485, 375))

def game():
    turn = 0
    mouse_pos = pygame.mouse.get_pos()
    screen.fill((10,60,128))
    screen.blit(image, (250, 150))
    screen.blit(pygame.image.load('reset.png'), (736, 0))
    board(0)
    if pygame.mouse.get_pressed()[0] and pygame.Rect(736, 0, 90, 90).collidepoint(mouse_pos):
        board(1)
        
#   pygame.draw.rect(screen,(123,123,123),pygame.Rect(250, 150, 90, 90),2)
#   pygame.draw.rect(screen,(123,123,123),pygame.Rect(355, 150, 90, 90),2)
#   pygame.draw.rect(screen,(123,123,123),pygame.Rect(460, 150, 90, 90),2)
#   pygame.draw.rect(screen,(123,123,123),pygame.Rect(250, 255, 90, 90),2)
#   pygame.draw.rect(screen,(123,123,123),pygame.Rect(355, 255, 90, 90),2)
#   pygame.draw.rect(screen,(123,123,123),pygame.Rect(460, 255, 90, 90),2)
#   pygame.draw.rect(screen,(123,123,123),pygame.Rect(250, 360, 90, 90),2)
#   pygame.draw.rect(screen,(123,123,123),pygame.Rect(355, 360, 90, 90),2)
#   pygame.draw.rect(screen,(123,123,123),pygame.Rect(460, 360, 90, 90),2)
    
    pygame.display.update()
    
# Game loop
running = True
while running:
    pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Background
    game()
