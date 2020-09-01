# game options/settings
TITLE = "High Schooler"
WIDTH = 1200
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'


#Game properties
MOB_FREQ = 5000

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12


# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 20),
                    (WIDTH / 2 - 50, HEIGHT * 3 / 4, 150, 30),#Beginning plat
                    (105, HEIGHT - 350, 300, 30),#Middle plat
                    (950, 170, 250, 30),#Second top
                    (790, 400, 200, 40),#Right side
                    (175, 80, 200, 30),#Top plat
                    (700,200,250,30),#Second right
                    (200, 400, 200, 30)]#Second bottom


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
#BGCOLOR = LIGHTBLUE
