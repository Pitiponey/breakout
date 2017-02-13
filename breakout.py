# coding: utf8
from ball import *
from racket import *
from collision import *
from brick import *


# Gère les événements
def event_handler(events):
    # Pour chaque événement dans la liste des événements
    for event in events:
        # Si on quitte ou que l'on appuie sur esc, alors on quitte
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return True

        # Au mouvement de la souris, on récupère les positions x et y
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            racket.set_x(x), racket.set_y(y)


# Fonction main de l'application
if __name__ == "__main__":
    # On initialise une instance de Pygame
    pygame.init()
    # On définit la taille de l'écran
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Booléen qui gère le fermeture de l'application
    to_quit = False
    # On initialise l'horloge afin de gérer les FPS
    clock = pygame.time.Clock()
    # On crée une instance de balle Ball(Écran, Couleur de la balle, position x,
    # position y, taille de la balle, remplissage)
    ball   = Ball(screen, WHITE, 255, 100, RADIUS, FILL)
    # Racket (Écran, Couleur de la raquette, lageur de la raquette, hauteur de la raquette)
    racket = Racket(screen, RACKET_COLOR, SQUARE_WIDTH, SQUARE_HEIGHT)
    # Création d'une instance Brick avec l'écran et la couleur, la gestion des briques se fait plus tard
    brick = Brick(screen, BRICK_COLOR)
    brick.create_bricks(NUMBER_BRICKS, NUMBER_LINE)

    # Gère les colisions
    collision = Collision(ball.get_x(), ball.get_y(), ball.get_radius(),
                          racket.get_x(), racket.get_y(), racket.get_width(), racket.get_height())

    # Tant que l'on ne quitte pas
    while not to_quit:
        # Récupère si la touche escape a été appuyée ou si l'utilisateur a fermé le programme
        to_quit = event_handler(pygame.event.get())
        # Gère les collisions avec le mur avant d'incrémenter
        collision.collision_ball_wall(ball.get_x(), ball.get_y())
        collision.update(ball.get_x(), ball.get_y(), racket.pos_x, racket.pos_y)

        # Rempli l'écran en noir
        screen.fill(BLACK)
        # Dessine la ligne blanche pour délimiter le terrain de jeu, la balle, et la raquette
        pygame.draw.line(screen, WHITE, (0, PLAY_ZONE_CALC), (SCREEN_WIDTH, PLAY_ZONE_CALC), LINE_HEIGHT)
        ball.draw()
        racket.draw()
        brick.draw()

        # Affiche les nouveaux éléments à l'écran
        pygame.display.flip()
        clock.tick(NUMBER_FPS)
