import pygame

pygame.init()


import events
import game_controller


def main():
    #INIZIALIZZAZIONE:

    #orologio
    orologio = pygame.time.Clock()

    #game controller
    status = game_controller.Status()
    status.load_area()

    #CICLO PRINCIPALE DEL GIOCO:
    while not events.gameOver:

        status.update()

        #aggiorno lo schermo
        pygame.display.update()
        #nebbia di guerra:
        #pygame.display.update(player.x-100,
                               #player.y-100,
                               #player_width+248,
                               #player_height+248)

        orologio.tick(events.game_speed)

    pygame.quit()


if __name__ == "__main__":
    main()
