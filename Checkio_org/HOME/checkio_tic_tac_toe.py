def checkio(game_result):
    if game_result[0][0] == game_result[0][1] == game_result[0][2] or \
            game_result[1][0] == game_result[1][1] == game_result[1][2] or \
            game_result[2][0] == game_result[2][1] == game_result[2][2] or \
            game_result[0][0] == game_result[1][0] == game_result[2][0] or \
            game_result[0][2] == game_result[1][2] == game_result[2][2] or \
            game_result[0][1] == game_result[1][1] == game_result[2][1]:
        return game_result[0][0]
    elif game_result[0][0] == game_result[1][1] == game_result[2][2] or \
            game_result[0][2] == game_result[1][1] == game_result[2][0]:
        return game_result[1][1]
    else:
        return "D"


if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


