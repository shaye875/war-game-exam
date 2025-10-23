from utils.deck import create_deck,compare_cards,shuffle
def create_player(name = "AI"):
    n_play = {}
    n_play["name"] = name
    n_play["hand"] = []
    n_play["won_plie"] = []
    return n_play

def init_game():
    p1 = create_player("shaye")
    p2 = create_player()

    deck = create_deck()
    deck = shuffle(deck)
    p1["hand"]+=deck[0:26]
    p2["hand"]+=deck[26:]
    return {"deck":deck,"player_1":p1,"player_2":p2}

def play_round(p1:dict,p2:dict):
    for i in range(len(p1["hand"])):
        win = compare_cards(p1["hand"][0],p2["hand"][0])
        if win == "p1":
            p1["won_plie"].append(p1["hand"].pop(0))
            p1["won_plie"].append(p2["hand"].pop(0))
            print("hand:",i,p1["name"],"win")
        elif win == "p2":
            p2["won_plie"].append(p1["hand"].pop(0))
            p2["won_plie"].append(p2["hand"].pop(0))
            print("hand:", i, p2["name"], "win")
        else:
            print("hand",i,win)
    if len(p1["won_plie"]) > len(p2["won_plie"]):
            print(p1["name"],"win")
    elif len(p1["won_plie"]) < len(p2["won_plie"]):
            print(p2["name"], "win")
    else:
        print("draw")
