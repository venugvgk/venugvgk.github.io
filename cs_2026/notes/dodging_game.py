import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 60, 80
BALL_RADIUS = 15
PLAYER_SPEED = 7
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodging Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def main():
    # Player position
    player_x = WIDTH // 2 - PLAYER_WIDTH // 2
    player_y = HEIGHT - PLAYER_HEIGHT - 10

    # Ball properties
    balls = []
    base_speed = 3
    spawn_rate = 60  # frames between spawns
    frame_count = 0
    score = 0
    game_over = False

    running = True
    while running:
        clock.tick(60)  # 60 FPS

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    # Restart game
                    player_x = WIDTH // 2 - PLAYER_WIDTH // 2
                    balls = []
                    base_speed = 3
                    spawn_rate = 60
                    frame_count = 0
                    score = 0
                    game_over = False

        if game_over:
            # Display game over screen
            screen.fill(BLACK)
            game_over_text = font.render("GAME OVER! Press R to restart", True, WHITE)
            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 10))
            pygame.display.flip()
            continue

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_WIDTH:
            player_x += PLAYER_SPEED

        # Spawn balls
        frame_count += 1
        if frame_count >= spawn_rate:
            ball_x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
            balls.append([ball_x, -BALL_RADIUS])
            frame_count = 0

        # Increase difficulty
        base_speed += 0.002  # Gradually increase speed
        if spawn_rate > 20:
            spawn_rate -= 0.01  # Gradually increase spawn rate

        # Update ball positions
        for ball in balls[:]:
            ball[1] += base_speed

        # Check collisions
        player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
        for ball in balls[:]:
            ball_rect = pygame.Rect(ball[0] - BALL_RADIUS, ball[1] - BALL_RADIUS, 
                                   BALL_RADIUS * 2, BALL_RADIUS * 2)
            if player_rect.colliderect(ball_rect):
                game_over = True

        # Remove balls that went off screen and count score
        for ball in balls[:]:
            if ball[1] > HEIGHT + BALL_RADIUS:
                balls.remove(ball)
                score += 1

        # Draw everything
        screen.fill(BLACK)

        # Draw player (simple rectangle for now)
        pygame.draw.rect(screen, BLUE, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

        # Draw balls
        for ball in balls:
            pygame.draw.circle(screen, RED, (int(ball[0]), int(ball[1])), BALL_RADIUS)

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
