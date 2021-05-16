import pygame, sys
from units import inquisitor
from encounters import raid, encounter


def create_raiding_party():
    raiders = []

    for i in range(5):
        raiders.append(inquisitor.Inquisitor(( i * 20 ) + 20 , 20)))

    raiding_party = raid.Raid(raiders)

    return raiding_party


def create_encounter():
    return


def main():
    pygame.init()
    FPS = 30

    GameClock = pygame.time.Clock()

    DisplaySurface = pygame.display \
                        .set_mode((600, \
                                   600))
    pygame.display.set_caption("Welcome to Hell")

    raiding_party = create_raiding_party()

    pause = False
    selected = []

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = not pause

        # Update Game State
        if not pause:
            solo.move()

        #Render
        DisplaySurface.fill((255,255,255))
        solo.render(DisplaySurface)

        pygame.display.update()
        GameClock.tick(FPS)

main()
