import pygame
import skills

gameOver = False

game_speed = 60


#events control
def manage_events(player):
    global gameOver, game_speed
    for event in pygame.event.get():

        #close game window
        if event.type == pygame.QUIT:
            gameOver = True

        #PLAYER MOVEMENT
        #keydown
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.walk_right = True
            if event.key == pygame.K_LEFT:
                player.walk_left = True
            if event.key == pygame.K_UP:
                player.walk_up = True
            if event.key == pygame.K_DOWN:
                player.walk_down = True
        #keyup
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.walk_right = False
                player.actual_pose = player.pose_R[0]
            if event.key == pygame.K_LEFT:
                player.walk_left = False
                player.actual_pose = player.pose_L[0]
            if event.key == pygame.K_UP:
                player.walk_up = False
                player.actual_pose = player.pose_U[0]
            if event.key == pygame.K_DOWN:
                player.walk_down = False
                player.actual_pose = player.pose_D[0]

        #ACTIONS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.act = True
                player.skill = skills.Explosion()
            if event.key == pygame.K_s:
                player.action(skills.Empty())
            if event.key == pygame.K_d:
                player.action(skills.Attack())

        #game speed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                game_speed = 30
            if event.key == pygame.K_2:
                game_speed = 60
            if event.key == pygame.K_3:
                game_speed = 120
