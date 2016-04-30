import pygame
from pygame.locals import *
import sys

pygame.init()

window = pygame.display.set_mode((800,500))

fond_color = pygame.Color(95,205,228)

obstacle_1 = pygame.image.load("C:\\Users\\michael\\Pictures\\obstacle1.png")
obstacle_2 = pygame.image.load("C:\\Users\\michael\\Pictures\\obstacle2.png")

continuer = True

class Obstacle1 (pygame.sprite.Sprite):
	
	def __init__ (self,group):
		pygame.sprite.Sprite.__init__(self,group)
		
	def update(self):
		self.image = obstacle_1

bounce_obstacle1 = Obstacle1([])
grp_ob1 = pygame.sprite.Group([bounce_obstacle1])
bounce_obstacle1.image = obstacle_1
bounce_obstacle1.rect = pygame.Rect(100,350,bounce_obstacle1.image.get_width(),bounce_obstacle1.image.get_height())
pygame.sprite.Group([bounce_obstacle1])

class Obstacle2 (pygame.sprite.Sprite):
	
	def __init__ (self, group):
		pygame.sprite.Sprite.__init__(self,group)
	
	def update(self):
		self.image = obstacle_2

bounce_obstacle2 = Obstacle2([])
grp_ob2 = pygame.sprite.Group([bounce_obstacle2])
bounce_obstacle2.image = obstacle_2
bounce_obstacle2.rect = pygame.Rect(300,350,bounce_obstacle2.image.get_width(),bounce_obstacle2.image.get_height())
pygame.sprite.Group([bounce_obstacle2])

class Joueur (pygame.sprite.Sprite):
	
	
	
	cpt = 0
	
	def __init__ (self, group):
		pygame.sprite.Sprite.__init__(self, group)
	
	def update(self):
		

while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	window.fill(fond_color)
	grp_ob1.draw(window)
	grp_ob2.draw(window)
	bounce_obstacle1.update()
	bounce_obstacle2.update()
	pygame.display.update()
