import pygame

pygame.init()


canvas = pygame.display.set_mode((400,400))

pygame.display.set_caption("Bouncing ball")

bg = pygame.image.load("bg.jpg")
x=170
y=200
x1=250
y1=200
x2=170
y2=380
x3=250
y3=20
z=0
speed=0.01
t=1

#ballrect = ball.get_rect()

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
   
    canvas.blit(bg,(0,0))   
        
    if y<380 and z<18001:
        y=y+speed
        y1=y1-speed
        pygame.draw.circle(canvas, "red", (x,y), 20)
        pygame.draw.circle(canvas, "green", (x1,y1), 20)
        z=z+1
        print(z)
    if z == 18001:
        y=y-speed
        y1=y1+speed
        pygame.draw.circle(canvas, "red", (x2,y), 20)
        pygame.draw.circle(canvas, "green", (x3,y1), 20)
        print("hi",z,"h",y)
        if y<20:
            z=0
            
   # canvas.blit(bg,(0,0))
   # pygame.draw.circle(canvas, "red", (x,y), 20)
    #pygame.draw.circle(canvas, "green", (x1,y1), 20)
    pygame.display.update()


