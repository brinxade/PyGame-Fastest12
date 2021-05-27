from Grid import Grid
import random

class Player:
    def __init__(self, name, grid):
        self.name=name
        self.pos=[0,0]
        self.grid=grid
        self.win_point=11
        self.has_won=-1

    def roll(self):
        dice_num=random.randint(1,6)

        print("Player {} game state is {}".format(self.name, self.has_won))
        if self.has_won>-1:
            return

        if self.pos[1]+dice_num < self.win_point:
            self.pos[1]+=dice_num
            self.grid.move_player(self.pos)
        elif self.pos[1]+dice_num==self.win_point:
            self.has_won=1
            self.pos[1] += dice_num
            self.grid.move_player(self.pos)
        else:
            self.has_won=-1
            self.pos[1]=0
            self.grid.move_player(self.pos)

        print("Player {} is at {}".format(self.name, self.pos))