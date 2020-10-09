#!/usr/bin/python3
'''
 Explanation video: http://youtu.be/mdTeqiWyFnc
'''
import pygame
import math

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (40, 80, 200)
 
# This sets the width and height of each grid location oh yeah and additional_space as well for the sake of centering
width = 20
height = 20
additional_space = 20
# This sets the margin between each cell
margin = 5

#drag and drop ship
class Small_Ship(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, id):
        super(Small_Ship, self).__init__()
        self.image = pygame.image.load("MrsWhite.jpg").convert()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        
        
ship_group = pygame.sprite.Group() 
       
grid = []
corners = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(column+1) 

for i in grid:
    print(i)
print(grid)
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
#grid[1][5] = 1
 
# Initialize pygame
pygame.init()
 
# Set the height and width of the screen
window_size = [255, 350]
screen = pygame.display.set_mode(window_size)

 
# Set title of screen
pygame.display.set_caption("Test")
 

done = False
 

clock = pygame.time.Clock()
select_ships = False


ship_group.add(Small_Ship(40,300,len(ship_group)+1))

#establishes grid and corners

corners = []

 
while not done:
    for event in pygame.event.get(): 
        #This is an if else statement because it prevents players from holding down the button to get infinite selections
        if event.type == pygame.QUIT:
            done = True 
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            #----Drag and drop logic
            
            if event.button == 1:
                for ship in ship_group:
                    if ship.rect.collidepoint(pos):
                        ship.clicked = True
                        
        if event.type == pygame.MOUSEBUTTONUP:
            for ship in ship_group:
                ship.clicked = False
            drag_id = 0
                
            #--------------------------
            
                
            #snap to grid when dragging objects
            
            if select_ships is not True:
            
                # Change the x/y screen coordinates to grid coordinates
    
                column = pos[0] // ((width + margin))
                row = pos[1] // ((height + margin))
                
                try:
                    grid[row][column] = 1
                    print("You've Hit:", row + 1, ",", column + 1)
                
                except:
                    print("You absolute fool. Thats their territory!!!!!!!!")
        
    
    #Drag and drop logic
    
    for ship in ship_group:
        if ship.clicked == True:
            pos = pygame.mouse.get_pos()
            ship.rect.x = pos[0]-(ship.rect.width/2)
            ship.rect.y = pos[1]-(ship.rect.height/2)
            
    # Set the screen background
    screen.fill(black)
                   
    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = blue
            pygame.draw.rect(screen,
                             color,
                             [((margin + width) * column + margin),
                              (margin + height) * row + margin,
                              width,
                              height])
            
    
            
    clock.tick(60)
 
    ship_group.draw(screen)

    pygame.display.flip()
 

pygame.quit()