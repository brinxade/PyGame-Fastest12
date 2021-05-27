import pygame

class Label:
    def __init__(self, x, y, text, size, color=(255,255,255)):
        self.x=x
        self.y=y
        self.text=text
        self.size=size
        self.font = pygame.font.SysFont("arial", size)
        self.label=self.font.render(text, True, color)

        label_rect=self.label.get_rect()
        self.center=(label_rect[0]/2, label_rect[1]/2)

    def set_text(self, text, color=(255,255,255)):
        self.label=self.font.render(text, True, color)

    def draw(self, win):
        win.blit(self.label,
                 (self.x+(self.center[0] - self.label.get_width() // 2), self.y, self.label.get_width(),
                   self.label.get_height()))