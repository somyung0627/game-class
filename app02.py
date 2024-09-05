import pygame


pygame.init()

pygame.display.set_caption("Flappy Bird")

screen_size = (288, 512)
screen = pygame.display.set_mode(screen_size)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    pygame.display.flip()

pygame.quit()
