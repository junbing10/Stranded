import pygame

class Character:


   def __init__(self, x, y):
       self.x = x
       self.y = y
       self.health = 100
       self.stamina = 100
       self.image = pygame.image.load("character.png")
       self.image_size = self.image.get_size()
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       self.delta = 3

   def move_direction(self, direction):
       if direction == "right":
           self.x = self.x + self.delta
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       if direction == "left":
           self.x = self.x - self.delta
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       if direction == "down":
           self.y = self.y + self.delta
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       if direction == "up":
           self.y = self.y - self.delta
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


