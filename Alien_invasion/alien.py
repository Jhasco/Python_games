import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""

	def __init__(self, ai_game):
		"""Initialize the alien and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the alien images and set its rect attribute.
		self.sprites = []
		self.sprites.append(pygame.image.load
			('images/surfman_animation/surfman_1.png'))
		self.sprites.append(pygame.image.load
			('images/surfman_animation/surfman_2.png'))
		self.sprites.append(pygame.image.load
			('images/surfman_animation/surfman_3.png'))
		self.sprites.append(pygame.image.load
			('images/surfman_animation/surfman_4.png'))
		self.sprites.append(pygame.image.load
			('images/surfman_animation/surfman_5.png'))
		self.sprites.append(pygame.image.load
			('images/surfman_animation/surfman_6.png'))
		self.sprites.append(pygame.image.load
			('images/surfman_animation/surfman_7.png'))	
		self.sprites.append(pygame.image.load
			('images/surfman_animation/surfman_8.png'))
		
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's exact horizontal position
		self.x = float(self.rect.x)

	def check_edges(self):
		"""Return True if alien is at edge of screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		"""Move the alien to the right or left"""
		self.x += (self.settings.alien_speed *
						self.settings.fleet_direction)
		self.rect.x = self.x

		# Animate alien
		self.current_sprite += (0.1)
		if self.current_sprite >= len(self.sprites):
			self.current_sprite = 0

		self.image = self.sprites[int(self.current_sprite)]