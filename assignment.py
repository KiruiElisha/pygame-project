#!/usr/bin/env python3
import pygame
import sys
from math import pi  
pygame.init()  

window = pygame.display.set_mode((800,700))
window.fill((255, 255, 255))

fps = 60
fpsClock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 20)

class Head:  
  def head():
    head = pygame.draw.circle(window,(0,255,0),[200,50],50,0)
    return head
  def eyes():
    left_eye = pygame.draw.circle(window,(0,0,255),[225,50],5,0)
    right_eye = pygame.draw.circle(window,(0,0,255),[175,50],5,0)
    return left_eye,right_eye
  def neck():
    neck = pygame.draw.rect(window,(255,0,0),[190,100,20,10],0)
    return neck
  
  def nose():
    nose = pygame.draw.polygon(window, (255, 0, 0),[[200, 50], [190, 60],[210, 60]])
    return nose

  def mouth():
    mouth = pygame.draw.rect(window,(0,0,2),[190,70,20,10],0)
    return mouth
 
  
class Body:

  def body():
    body = pygame.draw.rect(window,(0,0,2),[130,110,140,150],0)
    return body

class Legs:  
  def legs():
    left_leg = pygame.draw.rect(window,(0,0,255),[155,260,25,150],0)
    right_leg = pygame.draw.rect(window,(0,0,255),[225,260,25,150],0)
    return left_leg,right_leg

class Hands:
  def right_hand():
    right_hand = pygame.draw.rect(window,(0,0,255),[110,110,20,75],0)
    right_elbow = pygame.draw.rect(window,(0,0,200),[110,185,20,75],0)
    return right_hand, right_elbow
  def left_hand():
    left_hand = pygame.draw.rect(window,(0,0,255),[270,110,20,75],0)
    left_elbow = pygame.draw.rect(window,(0,0,200),[270,185,20,75],0)
    return left_hand, left_elbow

class Robot():  
    head = Head.head()
    mouth = Head.mouth()
    nose = Head.nose()    
    eyes = Head.eyes()
    neck = Head.neck()
    body = Body.body()
    hands = Hands.left_hand() and Hands.right_hand()    
    legs = Legs.legs()

objects = []
class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#d413ed',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()
        
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        window.blit(self.buttonSurface, self.buttonRect)

def myFunction():
    print('Animated')





AnimateButton = Button(400, 500, 150, 80, 'Animate', myFunction)
ClapButton = Button(620, 500, 150, 80, 'Clap', myFunction, True)
robot = Robot()
pygame.display.update()
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for object in objects:
        object.process()

    pygame.display.flip()
    fpsClock.tick(fps)

