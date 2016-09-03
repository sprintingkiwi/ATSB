import pygame

#events control
def manage_events(status):
    for event in pygame.event.get():

        #close game window
        if event.type == pygame.QUIT:
            status.GAMEOVER = True

        # KEYDOWN
        if event.type == pygame.KEYDOWN:
            # PLAYER MOVEMENT
            if event.key == pygame.K_RIGHT:
                status.player.walk_right = True
            if event.key == pygame.K_LEFT:
                status.player.walk_left = True
            if event.key == pygame.K_UP:
                status.player.walk_up = True
            if event.key == pygame.K_DOWN:
                status.player.walk_down = True
            #BUTTONS A e B
            if event.key == pygame.K_z:
                status.buttonA = True
                print("A")
            if event.key == pygame.K_x:
                status.buttonB = True
                print("B")

        # KEYUP
        if event.type == pygame.KEYUP:
            # PLAYER MOVEMENT
            if event.key == pygame.K_RIGHT:
                status.player.walk_right = False
                status.player.actual_pose = status.player.pose_R[0]
            if event.key == pygame.K_LEFT:
                status.player.walk_left = False
                status.player.actual_pose = status.player.pose_L[0]
            if event.key == pygame.K_UP:
                status.player.walk_up = False
                status.player.actual_pose = status.player.pose_U[0]
            if event.key == pygame.K_DOWN:
                status.player.walk_down = False
                status.player.actual_pose = status.player.pose_D[0]
            # BUTTONS A e B
            if event.key == pygame.K_z:
                status.buttonA = False

        #ACTIONS
            # if event.key == pygame.K_a:
            #     status.player.act = True
            #     status.player.skill = skills.Explosion()
            # if event.key == pygame.K_s:
            #     status.player.action(skills.Empty())
            # if event.key == pygame.K_d:
            #     status.player.action(skills.Attack())

        #game speed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                status.game_speed = 30
            if event.key == pygame.K_2:
                status.game_speed = 60
            if event.key == pygame.K_3:
                status.game_speed = 120
