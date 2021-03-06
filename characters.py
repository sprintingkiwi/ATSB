import pygame
import strategies
import HUD


# risoluzione = (1280, 720)
# gameDisplay = pygame.display.set_mode(risoluzione)

# decorator
def blockable(func):
    def wrapper(self, *args):
        if not self.paralyzed:
            return func(self, *args)
    return wrapper


#CLASSI:

#generic class for characters
class Character(pygame.sprite.Sprite):

    def __init__(self, status, position):

        #sprite heritage
        super(Character, self).__init__()

        #initialization
        self.graphics = status.char_dict
        self.x = position[0]
        self.y = position[1]
        self.direction = "down"
        self.speed = 1
        self.paralyzed = False
        self.actionID = 1
        # self.act = False
        self.skill = None

        self.graphical_initialization()

    def graphical_initialization(self):
        self.foglio = self.graphics["char" + str(self.charID) +
                                   "_" + str(self.actionID)]
        size = self.foglio.get_rect().size
        self.width = size[0] / 4
        self.height = size[1] / 4

        self.layer = 0

        # get char's poses list
        self.pose_D = [(0, 0),
                       (size[0] / 4, 0),
                       (size[0] / 2, 0),
                       ((size[0] / 4) * 3, 0)]
        self.pose_L = [(0, size[1] / 4),
                       (size[0] / 4, size[1] / 4),
                       (size[0] / 2, size[1] / 4),
                       ((size[0] / 4) * 3, size[1] / 4)]
        self.pose_R = [(0, size[1] / 2),
                       (size[0] / 4, size[1] / 2),
                       (size[0] / 2, size[1] / 2),
                       ((size[0] / 4) * 3, size[1] / 2)]
        self.pose_U = [(0, (size[1] / 4) * 3),
                       (size[0] / 4, (size[1] / 4) * 3),
                       (size[0] / 2, (size[1] / 4) * 3),
                       ((size[0] / 4) * 3, (size[1] / 4) * 3)]

        self.actual_pose = (0, 0)

        self.p = 0
        self.frame = 0

        # create rect and image attributes of the Sprite()
        self.image = self.foglio.subsurface([self.actual_pose[0],
                                             self.actual_pose[1],
                                             self.width,
                                             self.height]).copy()
        self.rect = self.image.get_rect()

        # attributes for collisions
        self.collided = False
        #base
        self.base = pygame.sprite.Sprite()
        self.update_base()
        self.base.image = self.image.subsurface([32, 32, 32, 32]).copy()
        self.base.mask = pygame.mask.from_surface(self.image)

    def update_base(self):
        self.base.rect = pygame.Rect(self.rect.x,
                                self.rect.y + self.rect.height - (self.rect.width / 2),
                                self.rect.width,
                                self.rect.width)

        # passability
        # self.base = pygame.sprite.Sprite()
        # self.base.image = pygame.Surface([int(self.rect.width), int(self.rect.width)])
        # self.base.image.fill([0, 0, 0])
        # self.base.rect = self.base.image.get_rect()
        # self.base.rect.x = self.x
        # self.base.rect.y = self.y
        # #bit mask is empty... :(
        # self.base.mask = pygame.mask.from_surface(self.base.image)

    # roll spritesheet frames
    def slide_frame(self):

        if self.p < 60:
            self.p = self.p + 1
        else:
            self.p = 0

        if self.p < 15:
            self.frame = 0
        elif 15 < self.p < 30:
            self.frame = 1
        elif 30 < self.p < 45:
            self.frame = 2
        elif 45 < self.p < 60:
            self.frame = 3

        # print player.frame
        return self.frame

    # move character
    def move_char(self, direction):
        if direction == "down":
            self.direction = "down"
            self.y = self.y + self.speed
            self.actual_pose = self.pose_D[self.slide_frame()]
        if direction == "left":
            self.direction = "left"
            self.x = self.x - self.speed
            self.actual_pose = self.pose_L[self.slide_frame()]
        if direction == "right":
            self.direction = "right"
            self.x = self.x + self.speed
            self.actual_pose = self.pose_R[self.slide_frame()]
        if direction == "up":
            self.direction = "up"
            self.y = self.y - self.speed
            self.actual_pose = self.pose_U[self.slide_frame()]

    #set direction
    def face(self, direction):
        if self.direction == "down":
            self.actual_pose = self.pose_D[0]
        if self.direction == "left":
            self.actual_pose = self.pose_L[0]
        if self.direction == "right":
            self.actual_pose = self.pose_R[0]
        if self.direction == "up":
            self.actual_pose = self.pose_U[0]

    #skill animations
    # def action(self, status):
    #     pass
        # pass
        # print(self.name + " is doing action: " + str(skill.actionID))
        #
        # self.actionID = skill.actionID
        # self.graphical_initialization()
        #
        # if self.direction == "down":
        #     self.actual_pose = self.pose_D[self.slide_frame()]
        # if self.direction == "left":
        #     self.actual_pose = self.pose_L[self.slide_frame()]
        # if self.direction == "right":
        #     self.actual_pose = self.pose_R[self.slide_frame()]
        # if self.direction == "up":
        #     self.actual_pose = self.pose_U[self.slide_frame()]
        #
        # if self.frame == 3:
        #     self.act = False

    #what happens after collisions?
    def collisions_manager(self):
        pass

    def movement(self):
        # Sprite class methods attributes
        self.image = self.foglio.subsurface([self.actual_pose[0],
                                             self.actual_pose[1],
                                             self.width,
                                             self.height]).copy()
        self.rect = self.image.get_rect()
        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)
        #compute deep (for layered updates)
        self.layer = self.y + self.height / 2
        #base for collisions
        self.update_base()


    def update(self):
        #self.collisions_manager()
        self.movement()
        # if self.act is True:
        #     self.action(self.skill)

########

#player class
class Player(Character):

    def __init__(self, *group):
        self.charID = 1
        self.name = "Oswaldo"

        super(Player, self).__init__(*group)
        # quello che viene messo sotto super sovrascrive gli attributi del Character generico

        self.walk_down = False
        self.walk_left = False
        self.walk_right = False
        self.walk_up = False

        self.speed = 5

        self.interaction_area = pygame.Rect([0, 0, 64, 64])

        # STAT
        self.HP = 200
        self.MP = 50
        self.TP = 0
        self.ATK = 30
        self.DEF = 20
        self.MATK = 15
        self.MDEF = 10
        self.DEX = 20
        self.LUK = 3

    # make player respond to inputs
    @blockable  # decorator to paralyze the player (not for map passability stuff)
    def obey(self):
        if self.walk_down:
            self.direction = "down"
            self.actual_pose = self.pose_D[self.slide_frame()]
            self.y = self.y + self.speed
        if self.walk_left:
            self.direction = "left"
            self.actual_pose = self.pose_L[self.slide_frame()]
            self.x = self.x - self.speed
        if self.walk_right:
            self.direction = "right"
            self.actual_pose = self.pose_R[self.slide_frame()]
            self.x = self.x + self.speed
        if self.walk_up:
            self.direction = "up"
            self.actual_pose = self.pose_U[self.slide_frame()]
            self.y = self.y - self.speed

    def update_interaction_area(self):
        if self.direction == "down":
            x = self.x
            y = self.y + 32
        if self.direction == "right":
            x = self.x + 32
            y = self.y
        if self.direction == "left":
            x = self.x - 32
            y = self.y
        if self.direction == "up":
            x = self.x
            y = self.y - 32
        self.interaction_area.centerx = x
        self.interaction_area.centery = y

    #UPDATE
    def update(self, *group):
        super(Player, self).update(*group)
        self.update_interaction_area()
        self.obey()


class NPC(Character):
    def __init__(self, ID, name, *group):

        self.charID = ID
        self.name = name
        self.talk = "Hi, how are you?"

        super(NPC, self).__init__(*group)

    def act(self, status):
        if hasattr(self, 'action'):
            self.action()
        else:
            status.HUD.add(HUD.TextBox(status, self.talk))

    def update(self, *group):
        super(NPC, self).update(*group)
        strategies.suegiu(self, 100, 500)
