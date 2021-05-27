import pygame

class Button:
    def __init__(self, x, y, width, height, label, callback=None, color=(155, 155, 155)):
        self.x = x-width/2
        self.y = y-height/2
        self.height = height
        self.label = label
        self.width = width
        self.callback = (callback)
        self.bg = color
        self.font = pygame.font.SysFont("arial", int(self.height * (3 / 4)))
        self.label = self.font.render(self.label, True, (0, 0, 0))
        self.clicked = False
        self.reset = True
        self.centre = [self.x + self.width // 2, self.y + self.height // 2]
        self.dead = False

    def draw(self, win):
        pygame.draw.rect(win, self.bg, (self.x, self.y, self.width, self.height))
        win.blit(self.label,
                 (self.centre[0] - self.label.get_width() // 2, self.y, self.label.get_width(), self.height))

    def run_callback(self):
        self.clicked = False
        self.callback()

    def check_clicked(self, mouse_pos):
        if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height and self.reset:
            self.clicked = True
            self.reset = False

    def display(self, win):
        self.draw(win)
        self.handle_input()
        if self.clicked:
            self.run_callback()

    def handle_input(self):
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            self.check_clicked([x, y])
        else:
            self.reset = True