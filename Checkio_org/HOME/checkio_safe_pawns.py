def safe_pawns(pawns):
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    saved_pawns = set()
    pawn_positions = [[pawn[:1], int(pawn[1:])] for pawn in pawns]
    for pawn_position in pawn_positions:
        print(pawn_position)
        p_list = []
        for i in [+1, -1]:
            p_list.append(cols[cols.index(pawn_position[0]) + i] + str(pawn_position[1] + 1))
        print(p_list)
        for item in p_list:
            if item in pawns:
                saved_pawns.add(item)
    return len(saved_pawns)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
