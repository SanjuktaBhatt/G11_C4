import pygame
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project C3")
carryOn = True
while carryOn:
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      carryOn = False             
  screen.fill(YELLOW)
  #Create a for loop for 4 iterations
  
    #Create a "stair variable to store the rectange object
    #The x coordinate and y coordinate get incremented by 50 in each iteration
   
    #Draw the rectangle object
    
  pygame.display.flip()
pygame.quit()
