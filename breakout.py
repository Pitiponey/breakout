from ball import *
from racket import *


def event_handler(events):
    for event in events:
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return True

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            racket.set_x(x), racket.set_y(y)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    done = False

    clock = pygame.time.Clock()
    ball   = Ball(screen, WHITE, 255, 495, 10, 0)
    racket = Racket(screen, RACKET_COLOR, SQUARE_WIDTH, SQUARE_HEIGHT)

    while not done:
        done = event_handler(pygame.event.get())

        screen.fill((0, 0, 0))

        pygame.draw.line(screen, (255, 255, 255), (0, PLAY_ZONE_CALC), (SCREEN_WIDTH, PLAY_ZONE_CALC), LINE_HEIGHT)
        ball.draw()
        racket.draw()

        pygame.display.flip()
        clock.tick(60)
