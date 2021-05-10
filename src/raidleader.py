import pygame, sys
from characters import raider, unit

def main():
    pygame.init()
    FPS = 30

    GameClock = pygame.time.Clock()

    DisplaySurface = pygame.display \
                        .set_mode((600, \
                                   600))
    pygame.display.set_caption("Welcome to Hell")

    solo = raider.Raider()

    while True:
        # Cycles through all events occuring
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Handle Input
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    solo.set_destination(event.pos)

        #Tick Code
        solo.move()
        #Render
        DisplaySurface.fill((255,255,255))
        solo.render(DisplaySurface)

        pygame.display.update()
        GameClock.tick(FPS)

main()
