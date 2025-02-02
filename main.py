import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, startX, portNum, image_path):
        super(Player, self).__init__()
        self.image_left = pygame.image.load(image_path)
        self.image_right = pygame.transform.flip(self.image_left, True, False)
        self.images = [self.image_left, self.image_right]
        self.image = self.images[1]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (startX, floor_rect.top)
        self.gravity = 0
        self.health = 500
        self.portNum = portNum
        self.FreedomofMovement = True

    def apply_gravity(self):
        if self.rect.bottom < floor_rect.top:
            self.gravity += 1
            self.rect.y += self.gravity
        if self.rect.bottom >= floor_rect.top:
            self.gravity = 0
            self.rect.bottom = floor_rect.top

    def check_attacks(self, screen):
        keys = pygame.key.get_pressed()
        if keys[controls["medium"][self.portNum]]:
            self.perform_medium_attack(screen)

    def perform_medium_attack(self, screen):
        pass  # To be implemented by subclasses

    def update(self, screen):
        #Handle Movement
        keys = pygame.key.get_pressed()
        if keys[controls["left"][self.portNum]] and not keys[controls["right"][self.portNum]] and self.rect.left > 0 and self.FreedomofMovement:
            self.image = self.images[0]
            self.rect.x -= self.move_speed
        if keys[controls["right"][self.portNum]] and self.rect.right < 1600 and not keys[controls["left"][self.portNum]] and self.FreedomofMovement:
            self.image = self.images[1]
            self.rect.x += self.move_speed
        if keys[controls["jump"][self.portNum]] and self.rect.bottom == floor_rect.top and self.FreedomofMovement:
            self.rect.y -= 250
        self.apply_gravity()
        self.check_attacks(screen)

class MeleeAttack():
    def __init__(self, startupTime, activeTime, recoveryTime, hitbox):
        self.damage = 10
        self.startupTime = startupTime
        self.activeTime = activeTime
        self.recoveryTime = recoveryTime    
        self.hitbox = hitbox

    def activate(self, screen):
        self.beginTime = pygame.time.get_ticks()
        if self.startupTime == (pygame.time.get_ticks() - self.beginTime) :
            print("Startup")
        elif self.activeTime == (pygame.time.get_ticks() - self.beginTime):
            print("Active")
        elif self.recoveryTime == (pygame.time.get_ticks() - self.beginTime):
            print("Recovery")
        
                
    

class FistGuy(Player):
    def __init__(self, startX, portNum):
        super(FistGuy, self).__init__(startX, portNum, "Assets/Characters/FistGuy/FistGuy2.png")
        self.move_speed = 8.5
        self.Swing = MeleeAttack(500,500,500,pygame.Rect(0,0,0,0))
        

class FootGuy(Player):
    def __init__(self, startX, portNum):
        super(FootGuy, self).__init__(startX, portNum, "Assets/Characters/FootGuy/footGuy2.png")
        self.move_speed = 10

class GunGuy(Player):
    def __init__(self, startX, portNum):
        super(GunGuy, self).__init__(startX, portNum, "Assets/Characters/GunGuy/GunGuy.png")
        self.move_speed = 6

class HealthBarLeft(pygame.sprite.Sprite):
    def __init__(self):
        super(HealthBarLeft, self).__init__()
        self.image = pygame.Surface((500, 50))
        self.health = 500
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (25, 25)
    
    def update(self):
        pass

class HealthBarRight(pygame.sprite.Sprite):
    def __init__(self):
        super(HealthBarRight, self).__init__()
        self.image = pygame.Surface((500, 50))
        self.health = 500
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.topright = (1575, 25)
    
    def update(self):
        pass

# Initialize the game
pygame.init()
pygame.display.set_caption("Iron Clash")

# Set up the screen
screen = pygame.display.set_mode((1600, 900))
screen_rect = screen.get_rect()

#Font Setup
font = pygame.font.Font("Assets\Fonts\Pixeltype.ttf", 140)

#Create Text
text_surf = font.render("Iron Clash", False, (0, 0, 0))
text_rect = text_surf.get_rect()
text_rect.midtop = (screen_rect.center[0], 25)

#Create Floor
floor = pygame.Surface((1600, 200))
floor.fill((150, 150, 150))
floor_rect = floor.get_rect()
floor_rect.topleft = (0, 700)

#Create Health Bars
health_bar_left = pygame.sprite.GroupSingle(HealthBarLeft())
health_bar_right = pygame.sprite.GroupSingle(HealthBarRight())

# Set up the clock
clock = pygame.time.Clock()

#Controls
controls = {
    "left": [pygame.K_a, pygame.K_j],
    "right": [pygame.K_d, pygame.K_l],
    "jump": [pygame.K_w, pygame.K_i],
    "block": [pygame.K_q, pygame.K_o],
    "medium": [pygame.K_x, pygame.K_COMMA]
}

# Create the FistGuy
player = pygame.sprite.GroupSingle(FistGuy(200, 0))

# Create the FootGuy
player2 = pygame.sprite.GroupSingle(FootGuy(1400, 1))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #Draw Backround
    screen.fill((200, 200, 200))
    screen.blit(floor, floor_rect)

    #Draw HUD
    screen.blit(text_surf, text_rect)

    # Update the FistGuy
    player.update(screen)
    player.draw(screen)

    player2.update(screen)
    player2.draw(screen)

    # Update the health bar
    health_bar_left.update()
    health_bar_left.draw(screen)
    health_bar_right.update()
    health_bar_right.draw(screen)

    # Update the screen
    pygame.display.update()
    clock.tick(60)
