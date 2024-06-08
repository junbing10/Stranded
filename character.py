import pygame

class Character:


   def __init__(self, x, y):
       self.x = x
       self.y = y
       self.image_list = ["character.png", "character idle 2.png", "character idle 3.png", "character idle 4.png", "character gethit.png"]
       self.health = 100
       self.stamina = 100
       self.image = pygame.image.load("character.png")
       self.image_size = self.image.get_size()
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       self.delta = 1

   def switch_image(self, image_number):
       self.image = pygame.image.load(self.image_list[image_number])
#        self.rescale_image(self.image)
       self.image_size = self.image.get_size()


