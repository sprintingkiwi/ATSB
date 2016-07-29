

#move down and up
def suegiu(nemico, top, bottom):
    if top < nemico.y < bottom and nemico.direction == "down":
        nemico.move_char("down")
    if nemico.y > (bottom-1):
        nemico.move_char("up")
    if top < nemico.y < bottom and nemico.direction == "up":
        nemico.move_char("up")
    if nemico.y < (top+1):
        nemico.move_char("down")
