import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((200, 300))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (200, floor_rect.top)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < 1600:
            self.rect.x += 5

# Initialize the game
pygame.init()
pygame.display.set_caption("Iron Clash")

# Set up the screen
screen = pygame.display.set_mode((1600, 900))

#Create Floor
floor = pygame.Surface((1600, 200))
floor.fill((150, 150, 150))
floor_rect = floor.get_rect()
floor_rect.topleft = (0, 700)

# Set up the clock
clock = pygame.time.Clock()

# Create the player
player = pygame.sprite.GroupSingle(Player())

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #Draw Backround
    screen.fill((200, 200, 200))
    screen.blit(floor, floor_rect)

    # Update the player
    player.update()
    player.draw(screen)

    # Update the screen
    pygame.display.update()
    clock.tick(60)