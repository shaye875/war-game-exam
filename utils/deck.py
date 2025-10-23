
def create_card(rank:str,suite:str):
    n_card = {}
    n_card["rank"] = rank
    n_card["suite"] = suite
    try:
        n_card["value"] = int(rank)
    except:
        if rank == "J":
            n_card["value"] = 11
        elif rank == "Q":
            n_card["value"] = 12
        elif rank == "K":
            n_card["value"] = 13
        elif rank == "A":
            n_card["value"] = 14
    return n_card

def compare_cards(p1:dict,p2:dict):
    if p1["value"] > p2["value"]:
        return "p1"
    elif p2["value"] > p1["value"]:
        return "p2"
    else:
        return "WAR"

def create_deck():
    serye = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suties = ["H","C","D","S"]
    deck = []
    for i in range(len(suties)):
        for j in range(len(serye)):
            deck.append(create_card(serye[j],suties[i]))
    return deck

def shuffle(deck:list[dict]):
    import random
    for _ in range(1000):
       booli = True
       while booli:
          i1 = random.randint(0,51)
          i2 = random.randint(0,51)
          if i1 != i2:
              deck[i1],deck[i2] = deck[i2],deck[i1]
              booli = False
    return deck



