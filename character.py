import pygame

class Character:


   def __init__(self, x, y):
       self.x = x
       self.y = y
       self.image_list = ["character.png", "character idle 2.png", "character idle 3.png", "character idle 4.png", "character gethit.png"]
       self.image_list_run = ["character run 1.png", "character run 2.png", "character run 3.png", "character run 4.png"]

       self.image_list_walk = ["character walk 1.png", "character walk 2.png", "character walk 3.png", "character walk 4.png"]

       self.health = 100
       self.stamina = 100
       self.image = pygame.image.load("character.png")
       self.image_size = self.image.get_size()
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       self.delta = 1
       self.current_image = 0
       self.current_image_run = 0
       self.current_image_walk = 0

   def switch_image(self, image_number):
       self.current_image += 1
       if self.current_image == 4:
           self.current_image = 0
       self.image = pygame.image.load(self.image_list[self.current_image])
       self.image_size = self.image.get_size()

   def switch_image_run(self, image_number):
       self.current_image_run += 1
       if self.current_image_run == 4:
           self.current_image_run = 0
       self.image = pygame.image.load(self.image_list_run[self.current_image_run])
       self.image_size = self.image.get_size()

   def switch_image_walk(self, image_number):
       self.current_image_walk += 1
       if self.current_image_walk == 4:
           self.current_image_walk = 0
       self.image = pygame.image.load(self.image_list_walk[self.current_image_walk])
       self.image_size = self.image.get_size()





