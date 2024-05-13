import pygame
import time
import random
from character import Character
from medkit import Medkit
import math

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Sarpanch', 90)


# set up variables for the display
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stranded")
bg_daylight = pygame.image.load("background.daylight.jpg")
#bg_afternoon = pygame.image.load("background.afternoon.jpg")
#bg_night = pygame.image.load("background.night.jpg")

# varaibles
can_collect = False

# background
def draw_background_daylight():
    daylight_bg_print = pygame.transform.scale(bg_daylight, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(daylight_bg_print, (0, 0))

# characters and items
c = Character(80, 60)

# inventory and collecting
def collect_item(item):
     c.inventory.append(item)


# stamina
c_stamina = 100
stamina_full = True
stamina_0 = False
display_stamina = my_font.render(str(c_stamina), True, (255,25,255))

# health
c_health = 100
display_health = my_font.render((str(c_health)), True, (255,255,255))

# sprinting
sprint = False
can_sprint = True

# medkits

#for i in range(6):
med = Medkit(0, 0)
list_of_medkits = []
#spawn_kit = Medkit(random_x, random_y)

for i in range(6):
    random_x = random.randint(0, 900)
    random_y = random.randint(0, 700)
    print(random_x)
    spawn_kit = Medkit(random_x, random_y)
    list_of_medkits.append(spawn_kit)




run = True
# -------- Main Program Loop -----------
while run:

    my_font = pygame.font.SysFont('Sarpanch', 90) # font and size

    # draw background
    draw_background_daylight()

    # stamina change
    if c_stamina > 0:
        can_sprint = True
    if c_stamina <= 0:
        can_sprint = False
    if sprint == False and c_stamina < 100:
        c_stamina = c_stamina + .05
        math.trunc(c_stamina)
        display_stamina = my_font.render(str(c_stamina), True, (255, 25, 255))
    if sprint:
        c_stamina = c_stamina - .1
        math.trunc(c_stamina)
        display_stamina = my_font.render(str(c_stamina), True, (255, 25, 255))


    keys = pygame.key.get_pressed()             # the keys getting pressed
    pygame.key.get_pressed()

    # item collecting
    if c.rect.colliderect(med.rect):
        can_collect = True
        my_font = pygame.font.SysFont('Sarpanch', 35)
        display_collect_msg = my_font.render((" 'E' to collect "), True, (255, 255, 255))
    else:
        can_collect = False


  #  if can_collect == True and keys[pygame.K_e]:        # collecting item

    keys = pygame.key.get_pressed()  # the keys getting pressed
    pygame.key.get_pressed()

    # movement
    if keys[pygame.K_d]:
        c.move_direction("right")
    if keys[pygame.K_a]:
        c.move_direction("left")
    if keys[pygame.K_w]:
        c.move_direction("up")
    if keys[pygame.K_s]:
        c.move_direction("down")

    if keys[pygame.K_LSHIFT] and can_sprint:
        sprint = True
        c.delta = .2
    else:
        sprint = False
        c.delta = .1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# display everything
    screen.blit(c.image, c.rect)
    for i
    screen.blit(med.image, med.rect)
    screen.blit(display_health, (40, 600))
    screen.blit(display_stamina, (170, 600))

# collecting
    if can_collect:
        my_font = pygame.font.SysFont('Sarpanch', 20)
        screen.blit(display_collect_msg, (400, 600))
    pygame.display.update()
