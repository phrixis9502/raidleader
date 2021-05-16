

class Raid():
    """docstring for Raid"""

    def __init__(self, raiders):
        self.raiders = raiders

    def tick(self):
        for raider in self.raiders:
            raider.tick()

    def render(self, display_surface):
        for raider in self.raiders:
            raider.render(display_surface)
