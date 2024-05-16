'''
contexte : code d'un petit mario capable de sauter sur des blocs
'''

# ---- importation des librairies ----

import pygame

# ---- définition des fonctions ----

class jeu :

    def __init__(self, player, object, window,x,y):
        self.frequenceAffichage = 0
        self.frequenceCalcul = 0
        self.player = player(x,y)
        self.object = object()
        self.window = window()
 
class player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.a = 0
        self.v = 0

    def setPosition(self,a,b):
        self.x = a
        self.y = b 

class object:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = 0
        self.v = 0


    def setPosition(self,a,b):
        self.x = a
        self.y = b 

class window :

    def __init__(self):
        self.taille_x = 1280
        self.taille_y = 720

    def refreshDisplay():
        pass
    def calculNewPosition(old_joueur,joueur):
        pass







# ---- MAIN ----

game = jeu(player,object,window,100,100)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((game.window.taille_x, game.window.taille_y))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()