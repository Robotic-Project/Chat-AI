import pygame

pygame.init()
size = [1080, 800]
screen= pygame.display.set_mode(size ,pygame.NOFRAME)
  
pygame.display.set_caption("BMO")

background = pygame.image.load("C:/Users/maydr/Documents/BMO/Face-Detection/source/unknown.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    pygame.display.update()

pygame.quit()