import pygame
import random

# Initialize the pygame library
pygame.init()

# Set up the game window
WIDTH = 400
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the game clock
clock = pygame.time.Clock()

# Set up the snake
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = "right"

# Set up the food
food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))

# Set up the score
score = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "down":
                snake_direction = "up"
            elif event.key == pygame.K_DOWN and snake_direction != "up":
                snake_direction = "down"
            elif event.key == pygame.K_LEFT and snake_direction != "right":
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT and snake_direction != "left":
                snake_direction = "right"

    # Move the snake
    if snake_direction == "up":
        snake.insert(0, (snake[0][0], snake[0][1] - 1))
    elif snake_direction == "down":
        snake.insert(0, (snake[0][0], snake[0][1] + 1))
    elif snake_direction == "left":
        snake.insert(0, (snake[0][0] - 1, snake[0][1]))
    elif snake_direction == "right":
        snake.insert(0, (snake[0][0] + 1, snake[0][1]))

    # Remove the tail of the snake
    if len(snake) > 5:
        snake.pop()

    # Check for collisions
    if snake[0] in snake[1:] or snake[0][0] < 0 or snake[0][0] >= WIDTH or snake[0][1] < 0 or snake[0][1] >= HEIGHT:
        running = False

    # Check for food collision
    if snake[0] == food:
        food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
        score += 1

    # Draw the game objects
    screen.fill((0, 0, 0))
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], 10, 10))
    pygame.display.update()

    # Limit the frame rate
    clock.tick(10)

# Quit the game
pygame.quit()