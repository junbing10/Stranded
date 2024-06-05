import pygame

class Wizard:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("wizardboss.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 1

    def move_direction(self, direction):
        if direction == "left":
            self.x = self.x + self.delta
            print("moving left")
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "right":
            self.x = self.x - self.delta
            print("moving right")
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "up":
            self.y = self.y + self.delta
            print("moving up")
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "down":
            self.y = self.y - self.delta
            print("moving down")
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
