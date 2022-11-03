from hex import Edge, Vertex, Hex
from player import Player
from trade import Trade

def get_clicked(pos):
    for v in Vertex.vertices:
        if v.clicked(pos):
            return v
    for e in Edge.edges:
        if e.clicked(pos):
            return e
    for h in Hex.hexes:
        if h.clicked(pos):
            return h
    if Player.current_player.prompt_clicked(pos):
        Player.current_player.prompt_action()

    if Trade.trade.button_clicked(pos):
        print('clicked')