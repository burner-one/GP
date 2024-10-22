# BASIC GAME DESIGNING TECHNIQUES

import pygame

# Initialize Pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))  # Fill the window with white

# Draw a blue rectangle
pygame.draw.rect(window, (0, 0, 255), [100, 100, 400, 100], 0)

# Draw a green circle
pygame.draw.circle(window, (0, 255, 0), [300, 300], 170, 0)

# Draw a red polygon
pygame.draw.polygon(window, (255, 0, 0), [[300, 300], [100, 400], [100, 300]])

# Update the display
pygame.display.update()
