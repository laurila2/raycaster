import pygame
import colours

pygame.init()

# Window dimensions
WIDTH = 1280
HEIGHT = 800

# Screen initialization
background_colour = colours.GRAY
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('raycaster_game')
screen.fill(background_colour)

# Variable to keep game loop running
running = True


def draw_dot_center():
    pygame.draw.rect(screen, colours.RED, pygame.Rect(WIDTH / 2, HEIGHT / 2, 10, 10))


def wall(start_pos, end_pos, colour=colours.GREEN):
    """
    :param colour:
    :param start_pos: tuple
    :param end_pos: tuple
    """
    pygame.draw.line(screen, colour, start_pos, end_pos, width=5)


if __name__ == '__main__':
    while running:
        draw_dot_center()

        # Screen 1280x800
        wall((700, 250), (500, 250))
        wall((700, 700), (500, 500), colours.BLUE)
        wall((1100, 400), (800, 500), colours.PURPLE)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
