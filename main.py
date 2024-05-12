import pygame
from character import Character

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)


# set up variables for the display
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stranded")
bg_daylight = pygame.image.load("background.daylight.jpg")
#bg_afternoon = pygame.image.load("background.afternoon.jpg")
#bg_night = pygame.image.load("background.night.jpg")

# background
def draw_background_daylight():
    daylight_bg_print = pygame.transform.scale(bg_daylight, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(daylight_bg_print, (0, 0))

# characters
c = Character(80, 60)


run = True
# -------- Main Program Loop -----------
while run:

    # draw background
    draw_background_daylight()

    # movement
    keys = pygame.key.get_pressed()  # checking pressed keys
    pygame.key.get_pressed()
    if keys[pygame.K_d]:
        c.move_direction("right")
    if keys[pygame.K_a]:
        c.move_direction("left")
    if keys[pygame.K_w]:
        c.move_direction("up")
    if keys[pygame.K_s]:
        c.move_direction("down")

    if keys[pygame.K_LSHIFT]:
        c.delta = .2
    else:
        c.delta =.1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(c.image, c.rect)
    pygame.display.update()
