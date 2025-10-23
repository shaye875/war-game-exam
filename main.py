from game_logic.game import init_game,play_round
if __name__ == "__main__":
    game = init_game()
    play_round(game["player_1"], game["player_2"])