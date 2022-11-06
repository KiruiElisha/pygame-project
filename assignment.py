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
    global head
    head = pygame.image.load('head1.png')
    head = pygame.transform.scale(head, (100,100))
    head = window.blit(head, (200,0))
    return head
  def rotate_head(head,angle):
    angle = 60    
    loc = head.get_rect().center 
    rot_sprite = pygame.transform.rotate(head, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite


 
  
class Body:

  def body():
    body = pygame.image.load('body.png')
    body = pygame.transform.scale(body, (150,200))
    body = window.blit(body, (175,95))
    return body

class Legs:  
  def legs():
    left_leg = pygame.image.load('leg2.png')
    left_leg = pygame.transform.scale(left_leg, (55,230))
    right_leg = pygame.image.load('leg1.png')
    right_leg = pygame.transform.scale(right_leg, (55,230))
    right_leg = window.blit(right_leg,(180,260))
    left_leg = window.blit(left_leg, (270,260))
    return left_leg, right_leg

class Hands:
  def arms():
    left_arm = pygame.image.load('left_arm.png')
    left_arm = pygame.transform.scale(left_arm, (30,80))
    right_arm = pygame.image.load('right_arm.png')
    right_arm = pygame.transform.scale(right_arm, (30,80))
    right_arm = window.blit(right_arm,(150,120))
    left_arm = window.blit(left_arm, (320,120))
    return left_arm, right_arm

  def elbow():
    left_elbow = pygame.image.load('elbow1.png')
    left_elbow = pygame.transform.scale(left_elbow, (30,90))
    right_elbow = pygame.image.load('elbow2.png')
    right_elbow = pygame.transform.scale(right_elbow, (30,90))
    right_elbow = window.blit(right_elbow,(150,200))
    left_elbow = window.blit(left_elbow, (320,200))
    return left_elbow, right_elbow


class Robot():        
    legs = Legs.legs()
    hands = Hands.arms() and Hands.elbow()
    body = Body.body()
    head = Head.head()
    
 

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

def animate():
    pass





AnimateButton = Button(400, 500, 150, 80, 'Animate', animate())
ClapButton = Button(620, 500, 150, 80, 'Clap', animate(), True)
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

