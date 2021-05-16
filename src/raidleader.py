import pygame, sys
from units import inquisitor, boss
from encounters import raid, encounter
from config import colors


def create_raiding_party():
    raiders = []

    for i in range(5):
        raiders.append(inquisitor.Inquisitor(( i * 20 ) + 20 , 20))

    raiding_party = raid.Raid(raiders)

    return raiding_party


def create_encounter():
    raiding_party = create_raiding_party()
    boss_list = [boss.Boss(300, 300)]
    return encounter.Encounter(raiding_party, boss_list, [])



def main():
    pygame.init()
    FPS = 30

    GameClock = pygame.time.Clock()

    DisplaySurface = pygame.display \
                        .set_mode((600, \
                                   600))
    pygame.display.set_caption("Welcome to Hell")

    current_encounter = create_encounter()

    pause = False
    multi_select = False
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
                    # if event.pos collides with any raider sprite
                        #add to selected
                    # else this v
                    for raider in selected:
                        raider.set_destination(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = not pause
                if (event.key == pygame.K_RSHIFT) | (event.key == pygame.K_RSHIFT):
                    multi_select = True
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_RSHIFT) | (event.key == pygame.K_RSHIFT):
                    multi_select = False

        # Update Game State
        if not pause:
            current_encounter.tick()

        #Render
        DisplaySurface.fill(colors.Black)
        current_encounter.render(DisplaySurface)

        for item in selected:
            item.render_highlights()

        pygame.display.update()
        GameClock.tick(FPS)

main()
