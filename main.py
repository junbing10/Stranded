import pygame
import time
import random
from character import Character
from medkit import Medkit
import math
from Background import Background
from Boss1 import Wizard
from Fireballs import fb
from mark import QMark


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Sarpanch', 90)


# set up variables for the display
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stranded")
bg_daylight = pygame.image.load("background.png")
inventory_slot = pygame.image.load("inventory.png")
no_flashlight = pygame.image.load("darkness.webp")

# varaibles
can_collect = False
inventory_full = False
start_time = time.time()
spawn_boss = False
display_boss_msg = True
reset_time = False
boss_attack = False
get_rand_num = False
got_hit = False
blit_slot1 = False
blit_slot2 = False
blit_slot3 = False
blit_slot4 = False
game_win = False
highlight_image = False
mark_count = 0
fb_last_phase = 0
fb_2nd_phase = 0
stop_draw_fb = 0

idle1 = True
idle2 = False
idle3 = False
idle4 = False

at_slot1 = False
at_slot2 = False
at_slot3 = False
at_slot4 = False



# background

def draw_inventory():
    inventory_slot_print = pygame.transform.scale(inventory_slot, (200, 200))
    screen.blit(inventory_slot_print, (350, 576))

def draw_darkness():
    darkness_print = pygame.transform.scale(no_flashlight, (900, 700))
    screen.blit(darkness_print, (0, 0))







# characters and items
c = Character(452, 287)
bg = Background(-500, -450)

#bosses
list_of_bosses = ["Wizard"]


switch_midday = False

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
qm = QMark(-500, -500)
ball = fb(400, 400)
list_of_objects = []
list_of_boss_moves = []
list_of_qmarks = []


for i in range(6):
    random_x = random.randint(5, 1400)
    random_y = random.randint(250, 1150)
    spawn_kit = Medkit(random_x, random_y)
    list_of_objects.append(spawn_kit)


for i in range(0, 15):
    random_x = random.randint(5, 1400)
    random_y = random.randint(250, 1150)
    spawn_fireballs = fb(random_x, random_y)
    list_of_boss_moves.append(spawn_fireballs)

generate_rand_num = random.randint(0, 10)
list_of_jackpot = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
list_of_jackpot.insert(generate_rand_num, "!")
print(list_of_jackpot)

for i in range (0, 10):
    random_x = random.randint(5, 1400)
    random_y = random.randint(250, 1150)
    spawn_questionmark = QMark(random_x, random_y)
    list_of_qmarks.append(spawn_questionmark)

for i in list_of_qmarks:
    for x in list_of_jackpot:
        i.lottery_num = x

run = True

idle = True
walk = False


clock = pygame.time.Clock()
frame = 0
# -------- Main Program Loop -----------
while run:

    keys = pygame.key.get_pressed()  # the keys getting pressed
    pygame.key.get_pressed()

    if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] and not sprint:
        walk = True
        idle = False
    else:
        idle = True
        walk = False


   # print(game_win)
    clock.tick(60)
    if frame % 25 == 0 and idle:
        c.switch_image(1)
    if sprint and frame % 5 == 0:
        print("running")
        idle = False
        walk = False
        c.switch_image_run(1)
    if walk and frame % 10 == 0 :
        c.switch_image_walk(1)
    if got_hit:
        c.switch_image(4)

    print(idle)

   # if frame % 30 == 0:
  #      c.switch_image(1)
  # if frame % 50 == 0:
   #     c.switch_image(2)

    keys = pygame.key.get_pressed()  # the keys getting pressed
    pygame.key.get_pressed()
    screen.blit(bg.image, bg.rect)


    x = pygame.mouse.get_pos()
    display_coord = my_font.render(str(x), True, (255, 255, 255))
    print(x)

    #time count and background switch
 #   if reset_time == False:
     #   print(time.time())
    current_time = time.time()
    current_time -= int(start_time)
    current_time = round(current_time, 2)
    total_time = "Time elapsed: " + str(current_time) + "s"
    time_display = my_font.render(total_time, True, (255, 255, 255))
    #elif reset_time:
    if reset_time:
        start_time = time.time()
        reset_time = False

    # boss
    if current_time == 2.0 and not spawn_boss: #60
        spawn_boss = True
        reset_time = True
        display_boss_msg = True

    if spawn_boss:
        if display_boss_msg:
            boss_display_message = my_font.render("What is that?", True, (255, 255, 255))
            my_font = pygame.font.SysFont('Sarpanch', 70)
            screen.blit(boss_display_message, (521, 368))
            if current_time == 4.0:
                display_boss_msg = False
        random_index = 0

        if list_of_bosses[random_index] == "Wizard":
            boss = list_of_bosses[random_index]
            wizard = Wizard(469, 388)
          #  screen.blit(wizard.image, wizard.rect)
            if current_time == 3.0:         #spawn fireballs
                boss_attack = True
                get_rand_num = True
                fb_last_phase = 5.0
                fb_2nd_phase = 4.8
                stop_draw_fb = 5.3

            if boss_attack:
                for i in list_of_boss_moves:
                    screen.blit(i.image, i.rect)

            if  current_time == fb_2nd_phase and boss_attack:
                for i in list_of_boss_moves:
                    i.image = pygame.image.load("red_circle_2ndphase.png")

            if current_time == fb_last_phase and boss_attack:
                for i in list_of_boss_moves:
                    i.image = pygame.image.load("red_circle_finalphase.png")
                    got_hit = False
                    if c.rect.colliderect(i.rect):
                        got_hit = True
                        c_health = c_health - 10
                        my_font = pygame.font.SysFont('Sarpanch', 90)
                        display_health = my_font.render((str(c_health)), True, (255, 255, 255))

            if current_time == stop_draw_fb and boss_attack:
                boss_attack = False
                reset_time = True
                print(current_time)



    my_font = pygame.font.SysFont('Sarpanch', 90) # font and size



    # stamina change
    if c_stamina > 0:
        can_sprint = True
    if c_stamina <= 0:
        can_sprint = False
    if sprint == False and c_stamina < 100:
        c_stamina = c_stamina + .3
        rounded = round(c_stamina, 0)
       # math.trunc(c_stamina)
        display_stamina = my_font.render(str(rounded), True, (255, 25, 255))
    if sprint:
        c_stamina = c_stamina - .5
        rounded = round(c_stamina, 0)
      #  math.trunc(c_stamina)
        display_stamina = my_font.render(str(rounded), True, (255, 25, 255))
    else:
        idle = True


    # item collecting
    for i in list_of_objects:


        if c.rect.colliderect(i.rect):
            can_collect = True
            my_font = pygame.font.SysFont('Sarpanch', 35)
            display_collect_msg = my_font.render((" 'E' to collect "), True, (255, 0, 0))
        else:
            can_collect = False

        keys = pygame.key.get_pressed()
        if can_collect and keys[pygame.K_e]:  # collecting item
            if len(inventory) == 4:
                inventory_full = True
                print("inventory full")
            else:
                collect_item(i)
                list_of_objects.remove(i)
                if len(inventory) == 1:
                    inventory[0].move_item(353, 602)
                    blit_slot1 = True
                if len(inventory) == 2:
                    inventory[1].move_item(400, 602)
                    blit_slot2 = True
                if len(inventory) == 3:
                    inventory[2].move_item(447, 602)
                    blit_slot3 = True
                if len(inventory) == 4:
                    inventory[3].move_item(500, 602)
                    blit_slot4 = True

    for x in list_of_qmarks:

        if c.rect.colliderect(x.rect):
            print(x.lottery_num)
            if x.lottery_num == "!":
                print("e")
                game_win = True

            mark_count = mark_count + 1

            list_of_qmarks.remove(x)

    if blit_slot1:
        screen.blit(inventory[0].image, inventory[0].rect)
    if blit_slot2:
        screen.blit(inventory[1].image, inventory[1].rect)
    if blit_slot3:
        screen.blit(inventory[2].image, inventory[2].rect)
    if blit_slot4:
        screen.blit(inventory[3].image, inventory[3].rect)

        # med kit heal
    keys = pygame.key.get_pressed()  # the keys getting pressed
    pygame.key.get_pressed()

    if keys[pygame.K_1]:
        highlight_image = True
        at_slot1 = True
        highlight_x = 358
        highlight_y = 592
    if keys[pygame.K_2]:
        highlight_image = True
        highlight_x = 410
        highlight_y = 592
    if keys[pygame.K_3]:
        highlight_image = True
        highlight_x = 458
        highlight_y = 592
    if keys[pygame.K_4]:
        highlight_image = True
        highlight_x = 508
        highlight_y = 592
    if highlight_image:
        highlight_inv = pygame.image.load("slot highlight.png")
        screen.blit(highlight_inv, (highlight_x, highlight_y))



#    if keys



    # movement
    if keys[pygame.K_d]:
        bg.move_direction("right")
        med.move_direction("right")
        for i in list_of_qmarks:
            i.move_direction("right")
        if spawn_boss:
            wizard.move_direction(" right")
        if boss_attack:
            for i in list_of_boss_moves:
                i.move_direction("right")
        for i in list_of_objects:
            i.move_direction("right")
    if keys[pygame.K_a]:
        bg.move_direction("left")
        med.move_direction("left")
        for i in list_of_qmarks:
            i.move_direction("left")
        if spawn_boss:
            wizard.move_direction("left")
        if boss_attack:
            for i in list_of_boss_moves:
                i.move_direction("left")
        for i in list_of_objects:
            i.move_direction("left")
    if keys[pygame.K_w]:
        bg.move_direction("up")
        med.move_direction("up")
        for i in list_of_qmarks:
            i.move_direction("up")
        if spawn_boss:
            wizard.move_direction("up")
        if boss_attack:
            for i in list_of_boss_moves:
                i.move_direction("up")
        for i in list_of_objects:
            i.move_direction("up")
    if keys[pygame.K_s]:
        bg.move_direction("down")
        med.move_direction("down")
        for i in list_of_qmarks:
            i.move_direction("down")
        if boss_attack:
            for i in list_of_boss_moves:
                i.move_direction("down")
        if spawn_boss:
            wizard.move_direction("down")
        for i in list_of_objects:
            i.move_direction("down")

    if keys[pygame.K_LSHIFT] and can_sprint:
        sprint = True
        bg.delta = 2
        med.delta = 2
        for t in list_of_qmarks:
            t.delta = 2
        if spawn_boss:
            wizard.delta = 2
        if boss_attack:
            for i in list_of_boss_moves:
                i.delta = 2
        for i in list_of_objects:
            i.delta = 2
    else:
        sprint = False
        bg.delta = 1
        med.delta = 1
        for t in list_of_qmarks:
            t.delta = 1
        if spawn_boss:
            wizard.delta = 5
        if boss_attack:
            for i in list_of_boss_moves:
                i.delta = 1
        for i in list_of_objects:
            i.delta = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# display everything
    screen.blit(c.image, c.rect)
    if spawn_boss:
        screen.blit(wizard.image, wizard.rect)


  #  if boss_attack:

    for i in list_of_objects:
        screen.blit(i.image, i.rect)

    for t in list_of_qmarks:
        screen.blit(t.image, t.rect)

    my_font = pygame.font.SysFont('Sarpanch', 80)
    display_mark_count = my_font.render((str(mark_count) + "/10 "), True, (255, 255, 255))
    screen.blit(display_mark_count, (755, 136))


# collecting
    if can_collect:
        if inventory_full:
           screen.blit(display_inv_full, (400, 600))
        else:
            my_font = pygame.font.SysFont('Sarpanch', 20)
            screen.blit(display_collect_msg, (400, 600))
    my_font = pygame.font.SysFont('Sarpanch', 20)
 #   screen.blit(display_coord, x)

    frame += 1
    draw_darkness()
    draw_inventory()
    screen.blit(display_health, (40, 600))
    screen.blit(display_stamina, (170, 600))
    pygame.display.update()

