import pygame

class FistGuy(pygame.sprite.Sprite):
    def __init__(self, startX, portNum):
        super(FistGuy,  self).__init__()
        self.image_left = pygame.image.load("Assets/Characters/FistGuy/FistGuy.png")
        self.image_right = pygame.transform.flip(self.image_left, True, False)
        self.images = [self.image_left, self.image_right]
        self.image = self.images[1]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (startX, floor_rect.top)
        self.gravity = 0
        self.health = 500
        self.portNum = portNum
    
    def apply_gravity(self):
        if self.rect.bottom < floor_rect.top:
            self.gravity += 1
            self.rect.y += self.gravity
        if self.rect.bottom >= floor_rect.top:
            self.gravity = 0
            self.rect.bottom = floor_rect.top


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[controls["left"][self.portNum]] and not keys[controls["right"][self.portNum]] and  self.rect.left > 0:
            self.image = self.images[0]
            self.rect.x -= 8.5
        if keys[controls["right"][self.portNum]] and self.rect.right < 1600 and not keys[controls["left"][self.portNum]]:
            self.image = self.images[1]
            self.rect.x += 8.5
        if keys[controls["jump"][self.portNum]] and self.rect.bottom == floor_rect.top:
            self.rect.y -= 250
        self.apply_gravity()

class FootGuy(pygame.sprite.Sprite):
    def __init__(self, startX, portNum):
        super(FootGuy,  self).__init__()
        self.image_left = pygame.image.load("Assets/Characters/FootGuy/FootGuy.png")
        self.image_right = pygame.transform.flip(self.image_left, True, False)
        self.images = [self.image_left, self.image_right]
        self.image = self.images[1]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (startX, floor_rect.top)
        self.gravity = 0
        self.health = 500
        self.portNum = portNum
    
    def apply_gravity(self):
        if self.rect.bottom < floor_rect.top:
            self.gravity += 1
            self.rect.y += self.gravity
        if self.rect.bottom >= floor_rect.top:
            self.gravity = 0
            self.rect.bottom = floor_rect.top

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[controls["left"][self.portNum]] and not keys[controls["right"][self.portNum]] and  self.rect.left > 0:
            self.image = self.images[0]
            self.rect.x -= 10
        if keys[controls["right"][self.portNum]] and self.rect.right < 1600 and not keys[controls["left"][self.portNum]]:
            self.image = self.images[1]
            self.rect.x += 10
        if keys[controls["jump"][self.portNum]] and self.rect.bottom == floor_rect.top:
            self.rect.y -= 250
        self.apply_gravity()


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
    "left": [pygame.K_a,pygame.K_j],
    "right": [pygame.K_d, pygame.K_l],
    "jump": [pygame.K_w, pygame.K_i],
    "block": [pygame.K_q, pygame.K_o]
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
    player.update()
    player.draw(screen)
    player2.update()
    player2.draw(screen)

    # Update the health bar
    health_bar_left.update()
    health_bar_left.draw(screen)
    health_bar_right.update()
    health_bar_right.draw(screen)

    # Update the screen
    pygame.display.update()
    clock.tick(60)