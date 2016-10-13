import pygame
import game_controller
import subprocess

pygame.init()

def main():
    #INIZIALIZZAZIONE:

    #orologio
    orologio = pygame.time.Clock()

    #game controller
    status = game_controller.Status()

    #CICLO PRINCIPALE DEL GIOCO:
    while not status.GAMEOVER:

        status.update()

        #aggiorno lo schermo
        pygame.display.update()
        #nebbia di guerra:
        #pygame.display.update(player.x-100,
                               #player.y-100,
                               #player_width+248,
                               #player_height+248)

        orologio.tick(status.game_speed)

    pygame.quit()
    try:
        subprocess.Popen(["python", "/home/pi/PYGB_OS/pygbOS.py"], cwd="/home/pi/")
    except:
        pass


if __name__ == "__main__":
    main()
