import pygame 
pygame.init() 
window = pygame.display.set_mode((600, 600)) 
window.fill((255, 255, 255)) 
pygame.draw.rect(window, (0, 0, 255), [100, 100, 400, 100], 0) 
pygame.draw.circle(window, (0, 255, 0), [300, 300], 170, 0) 
pygame.draw.polygon(window, (255, 0, 0), [[300, 300], [100, 400], [100, 300]]) 
pygame.display.update() 
