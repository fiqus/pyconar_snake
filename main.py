import pygame

from game_state import GameState
from init_state import InitState

pixel_size = width, height = 160, 144
screen_size = (width * 4, height * 4)


def main():
    """ Set up the game and run the main game loop """
    pygame.init()
    clock = pygame.time.Clock()

    main_surface = pygame.display.set_mode(screen_size)
    buffer = pygame.Surface((width, height))

    state = InitState(width, height)

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        state.update()
        state.draw(buffer)
        state = state.get_next_state()

        main_surface.blit(pygame.transform.scale(buffer, screen_size), (0, 0))
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()  # Once we leave the loop, close the window.


main()
