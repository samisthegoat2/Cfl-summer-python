import pygame
import sys

# Initialize Pygame
pygame.init()

# screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Example")

 #CLock for FPS
clock = pygame.time.Clock()
FPS = 60

# color definitions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#sprite class
class customSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        try:
            self.image = pygame.image.load(image_path)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        except pygame.error as e:
            print(f"Error loading image: {e}")
            #Create a placeholder surface if image fails to load
            self.image = pygame.Surface((50, 50))
            self.image.fill(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def update(self):
            # Simple movement with W,A,S,D keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.rect.x -= 5
            if keys[pygame.K_d]:
                self.rect.x += 5
            if keys[pygame.K_w]:
                self.rect.y -= 5    
            if keys[pygame.K_s]:
                self.rect.y += 5

           # Keep sprites within screen bounds 
            self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
            self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

        def draw(self, surface):
            surface.blit(self.image, self.rect)

# Create sprite group
all_sprites = pygame.sprite.Group()       

import os


script_dir = os.path.dirname(__file__)
Bowser_path = os.path.join(script_dir,"Bowser.jpg")
sprite = customSprite(Bowser_path, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
all_sprites.add(sprite)

#Main game loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        all_sprites.update()

        # Draw
        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()

pygame.quit()
sys.exit()