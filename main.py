import pygame
import events
import globals
from Button import Button
from Grid import Grid
from GridSquare import GridSquare
from Label import Label
from Player import Player

if __name__=="__main__":
    pygame.init()
    pygame.display.set_caption("Fastest to the 12")
    img_splash=pygame.transform.scale(pygame.image.load("dice.png"), (400,400))
    win = pygame.display.set_mode((globals.window_width, globals.window_height))

    # UI and Logic
    dice_roll_ready=True
    players, labels,buttons=dict(), dict(), dict()
    players["A"]=Player("A", Grid("Player A", 4, 5, 12, 1))
    players["B"]=Player("B", Grid("Player B", 4, 7, 12, 1))
    labels["player_turn"] = Label(globals.window_width / 2, 50, "Its Player A's Turn", 40)
    labels["player_turn_control"]=Label(globals.window_width / 2, 150, "Press 'R' to Roll Dice", 25)
    labels["game_status"] = Label(globals.window_width / 2,470, "", 40, (255,0,0))
    buttons["start"]=Button(globals.window_width/2, (globals.window_height/2)-50, 270, 60, "Start Game",
                            events.start_game)
    buttons["quit"]=Button((globals.window_width/2), (globals.window_height/2)+50, 270, 60, "Quit Game",
                           events.quit_game)

    current_player=players["A"]

    while (globals.run):
        win.fill((0,0,0))
        events = pygame.event.get()

        for player in players.values():
            if player.has_won==1:
                globals.game_over=True
                labels["player_turn_control"].set_text("Relaunch the game for another match!")
                labels["player_turn"].set_text("Game's Over")
                labels["game_status"].set_text("Player {} Won".format(player.name), (255,0,0))

        if globals.game_menu:
            [btn.display(win) for btn in buttons.values()]
            win.blit(img_splash, (globals.window_width / 2 - 450, globals.window_height / 2 - 250))
        else:
            [lbl.draw(win) for lbl in labels.values()]
            [player.grid.render(win) for player in players.values()]

            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and dice_roll_ready and not globals.game_over:
                        current_player.roll()

                        # Switch player
                        if current_player.name=="A":
                            current_player=players["B"]
                            labels["player_turn"].set_text("Its Player B's Turn")
                        elif current_player.name=="B":
                            current_player=players["A"]
                            labels["player_turn"].set_text("Its Player A's Turn")
                        else:
                            labels["player_turn"].set_text("Game has ended", (0,255,0))


        for event in events:
            if event.type == pygame.QUIT:
                globals.run = False

        pygame.display.update()