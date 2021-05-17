

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

    def click(self, position):
        selected = []
        for raider in self.raiders:
            if raider.check_distance(position):
                selected.append(raider)
        return selected
