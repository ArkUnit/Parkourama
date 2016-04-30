import pygame
from pygame.locals import *
import sys

pygame.init()

window = pygame.display.set_mode((800,500))
clock = pygame.time.Clock()

fond_color = pygame.Color(95,205,228)
#~ lol
obstacle_1 = pygame.image.load("C:\\Users\\michael\\Pictures\\obstacle1.png")
obstacle_2 = pygame.image.load("C:\\Users\\michael\\Pictures\\obstacle2.png")

personnage_droite_arret = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_droite_arret.png")
personnage_droite1 = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_droite1.png")
personnage_droite2 = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_droite2.png")
personnage_droite3 = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_droite3.png")

personnage_gauche_arret = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_gauche_arret.png")
personnage_gauche1 = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_gauche1.png")
personnage_gauche2 = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_gauche2.png")
personnage_gauche3 = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_gauche3.png")

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
	
	direction_droite = True
	direction_gauche = False
	continuer_animation = False
	
	cpt = 0
	
	def __init__ (self, group):
		pygame.sprite.Sprite.__init__(self, group)
	
	def update(self):
		
		if self.continuer_animation:
			if self.direction_droite:
				self.cpt += 1
				if self.cpt == 5:
					self.image = personnage_droite1
				if self.cpt == 10:
					self.image = personnage_droite2
				if self.cpt == 15:
					self.image = personnage_droite3
					self.cpt = 0
			if self.direction_gauche:
				self.cpt += 1
				if self.cpt == 5:
					self.image = personnage_gauche1
				if self.cpt == 10:
					self.image = personnage_gauche2
				if self.cpt == 15:
					self.image = personnage_gauche3
					self.cpt = 0
		

joueur = Joueur([])
grp_j = pygame.sprite.Group([joueur])
joueur.image = personnage_droite_arret
joueur.rect = pygame.Rect(300,315,joueur.image.get_width(),joueur.image.get_height())
pygame.sprite.Group([joueur])

while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				joueur.continuer_animation = True
				joueur.direction_droite = True
				joueur.direction_gauche = False
			if event.key == K_LEFT:
				joueur.continuer_animation = True
				joueur.direction_gauche = True
				joueur.direction_droite = False
		
		if event.type == KEYUP:
			if event.key == K_RIGHT:
				joueur.image = personnage_droite_arret
				joueur.continuer_animation = False
				joueur.cpt = 0
			if event.key == K_LEFT:
				joueur.image = personnage_gauche_arret
				joueur.continuer_animation = False
				joueur.cpt = 0
				
	
	if pygame.sprite.groupcollide(grp_j,grp_ob1,False,False):
		print("sa marche ")
	
	window.fill(fond_color)
	grp_ob1.draw(window)
	grp_ob2.draw(window)
	grp_j.draw(window)
	bounce_obstacle1.update()
	bounce_obstacle2.update()
	joueur.update()
	pygame.display.update()
	clock.tick(30)
