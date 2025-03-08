import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 50, 200)   # Giants
RED = (200, 50, 50)    # Cannons
GREEN = (50, 200, 50)  # Health bars
BLACK = (0, 0, 0)      # Cannonball color


class Giant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1.5
        self.attack_range = 40
        self.damage = 10
        self.health = 100
        self.attack_timer = 0

    def move_towards(self, target, other_giants):
        """Move towards the closest cannon while avoiding stacking"""
        if target:
            dx, dy = target.x - self.x, target.y - self.y
            distance = math.hypot(dx, dy)

            if distance > self.attack_range:
                self.x += (dx / distance) * self.speed
                self.y += (dy / distance) * self.speed

        # Avoid stacking with other giants
        for other in other_giants:
            if other == self:
                continue
            dist_to_other = math.hypot(self.x - other.x, self.y - other.y)
            if dist_to_other < 30:  # Minimum separation distance
                self.x += (self.x - other.x) * 0.05
                self.y += (self.y - other.y) * 0.05

    def attack(self, cannons):
        """Attack cannons when in range"""
        if self.attack_timer <= 0:
            for cannon in cannons:
                distance = math.hypot(self.x - cannon.x, self.y - cannon.y)
                if distance <= self.attack_range:
                    cannon.health -= self.damage
                    print(f"Giant attacked! Cannon health: {cannon.health}")
                    self.attack_timer = 60  # Cooldown (1 sec)

    def update(self):
        """Reduce attack cooldown"""
        if self.attack_timer > 0:
            self.attack_timer -= 1

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), 15)
        pygame.draw.rect(screen, GREEN, (self.x - 15, self.y - 20, max(0, self.health), 5))  # Health bar


class Cannon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 50
        self.attack_timer = 0
        self.damage = 15
        self.attack_speed = 90  # Shoots every 1.5 seconds

    def attack(self, giants, cannonballs):
        """Shoot at nearest giant"""
        if self.attack_timer <= 0 and giants:
            nearest_giant = min(giants, key=lambda g: math.hypot(self.x - g.x, self.y - g.y))
            distance = math.hypot(self.x - nearest_giant.x, self.y - nearest_giant.y)
            if distance <= 200:  # Cannon range
                cannonballs.append(Cannonball(self.x, self.y, nearest_giant.x, nearest_giant.y))  # Fire a cannonball
                self.attack_timer = self.attack_speed  # Reset cooldown

    def update(self):
        """Reduce attack cooldown"""
        if self.attack_timer > 0:
            self.attack_timer -= 1

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x - 15, self.y - 15, 30, 30))  # Cannon shape
        pygame.draw.rect(screen, GREEN, (self.x - 15, self.y - 25, max(0, self.health), 5))  # Health bar


class Cannonball:
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y
        self.speed = 4
        self.damage = 15

        # Calculate direction
        dx, dy = target_x - x, target_y - y
        distance = math.hypot(dx, dy)
        self.vel_x = (dx / distance) * self.speed
        self.vel_y = (dy / distance) * self.speed

    def move(self):
        """Move the cannonball forward"""
        self.x += self.vel_x
        self.y += self.vel_y

    def check_collision(self, giants):
        """Check if the cannonball hits a giant"""
        for giant in giants:
            if math.hypot(self.x - giant.x, self.y - giant.y) < 15:
                giant.health -= self.damage
                print(f"Cannonball hit! Giant health: {giant.health}")
                return True  # Remove cannonball after hit
        return False

    def draw(self, screen):
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), 5)  # Cannonball shape


# Create Giants and Cannons
giants = [Giant(random.randint(50, 150), random.randint(200, 400)) for _ in range(4)]
cannons = [Cannon(random.randint(500, 750), random.randint(200, 400)) for _ in range(4)]
cannonballs = []

# Game loop
# Game loop
running = True
game_over = False
winner = None  # "Giants" or "Cannons"

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Update and draw Giants
        for giant in giants:
            if cannons:
                nearest_cannon = min(cannons, key=lambda c: math.hypot(giant.x - c.x, giant.y - c.y))
                giant.move_towards(nearest_cannon, giants)
                giant.attack(cannons)
            
            giant.update()
            giant.draw(screen)

        # Update and draw Cannons
        for cannon in cannons:
            cannon.attack(giants, cannonballs)
            cannon.update()
            cannon.draw(screen)

        # Update and draw Cannonballs
        for cannonball in cannonballs[:]:  # Copy list to safely remove elements
            cannonball.move()
            if cannonball.check_collision(giants):
                cannonballs.remove(cannonball)
            else:
                cannonball.draw(screen)

        # Remove dead units
        giants = [g for g in giants if g.health > 0]
        cannons = [c for c in cannons if c.health > 0]

        # **Check for Win/Loss Conditions**
        if not cannons:  # Giants win
            game_over = True
            winner = "Giants"
        elif not giants:  # Cannons win
            game_over = True
            winner = "Cannons"
    
    else:  # **Game Over Screen**
        font = pygame.font.Font(None, 60)
        text = font.render(f"{winner} Win!", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()