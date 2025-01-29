import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GROUND_HEIGHT = 300
STICKMAN_WIDTH = 50
STICKMAN_HEIGHT = 50
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
GRAVITY = 1
JUMP_STRENGTH = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stickman Running Game")

# Stickman class
class Stickman:
    def __init__(self):
        self.x = 50
        self.y = GROUND_HEIGHT - STICKMAN_HEIGHT
        self.width = STICKMAN_WIDTH
        self.height = STICKMAN_HEIGHT
        self.is_jumping = False
        self.jump_count = JUMP_STRENGTH

    def draw(self):
        # Draw head
        pygame.draw.circle(screen, BLACK, (self.x + self.width // 2, self.y + 10), 10)
        # Draw body
        pygame.draw.line(screen, BLACK, (self.x + self.width // 2, 20), (self.x + self.width // 2, self.y), 5)
        # Draw arms
        pygame.draw.line(screen, BLACK, (self.x + self.width // 2, 30), (self.x, self.y + 50), 5)
        pygame.draw.line(screen, BLACK, (self.x + self.width // 2, 30), (self.x + self.width, self.y + 50), 5)
        # Draw legs

    def jump(self):
        if self.is_jumping:
            if self.jump_count >= -JUMP_STRENGTH:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = JUMP_STRENGTH
                self.y = GROUND_HEIGHT - STICKMAN_HEIGHT

# Obstacle class
class Obstacle:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = GROUND_HEIGHT - OBSTACLE_HEIGHT
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x -= 5

# Main game loop
def main():
    clock = pygame.time.Clock()
    run = True
    stickman = Stickman()
    obstacles = []
    score = 0

    while run:
        clock.tick(30)
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not stickman.is_jumping:
            stickman.is_jumping = True

        # Update stickman
        stickman.jump()

        # Update obstacles
        if random.randint(1, 100) < 5:  # Randomly create obstacles
            obstacles.append(Obstacle())

        for obstacle in obstacles:
            obstacle.move()
            if obstacle.x < 0:
                obstacles.remove(obstacle)
                score += 1  # Increase score when obstacle is passed

        # Draw everything
        stickman.draw()
        for obstacle in obstacles:
            obstacle.draw()

        # Check for collisions
        for obstacle in obstacles:
            if (stickman.x < obstacle.x + obstacle.width and
                stickman.x + stickman.width > obstacle.x and
                stickman.y < obstacle.y + obstacle.height and
                stickman.y + stickman.height > obstacle.y):
                print("Game Over! Your score:", score)
                run = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
