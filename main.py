import pygame

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


run = True
# -------- Main Program Loop -----------
while run:

    # draw background
    draw_background_daylight()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
