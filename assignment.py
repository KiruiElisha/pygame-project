#!/usr/bin/env python3
import pygame  
from math import pi  
pygame.init()  

window = pygame.display.set_mode((800,700))
window.fill((255, 255, 255))

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


robot = Robot()

pygame.display.update()
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

