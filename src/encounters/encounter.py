

class Encounter():
    """docstring for Encounter"""

    def __init__(self, raid, bosses, adds):
        self.raid = raid
        self.bosses = bosses
        self.adds = adds

    def tick(self):
        raid.tick()
        for boss in self.bosses:
            boss.move()
        for add in self.adds:
            add.move()


    def render(self, display_surface):
        for boss in self.bosses:
            boss.render(display_surface)
        for add in self.adds:
            add.render(display_surface)
        for raider in self.raid:
            raider.render(display_surface)
