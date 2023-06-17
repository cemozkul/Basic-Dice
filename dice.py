import random
import pygame

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define some dice parameters
dice_size = 200
dot_size = 40
dot_spacing = 60
dice_x1 = 100
dice_x2 = 400
dice_y = 100

# Initialize Pygame
pygame.init()

# Set up the window
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dice Roller")

# Define the draw_dice function
def draw_dice(screen, value, x, y, color, background, dot_size, dot_spacing, size):
    # Draw the outline of the dice
    pygame.draw.rect(screen, color, (x, y, size, size), 3)

    # Draw the dots for each value
    dot_positions = {
        1: [(x + size // 2, y + size // 2)],
        2: [(x + dot_spacing, y + dot_spacing), (x + size - dot_spacing, y + size - dot_spacing)],
        3: [(x + dot_spacing, y + dot_spacing), (x + size // 2, y + size // 2), (x + size - dot_spacing, y + size - dot_spacing)],
        4: [(x + dot_spacing, y + dot_spacing), (x + size - dot_spacing, y + dot_spacing), (x + dot_spacing, y + size - dot_spacing), (x + size - dot_spacing, y + size - dot_spacing)],
        5: [(x + dot_spacing, y + dot_spacing), (x + size - dot_spacing, y + dot_spacing), (x + size // 2, y + size // 2), (x + dot_spacing, y + size - dot_spacing), (x + size - dot_spacing, y + size - dot_spacing)],
        6: [(x + dot_spacing, y + dot_spacing), (x + size - dot_spacing, y + dot_spacing), (x + dot_spacing, y + size // 2), (x + size - dot_spacing, y + size // 2), (x + dot_spacing, y + size - dot_spacing), (x + size - dot_spacing, y + size - dot_spacing)]
    }
    dots = dot_positions.get(value, [])

    # Draw the dots on the dice
    for dot in dots:
        pygame.draw.circle(screen, color, dot, dot_size)

# Roll the dice
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

# Draw the initial dice
screen.fill(black)
draw_dice(screen, dice1, dice_x1, dice_y, white, black, dot_size, dot_spacing, dice_size)
draw_dice(screen, dice2, dice_x2, dice_y, white, black, dot_size, dot_spacing, dice_size)
pygame.display.update()

# Wait for user to close the window or click the mouse
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Roll both dice
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            # Redraw both dice on the screen
            screen.fill(black)
            draw_dice(screen, dice1, dice_x1, dice_y, white, black, dot_size, dot_spacing, dice_size)
            draw_dice(screen, dice2, dice_x2, dice_y, white, black, dot_size, dot_spacing, dice_size)

            # Update the display to reflect the changes
            pygame.display.update()
