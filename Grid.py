from GridSquare import GridSquare
from Label import Label
import globals

class Grid:
    def __init__(self, label_text, x, y, width, height, size=50):
        self.label=Label(x*size - 40, y * size + 5, label_text, 30)
        self.grid_squares=[]
        self.player_at=[0,0]
        self.blank_color=(0,255,0)
        self.player_color=(255,0,0)
        self.x_draw_offset=1

        for i in range(0,height):
            self.grid_squares.append([])
            for j in range(self.x_draw_offset,width+self.x_draw_offset):
                self.grid_squares[-1].append(GridSquare(x+j, y+i, size, self.blank_color))

        self.grid_squares[self.player_at[0]][self.player_at[1]].color=(255,0,0)

    def remove_player(self):
        self.grid_squares[self.player_at[0]][self.player_at[1]].color = self.blank_color

    def move_player(self, new_pos):
        self.grid_squares[self.player_at[0]][self.player_at[1]].color=self.blank_color
        self.grid_squares[new_pos[0]][new_pos[1]].color = self.player_color
        self.player_at[0], self.player_at[1]=new_pos[0], new_pos[1]

    def render(self, win):
        for i in self.grid_squares:
            for j in i:
                j.draw(win)

        self.label.draw(win)
