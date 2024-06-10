import pygame

class QMark:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["question mark up.png", "question mark down.png"]
        self.image = pygame.image.load("question mark up.png")
        self.image_size = self.image.get_size()
        self.lottery_num = "#"
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 1

    def move_direction(self, direction):
        if direction == "left":
            self.x = self.x + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "right":
            self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "up":
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "down":
            self.y = self.y - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def switch_image(self, image_number):
        self.image = pygame.image.load(self.image_list[image_number])
#       self.rescale_image(self.image)
        self.image_size = self.image.get_size()