import pygame

class GridSquare:
    def __init__(self,col,row,width=50,color=(0,255,0)):
        self.width=width
        self.row = row
        self.col = col
        self.y = self.row * self.width
        self.x = self.col * self.width
        self.color=color

    def add(self, other):
        self.row = self.row + other[1]
        self.col = self.col + other[0]
        self.y = self.row * self.width
        self.x = self.col * self.width

        return self

    def sub(self, other):
        self.row = self.row - other[1]
        self.col = self.col - other[0]
        self.y = self.row * self.width
        self.x = self.col * self.width

        return self


    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))
        for i in range(4):
            pygame.draw.rect(win, (255, 255, 255), (self.x - i/10, self.y - i/10, self.width, self.width), 1)