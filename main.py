import pygame

pygame.init()

import immagini
import eventi
import game_controller


def main():
    #INIZIALIZZAZIONE:

    #schermo
    risoluzione = (1280, 720)
    gameDisplay = pygame.display.set_mode(risoluzione)

    #orologio
    orologio = pygame.time.Clock()

    #dizionari graphics
    characters = immagini.load_chars()
    maps = immagini.load_maps()

    #game controller
    status = game_controller.Status(characters, maps, gameDisplay)

    #CICLO PRINCIPALE DEL GIOCO:
    while not eventi.gameOver:

        status.update()

        #aggiorno lo schermo
        pygame.display.update()
        #nebbia di guerra:
        #pygame.display.update(player.x-100,
                               #player.y-100,
                               #player_width+248,
                               #player_height+248)

        orologio.tick(eventi.game_speed)

    pygame.quit()


if __name__ == "__main__":
    main()
