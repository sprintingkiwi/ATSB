#funzione per coprire la posizione precedente del giocatore
def cover():
    gameDisplay.blit(current_map, (player.x,player.y), pygame.Rect(player.x,player.y, player_width,player_height))

#funzione di prova per trovare la posizione di partenze dei vari rect di una spritesheet dei characters
def cut(charID):
    image = graphics[charID]
    size = image.get_rect().size
    pose_D = ((0, 0), (size[0]/4, 0), (size[0]/2, 0), ((size[0]/4)*3, 0))
    pose_L = ((0, size[1]/4), (size[0]/4, size[1]/4), (size[0]/2, size[1]/4), ((size[0]/4)*3, size[1]/4))
    pose_R = ((0, size[1]/2), (size[0]/4, size[1]/2), (size[0]/2, size[1]/2), ((size[0]/4)*3, size[1]/2))
    pose_U = ((0, (size[1]/4)*3), (size[0]/4, (size[1]/4)*3), (size[0]/2, (size[1]/4)*3), ((size[0]/4)*3, (size[1]/4)*3))


#funzione per disegnare la mappa
def set_map(name):
    mappa = maps[name]
    gameDisplay.blit(mappa, (0,0))
    return mappa
