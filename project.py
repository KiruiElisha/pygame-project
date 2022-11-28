#!/usr/bin/env python3
import pygame
import sys
from math import pi  
pygame.init()  
color = (14, 1, 130 )
window = pygame.display.set_mode((800,700))
window.fill(color)

fps = 500
fpsClock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 20)



class Robot():
	def head():
		head = pygame.image.load('images/head1.png')
		head = pygame.transform.scale(head, (100,100))				
		return window.blit(head, (200,0))
	def head2():
		head2 = pygame.image.load('images/h5.png')
		head2 = pygame.transform.scale(head2, (100,110))				
		return window.blit(head2, (200,0))


	def body():
		body = pygame.image.load('images/body.png')
		body= pygame.transform.scale(body, (150,200))		
		return window.blit(body, (175,95))

	def left_leg():
		left_leg = pygame.image.load('images/leg2.png')		
		left_leg = pygame.transform.scale(left_leg, (55,230))		
		return window.blit(left_leg, (270,260))

	def right_leg():
		right_leg = pygame.image.load('images/leg1.png')		
		right_leg = pygame.transform.scale(right_leg, (55,230))		
		return window.blit(right_leg,(180,260))

	def right_arm():
		right_arm = pygame.image.load('images/right_arm.png')		
		right_arm = pygame.transform.scale(right_arm, (30,80))		
		return window.blit(right_arm,(150,120))

	def left_arm():
		left_arm = pygame.image.load('images/left_arm.png')		
		left_arm = pygame.transform.scale(left_arm, (30,80))		
		return window.blit(left_arm, (320,120))

	def right_elbow():
		right_elbow = pygame.image.load('images/elbow2.png')		
		right_elbow = pygame.transform.scale(right_elbow, (30,90))		
		return window.blit(right_elbow,(150,200))

	def left_elbow():
		left_elbow = pygame.image.load('images/elbow1.png')		
		left_elbow = pygame.transform.scale(left_elbow, (30,90))		
		return  window.blit(left_elbow, (320,200))

	def rotated_head():
		head = pygame.image.load('images/head1.png')
		head = pygame.transform.scale(head, (100,100))				
		return window.blit(head, (200,0))

	def straight_arm():
		left_arm = pygame.image.load('images/rotated_arm.png')		
		left_arm = pygame.transform.scale(left_arm, (90,50))		
		return window.blit(left_arm, (320,110))

	def straight_elbow():
		left_elbow = pygame.image.load('images/straight.png')		
		left_elbow = pygame.transform.scale(left_elbow, (30,90))		
		return  window.blit(left_elbow, (350,150))

	
	def up_elbow():
		left_elbow = pygame.image.load('images/up1.png')		
		left_elbow = pygame.transform.scale(left_elbow, (30,70))		
		return  window.blit(left_elbow, (410,49))


	def floating_arm():
		left_elbow = pygame.image.load('images/straight.png')
		left_elbow = pygame.transform.scale(left_elbow, (90, 30))
		return  window.blit(left_elbow, (412,125))

 	# def rotated_head():
 	# 	head = pygame.image.load('h3.png')
 	# 	head = pygame.transform.scale(head, (100,100))
 	# 	return window.blit(head, (200,0))
class Button():
	def __init__(self, x, y, width, height, buttonText='Button'):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self
		self.clicked = False
		self.buttonSurface = pygame.Surface((self.width, self.height))
		self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
		self.fillColors = {
            'normal': '#d413ed',
            'hover': '#666666',
            'pressed': '#333333',
        }
	def process(self):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()
		#check mouseover and clicked conditions
		self.buttonSurface.fill(self.fillColors['normal'])
		if self.buttonRect.collidepoint(pos):
			self.buttonSurface.fill(self.fillColors['hover'])
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.buttonSurface.fill(self.fillColors['pressed'])
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
		window.blit(self.buttonSurface, self.buttonRect)

		return action

def standing():
	head = Robot.head()
	Body = Robot.body()
	right_arm = Robot.right_arm()
	left_arm = Robot.left_arm()
	right_elbow = Robot.right_elbow()
	left_elbow = Robot.left_elbow()	
	right_leg = Robot.left_leg()
	left_leg = Robot.right_leg()
	return (head,Body,right_arm,left_arm,right_elbow,left_elbow,right_leg,left_leg)

def up():
	head = Robot.head2()
	Body = Robot.body()
	right_arm = Robot.right_arm()
	left_arm = Robot.straight_arm()
	right_elbow = Robot.right_elbow()
	left_elbow = Robot.up_elbow()	
	right_leg = Robot.left_leg()
	left_leg = Robot.right_leg()
	return (head,Body,right_arm,left_arm,right_elbow,left_elbow,right_leg,left_leg)

def straight_arm():
	head = Robot.head()
	Body = Robot.body()
	right_arm = Robot.right_arm()
	left_arm = Robot.straight_arm()
	right_elbow = Robot.right_elbow()
	left_elbow = Robot.floating_arm()	
	right_leg = Robot.left_leg()
	left_leg = Robot.right_leg()
	return (head,Body,right_arm,left_arm,right_elbow,left_elbow,right_leg,left_leg)




def animate():
	window.fill(color)
	standing()
	pygame.time.wait(2000)
	window.fill(color)
	straight_arm()
	pygame.time.wait(2000)
	window.fill(color)
	up()
	
	
	 

	

def endgame():
	running = False


animateButton = Button(400, 500, 150, 80, 'Animate')
ExitButton = Button(620, 500, 150, 80, 'Exit')
standing()

running = True
while running:	
	if animateButton.process():
		# animate()
		window.fill(color)
		standing()
		pygame.display.flip()
		pygame.time.wait(2000)
		window.fill(color)
		straight_arm()
		pygame.display.flip()
		pygame.time.wait(2000)
		window.fill(color)
		up()
		pygame.display.flip()
		
	if ExitButton.process():
		running = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()	
	pygame.display.flip()
	#fpsClock.tick(fps)



