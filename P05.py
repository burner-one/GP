import math
import pygame as py

# Initialize Pygame
py.init()
clock = py.time.Clock()

# Set up display dimensions
FrameHeight = 400
FrameWidth = 600
py.display.set_caption("Infinite Scrolling in Pygame")
screen = py.display.set_mode((FrameWidth, FrameHeight))

# Load background image
bg = py.image.load("img.jpg").convert()
scroll = 0

# Calculate number of tiles needed
tiles = math.ceil(FrameWidth / bg.get_width()) + 1

# Main loop
while True:
    clock.tick(33)  # Set frame rate
    i = 0
    
    # Draw background tiles
    while i < tiles:
        screen.blit(bg, (bg.get_width() * i + scroll, 0))
        i += 1

    # Update scroll position
    scroll -= 6
    if abs(scroll) > bg.get_width():
        scroll = 0

    # Handle events
    for event in py.event.get():
        if event.type == py.QUIT:
            quit()

    py.display.update()  # Update the display

py.quit()  # Clean up Pygame
