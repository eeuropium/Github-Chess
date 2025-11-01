import chess
import json
import sys
# this code updates state.json using python-chess
def main():

    game_id = sys.argv[1]
    move = sys.argv[2]

    # read in state
    with open('state.json', 'r') as f:
        state = json.load(f)

    board = chess.Board(state["board"])

    board.push_uci(move)

    state["board"] = board.fen()
    state["moves"].append(move)
    state["turn"] = "black" if state["turn"] == "white" else "white"

    with open("state.json", "w") as f:
        json.dump(state, f)
    




main()    