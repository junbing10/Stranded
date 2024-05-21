import pygame
import time
import random
from character import Character
from medkit import Medkit
import math
from Background import Background

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
inventory_slot = pygame.image.load("inventory.png")
#character_print = pygame.image.load("character.png")
#bg_afternoon = pygame.image.load("background.afternoon.jpg")
#bg_night = pygame.image.load("background.night.jpg")

# varaibles
can_collect = False
inventory_full = False

# background

#def draw_character():
#    character_display = pygame.transform.scale(character_print, (40, 80))
#    screen.blit(character_display, (400, 320))
def draw_background_daylight():
    daylight_bg_print = pygame.transform.scale(bg_daylight, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(daylight_bg_print, (0, 0))

def draw_inventory():
    inventory_slot_print = pygame.transform.scale(inventory_slot, (200, 200))
    screen.blit(inventory_slot_print, (350, 5))

def draw_item_on_slot(item, x, y):
    slot1 = pygame.transform.scale(item, item.image_size)
    screen.blit(slot1, x, y)


#def draw_item_in_slots():


# characters and items
c = Character(443, 353)
bg = Background(-500, -450)

# inventory and collecting
inventory = []
display_collect_msg = my_font.render((" 'E' to collect "), True, (255, 0, 0))
display_inv_full = my_font.render((" Inventory full "), True, (255, 0, 0))
def collect_item(item):
    inventory.append(item)


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


med = Medkit(400, 400)
list_of_objects = []


for i in range(6):
    random_x = random.randint(5, 1500)
    random_y = random.randint(250, 1150)
    spawn_kit = Medkit(random_x, random_y)
    list_of_objects.append(spawn_kit)
    print(list_of_objects)




run = True
# -------- Main Program Loop -----------
while run:
    screen.blit(bg.image, bg.rect)

    x = pygame.mouse.get_pos()
    display_coord = my_font.render(str(x), True, (255, 255, 255))
    print(x)


    my_font = pygame.font.SysFont('Sarpanch', 90) # font and size

    # draw background
   # draw_background_daylight()
    draw_inventory()
#    draw_character()

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
    for i in list_of_objects:
        if c.rect.colliderect(i.rect):
            print("e")
            can_collect = True
            my_font = pygame.font.SysFont('Sarpanch', 35)
            display_collect_msg = my_font.render((" 'E' to collect "), True, (255, 0, 0))
        else:
            can_collect = False


        if can_collect == True and keys[pygame.K_e]:        # collecting item
            if len(inventory) == 4:
                inventory_full = True
                print("inventory full")
            else:
                collect_item(i)
                list_of_objects.remove(i)
                draw_item_on_slot(i, 468, 80)
                print(inventory)

 #               for i in range(5):
#                    amount_of_items = i
##                    if len(inventory) == i:
  #                      screen.blit()

                if len(inventory) == 0:
                    inventory_slot_numbers = 0
                if len(inventory) == 1:
                    inventory_slot_numbers = 1
                if len(inventory) == 2:
                    inventory_slot_numbers = 2
                if len(inventory) == 3:
                    inventory_slot_numbers = 3
                if len(inventory) == 4:
                    inventory_slot_numbers = 4


        # med kit heal


    keys = pygame.key.get_pressed()  # the keys getting pressed
    pygame.key.get_pressed()

    # movement
    if keys[pygame.K_d]:
        bg.move_direction("right")
        med.move_direction("right")
        for i in list_of_objects:
            i.move_direction("right")
    if keys[pygame.K_a]:
        bg.move_direction("left")
        med.move_direction("left")
        for i in list_of_objects:
            i.move_direction("left")
    if keys[pygame.K_w]:
        bg.move_direction("up")
        med.move_direction("up")
        for i in list_of_objects:
            i.move_direction("up")
    if keys[pygame.K_s]:
        bg.move_direction("down")
        med.move_direction("down")
        for i in list_of_objects:
            i.move_direction("down")

    if keys[pygame.K_LSHIFT] and can_sprint:
        sprint = True
        bg.delta = 2
        med.delta = 2
        for i in list_of_objects:
            i.delta = 2
    else:
        sprint = False
        bg.delta = 1
        med.delta = 1
        for i in list_of_objects:
            i.delta = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# display everything
    screen.blit(c.image, c.rect)
    screen.blit(med.image, med.rect)

    screen.blit(med.image, med.rect)
    for i in list_of_objects:
        screen.blit(i.image, i.rect)
    screen.blit(display_health, (40, 600))
    screen.blit(display_stamina, (170, 600))


# collecting
    if can_collect:
        print("t")
        if inventory_full:
           screen.blit(display_inv_full, (400, 600))
        else:
            my_font = pygame.font.SysFont('Sarpanch', 20)
            screen.blit(display_collect_msg, (400, 600))
    my_font = pygame.font.SysFont('Sarpanch', 20)
 #   screen.blit(display_coord, x)


    pygame.display.update()

