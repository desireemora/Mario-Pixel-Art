import pygame,sys

pygame.init()

screen_width = 700
screen_height = 400

screen = pygame.display.set_mode([screen_width,screen_height])

r = pygame.Color("red")
w = pygame.Color("white")
blu = pygame.Color("blue")
bl = pygame.Color("black")
p = pygame.Color("antiquewhite1")
br = pygame.Color("brown")
y = pygame.Color("yellow")


data = [
    [w,w,w,r,r,r,r,r,r,w,w,w],
    [w,w,r,r,r,r,r,r,r,r,r,w],
    [w,w,br,br,br,p,p,bl,p,w,w,w],
    [w,br,p,br,p,p,p,bl,p,p,p,w],
    [w,br,p,br,br,p,p,p,bl,p,p,p],
    [w,br,br,p,p,p,p,bl,bl,bl,bl,w],
    [w,w,p,p,p,p,p,p,p,p,w,w],
    [w,w,r,r,blu,r,r,r,w,w,w,w],
    [w,r,r,r,blu,r,r,blu,r,r,r,w],
    [r,r,r,r,blu,blu,blu,blu,r,r,r,r],
    [p,p,p,blu,blu,blu,blu,blu,blu,p,p,p],
    [p,p,blu,blu,blu,blu,blu,blu,blu,blu,p,p],
    [p,p,blu,blu,blu,w,w,blu,blu,blu,p,p],
    [w,w,blu,blu,blu,w,w,blu,blu,blu,w,w],
    [w,br,br,br,w,w,w,w,br,br,br,w],
    [br,br,br,br,w,w,w,w,br,br,br,br],
    
    ]

for y, row in enumerate(data):
    for x, color in enumerate(row):
        rect = pygame.Rect(x*25,y*25,25,25)
        screen.fill(color,rect = rect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
